# HK Exports - Flask E-Commerce Application

A modern, secure, and professional Flask-based e-commerce platform for managing and selling seafood products (prawns and fish).

## 🚀 Features

- **Customer Portal**: Browse products, view details, and place orders
- **Admin Dashboard**: Manage products, inventory, and orders with real-time statistics
- **Secure Authentication**: Password-hashed admin login with session management
- **Database**: SQLite with proper schema and relationships
- **Responsive Design**: Mobile-friendly Bootstrap 5 UI
- **Security Features**:
  - CSRF protection
  - Password hashing
  - Session cookies with security flags
  - SQL injection protection via parameterized queries
  - Input validation and error handling
- **Professional Code Structure**:
  - Blueprints for organized routing
  - Configuration management
  - Separation of concerns (routes, database, config)

## 📋 Requirements

- Python 3.8+
- Flask 3.0.0
- python-dotenv

## 🔧 Installation

1. **Clone the repository**:
```bash
git clone <repo-url>
cd HK-EXPORTS
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run the application**:
```bash
python run.py
```

The app will be available at `http://localhost:5000`

## 🏠 Default Admin Credentials

- **Username**: `admin`
- **Password**: `hk123`

⚠️ **IMPORTANT**: Change these credentials in production!

## 📁 Project Structure

```
HK-EXPORTS/
├── app/
│   ├── __init__.py           # Application factory
│   ├── config.py             # Configuration settings
│   ├── database.py           # Database management
│   ├── routes.py             # All routes (main, auth, admin)
│   ├── templates/
│   │   ├── base.html         # Base template
│   │   ├── index.html        # Home page
│   │   ├── product_detail.html
│   │   ├── login.html        # Admin login
│   │   └── admin.html        # Admin dashboard
│   └── static/
│       ├── css/
│       │   └── style.css     # Custom styles
│       └── js/
│           └── main.js       # Client-side scripts
├── run.py                    # Entry point
├── requirements.txt
├── .env.example
└── README.md
```

## 🗄️ Database Schema

### Products Table
- `id`: Primary key
- `name`: Product name (unique)
- `category`: Product category
- `price`: Product price (must be > 0)
- `stock`: Stock quantity (must be >= 0)
- `description`: Product description
- `created_at`: Timestamp

### Orders Table
- `id`: Primary key
- `buyer_name`: Customer name
- `buyer_email`: Customer email
- `item_id`: Foreign key to products
- `quantity`: Order quantity (must be > 0)
- `order_date`: Order timestamp
- `status`: pending/processing/completed/cancelled

### Audit Log Table
- `id`: Primary key
- `action`: Action description
- `details`: Action details
- `timestamp`: When action occurred

## 🔐 Security Features

- ✅ Password hashing with Werkzeug
- ✅ Session-based authentication
- ✅ CSRF protection via Flask
- ✅ HTTP-only secure cookies
- ✅ SQL injection prevention (parameterized queries)
- ✅ Input validation on all forms
- ✅ Error handling and logging
- ✅ Database foreign key constraints

## 📊 Admin Features

1. **Product Management**:
   - Add new products
   - Edit existing products
   - Delete products
   - Monitor stock levels

2. **Order Management**:
   - View all orders
   - Update order status
   - Track customer details

3. **Dashboard Statistics**:
   - Total products count
   - Total inventory
   - Total orders
   - Units sold

## 🎯 Customer Features

1. **Browse Products**: View all available products with details
2. **Product Details**: See full product information
3. **Place Orders**: Easy order placement with quantity selection
4. **Real-time Pricing**: Automatic price calculation

## 🚀 Deployment

For production deployment:

1. **Update `.env`**:
```
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_COOKIE_SECURE=True
SECRET_KEY=<generate-strong-key>
ADMIN_PASS=<strong-password>
```

2. **Use production WSGI server**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

3. **Enable HTTPS**: Use Nginx/Apache reverse proxy with SSL

## � Deploy to Render or Railway

### Render
1. Create a new Web Service in Render.
2. Connect your Git repository.
3. Use the default branch `main`.
4. For the build command, use:
```bash
pip install -r requirements.txt
```
5. For the start command, use:
```bash
gunicorn run:app --bind 0.0.0.0:$PORT --workers 2 --log-level info
```
6. Set environment variables in Render dashboard:
   - `SECRET_KEY`
   - `ADMIN_USER`
   - `ADMIN_PASS`
   - `DATABASE_PATH=hk_exports.db`

### Railway
1. Connect your Git repository in Railway.
2. Railway will detect a Python project automatically.
3. Add a `Procfile` with:
```bash
web: gunicorn run:app --bind 0.0.0.0:$PORT --workers 2 --log-level info
```
4. Set environment variables in Railway project settings:
   - `SECRET_KEY`
   - `ADMIN_USER`
   - `ADMIN_PASS`
   - `DATABASE_PATH=hk_exports.db`

## �📝 API Endpoints

### Public Routes
- `GET /` - Home page with products
- `GET /product/<id>` - Product detail
- `POST /place_order` - Place an order

### Auth Routes
- `GET/POST /login` - Admin login
- `GET /logout` - Admin logout

### Admin Routes (Protected)
- `GET /admin` - Admin dashboard
- `POST /admin/product/add` - Add product
- `POST /admin/product/<id>/edit` - Edit product
- `POST /admin/product/<id>/delete` - Delete product
- `POST /admin/order/<id>/status` - Update order status

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

All rights reserved © 2026 HK Exports

## 📞 Support

For support, contact the development team.

---

**Happy selling! 🦐🐟**