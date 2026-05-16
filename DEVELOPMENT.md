# HK Exports - Development Guide

## 🛠️ Setup Instructions

### 1. Initial Setup
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run the app
python run.py
```

### 2. Access the Application
- **Customer Portal**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/login

### 3. Default Credentials
- Username: `admin`
- Password: `hk123`

## 📚 Adding a New Product

1. Go to Admin Dashboard (http://localhost:5000/admin)
2. Login with admin credentials
3. Fill in the product form:
   - Product Name
   - Category (Prawn/Fish/Other)
   - Price
   - Stock Quantity
   - Description (optional)
4. Click "Add" button

## 🔄 Database Management

### Viewing Database
```bash
# Install sqlite3 browser (optional)
sqlite3 hk_exports.db

# View products
SELECT * FROM products;

# View orders
SELECT * FROM orders;
```

### Reset Database
```bash
# Delete database file
rm hk_exports.db

# Restart app - it will recreate the database
python run.py
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in .env
FLASK_PORT=5001
```

### Database Locked Error
- Close any other instances using the database
- Delete `hk_exports.db` and restart

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## 🔐 Security Notes

- Never commit `.env` file with real credentials
- Change `ADMIN_PASS` before production deployment
- Generate a strong `SECRET_KEY` using:
  ```python
  import secrets
  secrets.token_hex(16)
  ```

## 📝 Code Style Guidelines

- Use snake_case for variables and functions
- Use UPPER_CASE for constants
- Comment complex logic
- Keep functions small and focused
- Use meaningful variable names

## 🧪 Testing the Application

### Test Product Ordering
1. Go to home page
2. Click "View & Order" on any product
3. Fill in buyer details
4. Select quantity
5. Click "Place Order"
6. Check admin panel for new order

### Test Admin Features
1. Add a new product
2. Edit an existing product
3. Change order status
4. Delete a product

## 📦 Dependencies

- **Flask 3.0.0**: Web framework
- **python-dotenv 1.0.0**: Environment variables
- **Werkzeug 3.0.1**: Security and utilities
- **Bootstrap 5.3.0**: CSS framework (from CDN)

## 🚀 Next Steps

### Potential Enhancements
- [ ] Email notifications for orders
- [ ] Payment gateway integration
- [ ] User registration
- [ ] Order history tracking
- [ ] Product reviews/ratings
- [ ] Inventory alerts
- [ ] CSV export for orders
- [ ] SMS notifications
- [ ] Multi-language support
- [ ] Two-factor authentication

---

For more information, see README.md