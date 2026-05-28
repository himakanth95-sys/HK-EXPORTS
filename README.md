# HK Exports - Seafood Export Platform

A comprehensive e-commerce platform for HK EXPORTS, specializing in premium seafood products including prawns, shrimp, fish, crab, lobster, and squid.

## 🌊 Project Overview

This project includes both:
1. **Frontend Website** (`index.html`, `styles.css`, `script.js`) - Modern responsive website
2. **Flask Backend** - E-commerce application with admin dashboard

---

## 📦 Frontend Website

A beautiful, responsive front-end website for the HK EXPORTS startup.

### Frontend Features

- ✅ **Responsive Design** - Mobile, tablet, and desktop friendly
- ✅ **Modern UI/UX** - Professional design with smooth animations
- ✅ **Product Showcase** - 6 premium seafood products displayed
- ✅ **About Section** - Company information and credentials
- ✅ **Contact Form** - Easy inquiry submission
- ✅ **Navigation** - Sticky header with smooth scrolling
- ✅ **Social Integration** - Social media links in footer

### Frontend Sections

1. **Navigation Bar** - Sticky header with mobile menu
2. **Hero Section** - Eye-catching landing area
3. **Products Gallery** - 
   - Premium Prawns
   - Fresh Shrimp
   - Assorted Fish
   - Fresh Crab
   - Premium Lobster
   - Squid & Octopus
4. **Features Section** - Key advantages of HK EXPORTS
5. **About Section** - Company background
6. **Contact Section** - Contact info and inquiry form
7. **Footer** - Quick links and social media

### Frontend File Structure

```
HK-EXPORTS/
├── index.html       # Main website HTML
├── styles.css       # Complete styling and responsive design
├── script.js        # Interactive functionality
└── README.md        # This file
```

### Quick Start (Frontend Only)

1. Open `index.html` in your browser
2. That's it! No build process needed
3. Fully functional with no dependencies

### Frontend Customization

**Update Company Info** in `index.html`:
- Address, phone, email
- Social media links
- Business hours
- Company description

**Add Products**:
Copy and modify the product card structure in the Products section

**Change Colors** in `styles.css`:
```css
:root {
    --primary-color: #0066cc;
    --secondary-color: #ff6b6b;
    --accent-color: #1abc9c;
}
```

---

## 🚀 Flask Backend (E-Commerce Application)

A full-featured e-commerce platform built with Flask.

### Backend Features

- **Customer Portal** - Browse products and place orders
- **Admin Dashboard** - Manage products, inventory, and orders
- **Secure Authentication** - Password-hashed admin login
- **Database** - SQLite with proper schema
- **Responsive Design** - Bootstrap 5 UI
- **Security** - CSRF protection, SQL injection prevention, password hashing

### Backend Requirements

- Python 3.8+
- Flask 3.0.0
- python-dotenv

### Backend Installation

```bash
# 1. Clone repository
git clone <repo-url>
cd HK-EXPORTS

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
cp .env.example .env

# 5. Run application
python run.py
```

Visit `http://localhost:5000`

### Default Admin Credentials

- **Username**: `admin`
- **Password**: `hk123`

⚠️ **Change these in production!**

### Backend Structure

```
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── product_detail.html
│   │   ├── login.html
│   │   └── admin.html
│   └── static/
│       ├── css/style.css
│       └── js/main.js
├── run.py
├── requirements.txt
└── .env.example
```

### Database Schema

**Products**
- id, name, category, price, stock, description, created_at

**Orders**
- id, buyer_name, buyer_email, item_id, quantity, order_date, status

**Audit Log**
- id, action, details, timestamp

### Admin Features

✅ Product Management (Add, Edit, Delete)
✅ Order Management & Status Tracking
✅ Dashboard Statistics
✅ Inventory Monitoring

### Customer Features

✅ Browse Products
✅ View Product Details
✅ Place Orders
✅ Real-time Pricing

---

## 🔐 Security Features

- ✅ Password hashing (Werkzeug)
- ✅ Session-based authentication
- ✅ CSRF protection
- ✅ HTTP-only secure cookies
- ✅ SQL injection prevention
- ✅ Input validation
- ✅ Error handling & logging

---

## 📊 API Endpoints

### Public Routes
- `GET /` - Home with products
- `GET /product/<id>` - Product details
- `POST /place_order` - Place order

### Auth Routes
- `GET/POST /login` - Admin login
- `GET /logout` - Logout

### Admin Routes (Protected)
- `GET /admin` - Dashboard
- `POST /admin/product/add` - Add product
- `POST /admin/product/<id>/edit` - Edit product
- `POST /admin/product/<id>/delete` - Delete product
- `POST /admin/order/<id>/status` - Update status

---

## 🚀 Production Deployment

### Environment Setup
```
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_COOKIE_SECURE=True
SECRET_KEY=<generate-strong-key>
ADMIN_PASS=<strong-password>
```

### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Deploy to Render

1. Create Web Service in Render
2. Connect Git repository
3. Build command:
```bash
pip install -r requirements.txt
```
4. Start command:
```bash
gunicorn run:app --bind 0.0.0.0:$PORT --workers 2 --log-level info
```
5. Set environment variables:
   - `SECRET_KEY`
   - `ADMIN_USER`
   - `ADMIN_PASS`
   - `DATABASE_PATH=hk_exports.db`

### Deploy to Railway

1. Connect Git repo in Railway
2. Add `Procfile`:
```bash
web: gunicorn run:app --bind 0.0.0.0:$PORT --workers 2 --log-level info
```
3. Set environment variables in Railway dashboard

---

## 🛠️ Technologies

**Frontend**
- HTML5, CSS3, Vanilla JavaScript
- Font Awesome Icons
- Responsive Design (Grid, Flexbox)

**Backend**
- Python, Flask
- SQLite Database
- Bootstrap 5
- Werkzeug (Password Hashing)

---

## 📱 Browser Support

- ✅ Chrome/Edge (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Mobile browsers

---

## 📋 Responsive Breakpoints

- Desktop: 1024px+
- Tablet: 768px - 1023px
- Mobile: Below 768px
- Small Mobile: Below 480px

---

## 📈 Future Enhancements

- [ ] Shopping cart functionality
- [ ] User accounts & authentication
- [ ] Payment gateway integration
- [ ] Order tracking system
- [ ] Blog section
- [ ] Customer testimonials
- [ ] Live chat support
- [ ] Multi-language support
- [ ] Email notifications
- [ ] Advanced analytics

---

## 🤝 Contributing

Feel free to fork, modify, and enhance this project!

---

## 📞 Support

For issues or questions, please open an GitHub issue.

---

## 📄 License

All rights reserved © 2026 HK Exports

---

**Bringing Premium Seafood to Global Markets 🦐🐟**
