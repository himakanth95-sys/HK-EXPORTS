"""Application routes organized by blueprint."""
from flask import Blueprint, render_template, request, redirect, url_for, session, g, flash
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
import os
import sqlite3
from app.database import get_db_connection, execute_query, execute_insert

# Define blueprints
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)

# Admin credentials (should be from environment in production)
ADMIN_USER = os.getenv('ADMIN_USER', 'admin')
ADMIN_PASS_HASH = generate_password_hash(os.getenv('ADMIN_PASS', 'hk123'))

def login_required(f):
    """Decorator to require login for admin routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Please login first.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# ========== MAIN ROUTES ==========

@main_bp.route('/')
def home():
    """Customer View: Show all products."""
    try:
        conn = get_db_connection()
        products = conn.execute('SELECT * FROM products WHERE stock > 0 ORDER BY category').fetchall()
        conn.close()
        return render_template('index.html', products=products)
    except sqlite3.Error as e:
        flash('Error fetching products.', 'danger')
        return render_template('index.html', products=[])

@main_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    """Show product details."""
    try:
        conn = get_db_connection()
        product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
        conn.close()
        
        if not product:
            flash('Product not found.', 'danger')
            return redirect(url_for('main.home'))
        
        return render_template('product_detail.html', product=product)
    except sqlite3.Error as e:
        flash('Error fetching product.', 'danger')
        return redirect(url_for('main.home'))

@main_bp.route('/place_order', methods=['POST'])
def place_order():
    """Action: Save customer order details."""
    try:
        buyer_name = request.form.get('buyer_name', '').strip()
        buyer_email = request.form.get('buyer_email', '').strip()
        item_id = request.form.get('item_id', type=int)
        qty = request.form.get('qty', type=int)
        
        # Validation
        if not all([buyer_name, buyer_email, item_id, qty]):
            flash('All fields are required.', 'danger')
            return redirect(url_for('main.home'))
        
        if qty < 1:
            flash('Quantity must be at least 1.', 'danger')
            return redirect(url_for('main.home'))
        
        conn = get_db_connection()
        product = conn.execute('SELECT * FROM products WHERE id = ?', (item_id,)).fetchone()
        
        if not product:
            flash('Product not found.', 'danger')
            conn.close()
            return redirect(url_for('main.home'))
        
        if product['stock'] < qty:
            flash(f'Insufficient stock. Available: {product["stock"]}', 'warning')
            conn.close()
            return redirect(url_for('main.home'))
        
        # Insert order
        try:
            conn.execute('''INSERT INTO orders (buyer_name, buyer_email, item_id, quantity, status) 
                           VALUES (?, ?, ?, ?, ?)''',
                        (buyer_name, buyer_email, item_id, qty, 'pending'))
            conn.commit()
            flash('Order placed successfully! We will contact you soon.', 'success')
        except sqlite3.Error as e:
            conn.rollback()
            flash('Error placing order. Please try again.', 'danger')
        finally:
            conn.close()
        
        return redirect(url_for('main.home'))
    except Exception as e:
        flash('An unexpected error occurred.', 'danger')
        return redirect(url_for('main.home'))

# ========== AUTH ROUTES ==========

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Secure login for admin."""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if not username or not password:
            flash('Username and password are required.', 'danger')
            return render_template('login.html')
        
        if username == ADMIN_USER and check_password_hash(ADMIN_PASS_HASH, password):
            session.permanent = True
            session['logged_in'] = True
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        
        flash('Invalid credentials.', 'danger')
        return render_template('login.html')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    """Logout admin."""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))

# ========== ADMIN ROUTES ==========

@admin_bp.route('/admin')
@login_required
def dashboard():
    """Admin dashboard with stats and products."""
    try:
        conn = get_db_connection()
        
        # Get stats
        stats = conn.execute('''
            SELECT 
                COUNT(*) as total_products,
                SUM(stock) as total_stock,
                COUNT(DISTINCT item_id) as unique_items
            FROM products
        ''').fetchone()
        
        orders_stats = conn.execute('''
            SELECT 
                COUNT(*) as total_orders,
                SUM(quantity) as total_quantity
            FROM orders
        ''').fetchone()
        
        products = conn.execute('SELECT * FROM products ORDER BY category, name').fetchall()
        recent_orders = conn.execute('''
            SELECT orders.*, products.name as product_name 
            FROM orders 
            JOIN products ON orders.item_id = products.id
            ORDER BY orders.order_date DESC 
            LIMIT 10
        ''').fetchall()
        
        conn.close()
        
        return render_template('admin.html', 
                             stats=stats, 
                             orders_stats=orders_stats,
                             products=products, 
                             orders=recent_orders)
    except sqlite3.Error as e:
        flash('Error loading dashboard.', 'danger')
        return render_template('admin.html', stats={}, orders_stats={}, products=[], orders=[])

@admin_bp.route('/admin/product/add', methods=['POST'])
@login_required
def add_product():
    """Add a new product."""
    try:
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        price = request.form.get('price', type=float)
        stock = request.form.get('stock', type=int)
        description = request.form.get('description', '').strip()
        image_url = request.form.get('image_url', '').strip()
        
        # Validation
        if not all([name, category, price, stock is not None]):
            flash('All fields are required.', 'danger')
        elif price <= 0:
            flash('Price must be greater than 0.', 'danger')
        elif stock < 0:
            flash('Stock cannot be negative.', 'danger')
        else:
            conn = get_db_connection()
            try:
                conn.execute('''INSERT INTO products (name, category, price, stock, description, image_url) 
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (name, category, price, stock, description, image_url or None))
                conn.commit()
                flash('Product added successfully!', 'success')
            except sqlite3.IntegrityError:
                flash('Product name already exists.', 'danger')
            finally:
                conn.close()
    except Exception as e:
        flash('Error adding product.', 'danger')
    
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/admin/product/<int:product_id>/edit', methods=['POST'])
@login_required
def edit_product(product_id):
    """Edit an existing product."""
    try:
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        price = request.form.get('price', type=float)
        stock = request.form.get('stock', type=int)
        description = request.form.get('description', '').strip()
        image_url = request.form.get('image_url', '').strip()
        
        # Validation
        if not all([name, category, price, stock is not None]):
            flash('All fields are required.', 'danger')
        elif price <= 0:
            flash('Price must be greater than 0.', 'danger')
        elif stock < 0:
            flash('Stock cannot be negative.', 'danger')
        else:
            conn = get_db_connection()
            conn.execute('''UPDATE products SET name=?, category=?, price=?, stock=?, description=?, image_url=? 
                          WHERE id=?''',
                       (name, category, price, stock, description, image_url or None, product_id))
            conn.commit()
            conn.close()
            flash('Product updated successfully!', 'success')
    except Exception as e:
        flash('Error updating product.', 'danger')
    
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/admin/product/<int:product_id>/delete', methods=['POST'])
@login_required
def delete_product(product_id):
    """Delete a product."""
    try:
        conn = get_db_connection()
        conn.execute('DELETE FROM products WHERE id=?', (product_id,))
        conn.commit()
        conn.close()
        flash('Product deleted successfully!', 'success')
    except Exception as e:
        flash('Error deleting product.', 'danger')
    
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/admin/order/<int:order_id>/status', methods=['POST'])
@login_required
def update_order_status(order_id):
    """Update order status."""
    try:
        status = request.form.get('status', '').strip()
        valid_statuses = ['pending', 'processing', 'completed', 'cancelled']
        
        if status not in valid_statuses:
            flash('Invalid status.', 'danger')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE orders SET status=? WHERE id=?', (status, order_id))
            conn.commit()
            conn.close()
            flash('Order status updated!', 'success')
    except Exception as e:
        flash('Error updating order.', 'danger')
    
    return redirect(url_for('admin.dashboard'))
