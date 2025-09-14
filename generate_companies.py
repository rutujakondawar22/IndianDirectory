#!/usr/bin/env python3
"""
Generate Indian Business Directory with 10,000+ companies
This script creates realistic company data across all 28 Indian states
"""

import json
import random
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Load states data
with open('data/states.json', 'r', encoding='utf-8') as f:
    states_data = json.load(f)

# Indian company name patterns and suffixes
company_suffixes = [
    'Pvt Ltd', 'Ltd', 'Private Limited', 'Limited', 'LLP', 'Enterprises', 'Industries',
    'Trading Co', 'Corporation', 'Group', 'Holdings', 'Solutions', 'Technologies',
    'Services', 'Systems', 'Exports', 'Imports', 'Textiles', 'Motors', 'Steel',
    'Pharmaceuticals', 'Chemicals', 'Construction', 'Engineering', 'Consultancy'
]

# Indian business sectors
business_sectors = [
    'Information Technology', 'Textiles', 'Pharmaceuticals', 'Manufacturing',
    'Automotive', 'Construction', 'Agriculture', 'Food Processing', 'Chemical',
    'Steel', 'Banking', 'Insurance', 'Education', 'Healthcare', 'Real Estate',
    'Retail', 'E-commerce', 'Logistics', 'Energy', 'Mining', 'Tourism',
    'Hospitality', 'Media', 'Entertainment', 'Telecommunications', 'Aviation'
]

# Common Indian business name prefixes
name_prefixes = [
    'Shree', 'Sri', 'Bharat', 'Indian', 'National', 'Universal', 'Global',
    'Royal', 'Supreme', 'Premier', 'Elite', 'Alpha', 'Omega', 'Delta',
    'Sunrise', 'Sunset', 'Golden', 'Silver', 'Diamond', 'Star', 'Crown',
    'Lotus', 'Himalaya', 'Ganges', 'Yamuna', 'Kaveri', 'Godavari'
]

# Generate Indian phone numbers
def generate_indian_phone():
    prefixes = ['9', '8', '7', '6']
    return f"+91 {random.choice(prefixes)}{random.randint(100000000, 999999999)}"

# Generate Indian email addresses
def generate_email(company_name):
    domain_suffixes = ['com', 'co.in', 'in', 'org', 'net']
    clean_name = company_name.replace(' ', '').replace('.', '').lower()[:15]
    domains = ['gmail', 'yahoo', 'outlook', 'rediffmail', 'hotmail', clean_name]
    return f"info@{random.choice(domains)}.{random.choice(domain_suffixes)}"

# Generate website URLs
def generate_website(company_name):
    if random.random() < 0.3:  # 30% don't have websites
        return ""
    clean_name = company_name.replace(' ', '').replace('.', '').lower()[:20]
    domains = [clean_name, f"{clean_name}india", f"{clean_name}ltd"]
    extensions = ['com', 'co.in', 'in', 'org']
    return f"https://www.{random.choice(domains)}.{random.choice(extensions)}"

# Generate realistic Indian company names
def generate_company_name():
    patterns = [
        f"{random.choice(name_prefixes)} {fake.last_name()} {random.choice(company_suffixes)}",
        f"{fake.last_name()} {random.choice(business_sectors)} {random.choice(company_suffixes)}",
        f"{random.choice(name_prefixes)} {random.choice(business_sectors)} {random.choice(company_suffixes)}",
        f"{fake.city()} {random.choice(business_sectors)} {random.choice(company_suffixes)}",
        f"{fake.last_name()} & {fake.last_name()} {random.choice(company_suffixes)}"
    ]
    return random.choice(patterns)

# Generate Indian postal codes
def generate_pincode():
    return f"{random.randint(100000, 999999)}"

# Generate realistic Indian addresses
def generate_address():
    building_types = ['Building', 'Complex', 'Plaza', 'Tower', 'Centre', 'Bhavan']
    road_types = ['Road', 'Street', 'Lane', 'Marg', 'Cross', 'Circle', 'Nagar']
    
    address_parts = [
        f"{random.randint(1, 999)} {fake.street_name()} {random.choice(road_types)}",
        f"{fake.last_name()} {random.choice(building_types)}",
        f"Near {fake.street_name()} {random.choice(['Station', 'Market', 'Hospital', 'School'])}"
    ]
    
    return f"{random.choice(address_parts)}, {fake.city()}"

def generate_companies():
    companies = []
    company_id = 1
    
    print("Generating 10,000+ Indian companies...")
    
    for state in states_data:
        state_name = state['name']
        districts = state['districts']
        
        # Generate different number of companies per state based on population/economy
        major_states = ['Maharashtra', 'Tamil Nadu', 'Karnataka', 'Gujarat', 'Uttar Pradesh', 
                       'West Bengal', 'Rajasthan', 'Andhra Pradesh', 'Telangana', 'Haryana']
        
        if state_name in major_states:
            companies_per_state = random.randint(500, 800)  # Major business states
        else:
            companies_per_state = random.randint(200, 400)  # Other states
        
        print(f"Generating {companies_per_state} companies for {state_name}...")
        
        for _ in range(companies_per_state):
            district = random.choice(districts)
            company_name = generate_company_name()
            
            company = {
                'id': company_id,
                'name': company_name,
                'director': fake.name(),
                'phone': generate_indian_phone(),
                'email': generate_email(company_name),
                'website': generate_website(company_name),
                'address': generate_address(),
                'district': district,
                'state': state_name,
                'pincode': generate_pincode(),
                'sector': random.choice(business_sectors),
                'established': random.randint(1980, 2024),
                'employees': random.choice([
                    '1-10', '11-50', '51-200', '201-500', '501-1000', '1000+'
                ])
            }
            
            companies.append(company)
            company_id += 1
    
    print(f"Generated {len(companies)} companies total!")
    return companies

def main():
    companies = generate_companies()
    
    # Save to JSON file
    with open('data/companies.json', 'w', encoding='utf-8') as f:
        json.dump(companies, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully saved {len(companies)} companies to data/companies.json")
    
    # Print statistics
    print("\n=== STATISTICS ===")
    print(f"Total Companies: {len(companies)}")
    
    # Companies by state
    state_counts = {}
    for company in companies:
        state = company['state']
        state_counts[state] = state_counts.get(state, 0) + 1
    
    print("\nTop 10 States by Company Count:")
    sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)
    for state, count in sorted_states[:10]:
        print(f"  {state}: {count}")
    
    # Sector distribution
    sector_counts = {}
    for company in companies:
        sector = company['sector']
        sector_counts[sector] = sector_counts.get(sector, 0) + 1
    
    print("\nTop 10 Business Sectors:")
    sorted_sectors = sorted(sector_counts.items(), key=lambda x: x[1], reverse=True)
    for sector, count in sorted_sectors[:10]:
        print(f"  {sector}: {count}")

if __name__ == "__main__":
    main()