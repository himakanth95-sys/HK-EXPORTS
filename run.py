"""Entry point for the Flask application."""
import os
from dotenv import load_dotenv
from app import create_app

# Load environment variables
load_dotenv()

# Create app
app = create_app(os.getenv('FLASK_ENV', 'development'))

# Register database close handler
from app.database import close_db
app.teardown_appcontext(close_db)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', False)
    )
