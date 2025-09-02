#!/usr/bin/env python3
"""
Startup script for the Companies House Search application.
This script handles the initial setup and starts the Flask application.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_mongodb():
    """Check if MongoDB is running"""
    try:
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
        client.server_info()
        print("✅ MongoDB is running")
        return True
    except Exception as e:
        print("❌ MongoDB is not running or not accessible")
        print("Please start MongoDB before running this application")
        print("Windows: net start MongoDB")
        print("macOS/Linux: sudo systemctl start mongod")
        return False

def check_dependencies():
    """Check if required Python packages are installed"""
    try:
        import flask
        import pymongo
        import dotenv
        print("✅ All required dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def seed_database_if_empty():
    """Seed the database if it's empty"""
    try:
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017/')
        db = client['companies_house']
        
        if db.companies.count_documents({}) == 0:
            print("📊 Database is empty, seeding with sample data...")
            subprocess.run([sys.executable, 'seed_data.py'], check=True)
            print("✅ Database seeded successfully")
        else:
            print("✅ Database already contains data")
    except Exception as e:
        print(f"⚠️  Could not check/seed database: {e}")

def main():
    """Main startup function"""
    print("🚀 Starting Companies House Search Application")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check MongoDB
    if not check_mongodb():
        sys.exit(1)
    
    # Seed database if needed
    seed_database_if_empty()
    
    print("\n🌐 Starting Flask application...")
    print("The application will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the application")
    print("=" * 50)
    
    # Start Flask application
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
