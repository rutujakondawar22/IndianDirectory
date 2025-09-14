import os
import logging
from flask import Flask
from extensions import db   # ✅ import db from extensions

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "indian-business-directory-secret-key-2024")

# Configure the database - using SQLite for simplicity
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///business_directory.db"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

db.init_app(app)

with app.app_context():
    import models   
    db.create_all()

import routes

if __name__ == "__main__":
    app.run(debug=True)

