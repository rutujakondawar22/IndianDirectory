from flask import render_template, request, redirect, url_for, flash, session, jsonify
from models import User
from utils import load_companies_data, load_states_data, search_companies, get_company_by_id
import json
from app import app   # ✅ only import app, not db
from extensions import db   # ✅ import db from extensions instead


@app.route('/')
def index():
    states_data = load_states_data()
    recent_companies = load_companies_data()[:12]  # Show first 12 companies
    return render_template('index.html', states=states_data, companies=recent_companies)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please use a different email.', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access your dashboard.', 'error')
        return redirect(url_for('login'))
    
    states_data = load_states_data()
    companies_count = len(load_companies_data())
    
    return render_template('dashboard.html', states=states_data, companies_count=companies_count)

@app.route('/companies')
def companies():
    state = request.args.get('state', '')
    district = request.args.get('district', '')
    page = int(request.args.get('page', 1))
    per_page = 20
    
    companies_data = load_companies_data()
    states_data = load_states_data()
    
    # Filter by state and district if provided
    if state:
        companies_data = [c for c in companies_data if c['state'].lower() == state.lower()]
    if district:
        companies_data = [c for c in companies_data if c['district'].lower() == district.lower()]
    
    # Pagination
    total = len(companies_data)
    start = (page - 1) * per_page
    end = start + per_page
    companies_page = companies_data[start:end]
    
    has_prev = page > 1
    has_next = end < total
    
    return render_template('companies.html', 
                         companies=companies_page,
                         states=states_data,
                         current_state=state,
                         current_district=district,
                         page=page,
                         has_prev=has_prev,
                         has_next=has_next,
                         total=total)

@app.route('/company/<int:company_id>')
def company_detail(company_id):
    company = get_company_by_id(company_id)
    if not company:
        flash('Company not found.', 'error')
        return redirect(url_for('companies'))
    
    return render_template('company_detail.html', company=company)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    state = request.args.get('state', '')
    
    if query or state:
        results = search_companies(query, state)
    else:
        results = []
    
    states_data = load_states_data()
    
    return render_template('search.html', 
                         results=results, 
                         query=query, 
                         selected_state=state,
                         states=states_data)

@app.route('/api/districts/<state>')
def get_districts(state):
    """API endpoint to get districts for a state"""
    states_data = load_states_data()
    state_info = next((s for s in states_data if s['name'].lower() == state.lower()), None)
    
    if state_info:
        return jsonify(state_info['districts'])
    return jsonify([])
