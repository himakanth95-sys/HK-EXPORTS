"""Database initialization and connection management."""
import sqlite3
import os
from flask import g, current_app

def get_db_connection():
    """Get database connection with proper error handling."""
    if 'db' not in g:
        db_path = current_app.config['DATABASE']
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
        # Enable foreign key constraints
        g.db.execute('PRAGMA foreign_keys = ON')
    return g.db

def close_db(e=None):
    """Close database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Initialize database with tables and seed sample data."""
    db_path = current_app.config['DATABASE']
    db_exists = os.path.exists(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Products table
        cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         name TEXT NOT NULL UNIQUE,
                         category TEXT NOT NULL,
                         price REAL NOT NULL CHECK(price > 0),
                         stock INTEGER NOT NULL CHECK(stock >= 0),
                         description TEXT,
                         image_url TEXT,
                         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
        # Orders table
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         buyer_name TEXT NOT NULL,
                         buyer_email TEXT NOT NULL,
                         item_id INTEGER NOT NULL,
                         quantity INTEGER NOT NULL CHECK(quantity > 0),
                         order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                         status TEXT DEFAULT 'pending',
                         FOREIGN KEY(item_id) REFERENCES products(id) ON DELETE CASCADE)''')
        
        # Audit log table
        cursor.execute('''CREATE TABLE IF NOT EXISTS audit_log
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         action TEXT NOT NULL,
                         details TEXT,
                         timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        # Ensure existing table has image_url for compatibility
        cursor.execute("PRAGMA table_info(products)")
        columns = [row[1] for row in cursor.fetchall()]
        if 'image_url' not in columns:
            cursor.execute('ALTER TABLE products ADD COLUMN image_url TEXT')

        # Seed sample products only when the table is empty
        product_count = cursor.execute('SELECT COUNT(*) FROM products').fetchone()[0]
        if product_count == 0:
            default_products = [
                ('King Prawns (Frozen)', 'Prawn', 1215.0, 150, 'Premium frozen king prawns from Bangladesh. Perfect size for grilling and frying.', '/static/images/king_prawns.jpg'),
                ('Tiger Prawns (Premium)', 'Prawn', 1890.0, 120, 'Grade A tiger prawns. Best for special occasions and restaurants.', '/static/images/tiger_prawns.jpg'),
                ('Vannamei Prawns', 'Prawn', 855.0, 200, 'Fresh vannamei prawns. Ideal for commercial and retail purposes.', '/static/images/vannamei_prawns.jpg'),
                ('Hilsa Fish (Ilish)', 'Fish', 675.0, 80, 'The national fish of Bangladesh. Fresh and delicious. Weight: 1-1.5 kg', '/static/images/hilsa_fish.jpg'),
                ('Tilapia (Fresh)', 'Fish', 405.0, 180, 'High-quality fresh tilapia. Great for curry and frying.', '/static/images/tilapia_fish.jpg'),
                ('Catfish (Pabda)', 'Fish', 495.0, 160, 'Fresh catfish perfect for traditional Bengali recipes.', '/static/images/catfish.jpg'),
                ('Crab (Live)', 'Crab', 1485.0, 60, 'Live mud crabs. Perfect for seafood lovers. Each piece: 400-500g', '/static/images/crab.jpg'),
                ('Shrimp (Dried)', 'Shrimp', 1350.0, 100, 'Premium dried shrimp for cooking and export.', '/static/images/dried_shrimp.jpg'),
                ('Mullet Fish', 'Fish', 540.0, 140, 'Fresh mullet fish. High protein content.', '/static/images/mullet_fish.jpg'),
                ('Snapper (Red)', 'Fish', 1125.0, 70, 'Premium red snapper. Perfect for grilling and baking.', '/static/images/red_snapper.jpg')
            ]
            cursor.executemany('''INSERT INTO products (name, category, price, stock, description, image_url)
                                  VALUES (?, ?, ?, ?, ?, ?)''', default_products)

        conn.commit()
        if not db_exists:
            print("✓ Database initialized successfully")
    except sqlite3.Error as e:
        print(f"✗ Database initialization error: {e}")
        raise
    finally:
        conn.close()

def execute_query(query, params=None, fetch_one=False):
    """Execute database query with error handling."""
    try:
        db = get_db_connection()
        cursor = db.execute(query, params or [])
        
        if fetch_one:
            return cursor.fetchone()
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise

def execute_insert(query, params=None):
    """Execute insert query and return last row id."""
    try:
        db = get_db_connection()
        cursor = db.execute(query, params or [])
        db.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        raise
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
