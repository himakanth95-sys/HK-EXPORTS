#!/bin/bash

# HK Exports - Quick Setup Script

echo "🚀 Setting up HK Exports Application..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📚 Installing dependencies..."
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

# Setup .env file
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file..."
    cp .env.example .env
    echo "✓ .env file created (Update with your settings)"
else
    echo "✓ .env file already exists"
fi

# Create database
if [ ! -f "hk_exports.db" ]; then
    echo "🗄️  Initializing database..."
    python3 -c "from app import create_app; app = create_app()" 2>/dev/null
    echo "✓ Database initialized"
else
    echo "✓ Database already exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the application, run:"
echo "   python run.py"
echo ""
echo "📖 Access the application at:"
echo "   http://localhost:5000"
echo ""
echo "🔐 Admin credentials:"
echo "   Username: admin"
echo "   Password: hk123"
echo ""
