#!/usr/bin/env python3
"""
Generate Indian Business Directory with 1 Million Companies
This script creates realistic company data across all 28 Indian states
Optimized for large-scale generation with efficient memory usage
"""

import json
import random
import os
from datetime import datetime
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker('en_IN')

print("🇮🇳 Generating 1 Million Indian Companies...")
print("This will take several minutes to complete...")

# Load states data
with open('data/states.json', 'r', encoding='utf-8') as f:
    states_data = json.load(f)

# Optimized data arrays for faster generation
company_suffixes = [
    'Pvt Ltd', 'Ltd', 'Private Limited', 'Limited', 'LLP', 'Enterprises', 'Industries',
    'Trading Co', 'Corporation', 'Group', 'Holdings', 'Solutions', 'Technologies',
    'Services', 'Systems', 'Exports', 'Imports', 'Textiles', 'Motors', 'Steel',
    'Pharmaceuticals', 'Chemicals', 'Construction', 'Engineering', 'Consultancy',
    'Associates', 'Partners', 'Brothers', 'Sons', 'Traders', 'Suppliers', 'Manufacturers'
]

business_sectors = [
    'IT', 'Software', 'Technology', 'Textiles', 'Pharmaceuticals', 'Manufacturing',
    'Automotive', 'Construction', 'Agriculture', 'Food Processing', 'Chemical',
    'Steel', 'Banking', 'Insurance', 'Education', 'Healthcare', 'Real Estate',
    'Retail', 'E-commerce', 'Logistics', 'Energy', 'Mining', 'Tourism',
    'Hospitality', 'Media', 'Entertainment', 'Telecommunications', 'Aviation',
    'Finance', 'Consulting', 'Trading', 'Import Export', 'Electronics', 'Machinery'
]

name_prefixes = [
    'Shree', 'Sri', 'Bharat', 'Indian', 'National', 'Universal', 'Global',
    'Royal', 'Supreme', 'Premier', 'Elite', 'Alpha', 'Omega', 'Delta',
    'Sunrise', 'Golden', 'Silver', 'Star', 'Crown', 'Lotus', 'New',
    'Modern', 'Advanced', 'Super', 'Mega', 'Ultra', 'Prime', 'Best'
]

# Pre-generate common surnames for faster access
common_surnames = [
    'Kumar', 'Singh', 'Sharma', 'Gupta', 'Agarwal', 'Shah', 'Patel', 'Jain',
    'Reddy', 'Rao', 'Nair', 'Menon', 'Iyer', 'Krishnan', 'Chandra', 'Mishra',
    'Tiwari', 'Pandey', 'Srivastava', 'Verma', 'Bansal', 'Mittal', 'Goel',
    'Chopra', 'Malhotra', 'Arora', 'Kapoor', 'Bhatia', 'Sethi', 'Khanna'
]

# Pre-generate city names from all states
all_cities = []
for state in states_data:
    all_cities.extend(state.get('districts', []))

def generate_indian_phone():
    """Generate realistic Indian mobile numbers"""
    prefixes = ['9', '8', '7', '6']
    return f"+91 {random.choice(prefixes)}{random.randint(100000000, 999999999)}"

def generate_email(company_name):
    """Generate email addresses based on company name"""
    domain_suffixes = ['com', 'co.in', 'in', 'org', 'net']
    clean_name = ''.join(c for c in company_name if c.isalnum())[:12].lower()
    if len(clean_name) < 3:
        clean_name = 'company'
    domains = ['gmail', 'yahoo', 'rediffmail', clean_name]
    return f"info@{random.choice(domains)}.{random.choice(domain_suffixes)}"

def generate_website(company_name):
    """Generate website URLs"""
    if random.random() < 0.4:  # 40% don't have websites
        return ""
    clean_name = ''.join(c for c in company_name if c.isalnum())[:15].lower()
    if len(clean_name) < 3:
        clean_name = 'company'
    extensions = ['com', 'co.in', 'in', 'org']
    return f"https://www.{clean_name}.{random.choice(extensions)}"

def generate_company_name():
    """Generate realistic Indian company names"""
    patterns = [
        f"{random.choice(name_prefixes)} {random.choice(common_surnames)} {random.choice(company_suffixes)}",
        f"{random.choice(common_surnames)} {random.choice(business_sectors)} {random.choice(company_suffixes)}",
        f"{random.choice(name_prefixes)} {random.choice(business_sectors)} {random.choice(company_suffixes)}",
        f"{random.choice(all_cities)} {random.choice(business_sectors)} {random.choice(company_suffixes)}",
        f"{random.choice(common_surnames)} & {random.choice(common_surnames)} {random.choice(company_suffixes)}"
    ]
    return random.choice(patterns)

def generate_pincode(state_name):
    """Generate realistic Indian postal codes by state"""
    state_pincode_ranges = {
        'Andhra Pradesh': (500000, 534999),
        'Arunachal Pradesh': (790000, 792999),
        'Assam': (781000, 788999),
        'Bihar': (800000, 855999),
        'Chhattisgarh': (490000, 497999),
        'Goa': (403000, 403999),
        'Gujarat': (360000, 396999),
        'Haryana': (121000, 136999),
        'Himachal Pradesh': (170000, 177999),
        'Jharkhand': (810000, 835999),
        'Karnataka': (560000, 591999),
        'Kerala': (670000, 695999),
        'Madhya Pradesh': (450000, 488999),
        'Maharashtra': (400000, 445999),
        'Manipur': (795000, 795999),
        'Meghalaya': (793000, 794999),
        'Mizoram': (796000, 796999),
        'Nagaland': (797000, 798999),
        'Odisha': (750000, 770999),
        'Punjab': (140000, 160999),
        'Rajasthan': (300000, 345999),
        'Sikkim': (737000, 737999),
        'Tamil Nadu': (600000, 643999),
        'Telangana': (500000, 509999),
        'Tripura': (799000, 799999),
        'Uttar Pradesh': (200000, 285999),
        'Uttarakhand': (240000, 263999),
        'West Bengal': (700000, 743999)
    }
    
    range_tuple = state_pincode_ranges.get(state_name, (100000, 999999))
    return str(random.randint(range_tuple[0], range_tuple[1]))

def generate_address(district, state, pincode):
    """Generate realistic Indian addresses"""
    building_types = ['Plot', 'Building', 'Complex', 'Tower', 'Plaza', 'Center', 'House']
    road_types = ['Road', 'Street', 'Lane', 'Avenue', 'Marg', 'Path']
    
    building = f"{random.randint(1, 999)} {random.choice(building_types)}"
    road = f"{random.choice(common_surnames)} {random.choice(road_types)}"
    
    return f"{building}, {road}, {district}, {state} - {pincode}"

def generate_company_data(company_id, state_info):
    """Generate a single company's data"""
    state_name = state_info['name']
    district = random.choice(state_info.get('districts', [state_name]))
    
    company_name = generate_company_name()
    director_name = f"{fake.first_name()} {random.choice(common_surnames)}"
    phone = generate_indian_phone()
    email = generate_email(company_name)
    website = generate_website(company_name)
    sector = random.choice(business_sectors)
    pincode = generate_pincode(state_name)
    address = generate_address(district, state_name, pincode)
    established = random.randint(1980, 2024)
    
    employee_ranges = ['1-10', '11-50', '51-200', '201-500', '501-1000', '1000+']
    employees = random.choice(employee_ranges)
    
    return {
        'id': company_id,
        'name': company_name,
        'director': director_name,
        'phone': phone,
        'email': email,
        'website': website,
        'state': state_name,
        'district': district,
        'address': address,
        'pincode': pincode,
        'sector': sector,
        'established': established,
        'employees': employees
    }

def calculate_state_distribution(total_companies):
    """Calculate how many companies per state based on population"""
    # Rough population-based distribution
    state_weights = {
        'Uttar Pradesh': 0.16,
        'Maharashtra': 0.12,
        'Bihar': 0.10,
        'West Bengal': 0.09,
        'Madhya Pradesh': 0.07,
        'Tamil Nadu': 0.07,
        'Rajasthan': 0.07,
        'Karnataka': 0.06,
        'Gujarat': 0.06,
        'Andhra Pradesh': 0.05,
        'Odisha': 0.04,
        'Telangana': 0.04,
        'Kerala': 0.03,
        'Jharkhand': 0.03,
        'Assam': 0.03,
        'Punjab': 0.03,
        'Chhattisgarh': 0.03,
        'Haryana': 0.03,
        'Delhi': 0.02,
        'Jammu and Kashmir': 0.01,
        'Uttarakhand': 0.01,
        'Himachal Pradesh': 0.007,
        'Tripura': 0.004,
        'Meghalaya': 0.003,
        'Manipur': 0.003,
        'Nagaland': 0.002,
        'Goa': 0.001,
        'Arunachal Pradesh': 0.001,
        'Mizoram': 0.001,
        'Sikkim': 0.0006
    }
    
    distribution = {}
    remaining = total_companies
    
    for state in states_data:
        state_name = state['name']
        weight = state_weights.get(state_name, 0.01)  # Default 1% for unlisted states
        count = int(total_companies * weight)
        distribution[state_name] = max(count, 100)  # Minimum 100 companies per state
        remaining -= distribution[state_name]
    
    # Distribute remaining companies to major states
    major_states = ['Maharashtra', 'Uttar Pradesh', 'Karnataka', 'Tamil Nadu', 'Gujarat']
    if remaining > 0:
        per_state = remaining // len(major_states)
        for state in major_states:
            distribution[state] += per_state
    
    return distribution

def main():
    """Main function to generate 1 million companies"""
    target_companies = 1000000
    print(f"Target: {target_companies:,} companies")
    
    # Calculate distribution
    state_distribution = calculate_state_distribution(target_companies)
    
    print("\nDistribution by state:")
    for state, count in sorted(state_distribution.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {state}: {count:,}")
    print("  ... and others")
    
    # Generate companies in batches to manage memory
    batch_size = 10000
    total_generated = 0
    all_companies = []
    
    print(f"\nStarting generation in batches of {batch_size:,}...")
    
    for state_info in states_data:
        state_name = state_info['name']
        target_count = state_distribution.get(state_name, 1000)
        
        print(f"\nGenerating {target_count:,} companies for {state_name}...")
        
        state_companies = []
        for i in range(target_count):
            company_id = total_generated + i + 1
            company = generate_company_data(company_id, state_info)
            state_companies.append(company)
            
            # Progress indicator
            if (i + 1) % 5000 == 0:
                print(f"  Generated {i + 1:,}/{target_count:,} for {state_name}")
        
        all_companies.extend(state_companies)
        total_generated += len(state_companies)
        
        print(f"✓ Completed {state_name}: {len(state_companies):,} companies")
        print(f"Total so far: {total_generated:,}")
    
    print(f"\n🎉 Generated {len(all_companies):,} companies total!")
    
    # Save to file
    print("\nSaving to data/companies_1million.json...")
    with open('data/companies_1million.json', 'w', encoding='utf-8') as f:
        json.dump(all_companies, f, ensure_ascii=False, indent=None, separators=(',', ':'))
    
    # Also update the original file for compatibility
    print("Updating data/companies.json...")
    with open('data/companies.json', 'w', encoding='utf-8') as f:
        json.dump(all_companies, f, ensure_ascii=False, indent=None, separators=(',', ':'))
    
    # Generate statistics
    print("\n=== FINAL STATISTICS ===")
    print(f"Total Companies: {len(all_companies):,}")
    print(f"File size: ~{os.path.getsize('data/companies_1million.json') / (1024*1024):.1f} MB")
    
    # Top states by company count
    state_counts = {}
    sector_counts = {}
    
    for company in all_companies:
        state = company['state']
        sector = company['sector']
        
        state_counts[state] = state_counts.get(state, 0) + 1
        sector_counts[sector] = sector_counts.get(sector, 0) + 1
    
    print(f"\nTop 10 States by Company Count:")
    for state, count in sorted(state_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {state}: {count:,}")
    
    print(f"\nTop 10 Business Sectors:")
    for sector, count in sorted(sector_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {sector}: {count:,}")
    
    print(f"\n✅ Successfully generated {len(all_companies):,} Indian companies!")
    print("Files saved:")
    print("  - data/companies_1million.json (new large dataset)")
    print("  - data/companies.json (updated for compatibility)")

if __name__ == "__main__":
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n⏱️  Total generation time: {duration}")