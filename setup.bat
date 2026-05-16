@echo off
REM HK Exports - Quick Setup Script for Windows

echo 🚀 Setting up HK Exports Application...

REM Check Python version
python --version
echo ✓ Python found

REM Create virtual environment
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo 📚 Installing dependencies...
pip install -q -r requirements.txt
echo ✓ Dependencies installed

REM Setup .env file
if not exist ".env" (
    echo ⚙️  Creating .env file...
    copy .env.example .env
    echo ✓ .env file created (Update with your settings)
) else (
    echo ✓ .env file already exists
)

echo.
echo ✅ Setup complete!
echo.
echo 🚀 To start the application, run:
echo    python run.py
echo.
echo 📖 Access the application at:
echo    http://localhost:5000
echo.
echo 🔐 Admin credentials:
echo    Username: admin
echo    Password: hk123
echo.
pause
