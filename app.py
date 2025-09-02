from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
import math

load_dotenv()

app = Flask(__name__)

# MongoDB connection
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'companies_house')

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
companies_collection = db.companies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        page = int(request.form.get('page', 1))
    else:
        query = request.args.get('query', '').strip()
        page = int(request.args.get('page', 1))
    
    if not query:
        return render_template('search_results.html', 
                             companies=[], 
                             query='', 
                             current_page=1, 
                             total_pages=0,
                             total_results=0)
    
    # Search logic
    search_criteria = {
        '$or': [
            {'company_name': {'$regex': query, '$options': 'i'}},
            {'company_number': {'$regex': query, '$options': 'i'}},
            {'registered_address': {'$regex': query, '$options': 'i'}},
            {'business_activity': {'$regex': query, '$options': 'i'}}
        ]
    }
    
    # Calculate pagination
    results_per_page = 5  # Reduced to 5 for easier pagination testing
    skip = (page - 1) * results_per_page
    
    # Get total count
    total_results = companies_collection.count_documents(search_criteria)
    total_pages = min(math.ceil(total_results / results_per_page), 5)  # Limit to 5 pages
    
    # Get companies for current page
    companies = list(companies_collection.find(search_criteria)
                    .skip(skip)
                    .limit(results_per_page)
                    .sort('company_name', 1))
    
    # Convert ObjectId to string for JSON serialization
    for company in companies:
        company['_id'] = str(company['_id'])
    
    return render_template('search_results.html',
                         companies=companies,
                         query=query,
                         current_page=page,
                         total_pages=total_pages,
                         total_results=total_results)

@app.route('/company/<company_id>')
def company_detail(company_id):
    try:
        company = companies_collection.find_one({'_id': ObjectId(company_id)})
        if company:
            company['_id'] = str(company['_id'])
            return render_template('company_detail.html', company=company)
        else:
            return render_template('error.html', message='Company not found'), 404
    except:
        return render_template('error.html', message='Invalid company ID'), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
