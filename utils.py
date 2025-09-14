import json
import os

def load_companies_data():
    """Load companies data from JSON file"""
    try:
        with open('data/companies.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_states_data():
    """Load states data from JSON file"""
    try:
        with open('data/states.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def search_companies(query, state_filter=''):
    """Search companies by name, director, or other fields"""
    companies = load_companies_data()
    results = []
    
    query_lower = query.lower() if query else ''
    
    for company in companies:
        # Apply state filter first
        if state_filter and company['state'].lower() != state_filter.lower():
            continue
            
        # Search in company fields
        if query_lower:
            searchable_text = f"{company['name']} {company['director']} {company['district']} {company['address']}".lower()
            if query_lower in searchable_text:
                results.append(company)
        else:
            results.append(company)
    
    return results

def get_company_by_id(company_id):
    """Get a single company by ID"""
    companies = load_companies_data()
    return next((c for c in companies if c['id'] == company_id), None)
