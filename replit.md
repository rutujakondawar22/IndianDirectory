# Indian Business Directory

## Overview

The Indian Business Directory is a Flask-based web application that provides a comprehensive directory of Indian companies organized by state and district. The platform allows users to search, browse, and view detailed information about businesses across India's 28 states and union territories. The application features user authentication, advanced search capabilities, and a responsive web interface built with Bootstrap.

## User Preferences

**Communication Style**: Simple, everyday language
**Design Preference**: Simple and clean design, no extra features
**Development Requirements**: Easy to run on VS Code without downloading extra libraries
**Color Scheme**: 2-3 color combinations only
**Code Complexity**: Easy to execute and understandable code
**Feature Priority**: Basic functionality over advanced features

## System Architecture

### Simple HTML Architecture (Updated August 2025)
The user requested a simplified approach focusing on ease of use and VS Code compatibility:
- **simple_index.html**: Single-file website with embedded CSS and JavaScript
- **simple_style.css**: Optional separate stylesheet for organization
- **data/companies.json**: 12,331 Indian companies database
- **data/states.json**: Indian states and districts mapping
- **README.md**: Simple instructions for VS Code execution

**Color Scheme**: 3-color design - Orange (#ff6b35), Green (#138808), White (#ffffff)
**No Dependencies**: Pure HTML, CSS, JavaScript - no libraries needed
**VS Code Ready**: Can be opened directly with Live Server extension

### Previous Flask Framework Architecture
The application uses Flask as the primary web framework with a modular structure:
- **app.py**: Main application factory with SQLAlchemy database configuration
- **routes.py**: Route handlers for all web endpoints (home, search, user management)
- **models.py**: SQLAlchemy database models (currently User model for authentication)
- **utils.py**: Helper functions for data loading and business logic
- **main.py**: Application entry point

### Database Architecture
**Primary Storage**: SQLite database (`business_directory.db`) with SQLAlchemy ORM
- User authentication table with password hashing using Werkzeug
- Session-based user management without Flask-Login dependency
- Database connection pooling with recycle and pre-ping configuration

**Data Storage**: JSON-based company and state data
- `data/companies.json`: Company directory data (currently empty, ready for population)
- `data/states.json`: Indian states and districts mapping for geographical organization

### Frontend Architecture
**Template Engine**: Jinja2 with component-based template inheritance
- `base.html`: Master template with navigation and common elements
- Specialized templates for different views (index, search, company details, user auth)
- Bootstrap 5 integration for responsive design

**Static Assets**: 
- Custom CSS with Indian-themed color palette and gradients
- JavaScript for interactive features, search debouncing, and animations
- Font Awesome icons for enhanced UI elements

### Authentication System
Simple session-based authentication without external dependencies:
- User registration and login with password hashing
- Session management using Flask's built-in session handling
- Username and email uniqueness validation

### Search and Filtering System
Multi-criteria search functionality:
- Text-based search across company names, directors, and locations
- State and district-based geographical filtering
- Real-time search with debouncing for better user experience

## External Dependencies

### Core Framework Dependencies
- **Flask**: Web application framework
- **SQLAlchemy/Flask-SQLAlchemy**: Database ORM and integration
- **Werkzeug**: Password hashing and security utilities

### Frontend Dependencies (CDN-based)
- **Bootstrap 5**: CSS framework for responsive design
- **Font Awesome 6**: Icon library for enhanced UI

### Data Dependencies
- **JSON Files**: Local data storage for company directory and geographical data
- **SQLite**: Embedded database for user management and session storage

### Development Dependencies
- Python built-in modules: `os`, `logging`, `json`, `datetime`
- No external API integrations currently implemented
- No third-party authentication providers