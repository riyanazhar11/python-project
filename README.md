# Companies House Search Website

A web application similar to Companies House that allows users to search for company information with pagination support up to 5 pages. Built with Python Flask and MongoDB.

## Features

- **Company Search**: Search by company name, number, address, or business activity
- **Pagination**: Display results across up to 5 pages (20 results per page)
- **Company Details**: View comprehensive company information including directors and financial data
- **Responsive Design**: Modern, mobile-friendly interface
- **Fast Search**: Optimized MongoDB queries with text indexing

## Technology Stack

- **Backend**: Python Flask
- **Database**: MongoDB
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design principles

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python-project
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and start MongoDB**
   - Download and install MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community)
   - Start MongoDB service:
     ```bash
     # Windows
     net start MongoDB
     
     # macOS/Linux
     sudo systemctl start mongod
     ```

4. **Seed the database with sample data**
   ```bash
   python seed_data.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the website**
   Open your browser and go to `http://localhost:5000`

## Usage

### Search Companies
- Enter a company name, number, address, or business activity in the search box
- Results will be displayed with pagination (up to 5 pages)
- Click on any company name to view detailed information

### Company Details
- View comprehensive company information including:
  - Company name and number
  - Status and incorporation date
  - Registered address
  - Directors and their roles
  - Financial information (if available)

## API Endpoints

- `GET /` - Home page with search form
- `POST /search` - Search for companies
- `GET /search?query=<term>&page=<number>` - Search with pagination
- `GET /company/<company_id>` - View company details

## Database Schema

### Company Document Structure
```json
{
  "_id": "ObjectId",
  "company_name": "string",
  "company_number": "string",
  "status": "string",
  "incorporation_date": "string",
  "company_type": "string",
  "registered_address": "string",
  "business_activity": "string",
  "directors": [
    {
      "name": "string",
      "role": "string",
      "appointment_date": "string"
    }
  ],
  "financial_info": {
    "turnover": "number",
    "profit": "number",
    "employees": "number"
  }
}
```

## Configuration

Create a `.env` file in the project root with the following variables:
```
MONGODB_URI=mongodb://localhost:27017/
DB_NAME=companies_house
FLASK_ENV=development
FLASK_DEBUG=True
```

## Features Implemented

- ✅ Company search functionality
- ✅ Pagination (up to 5 pages)
- ✅ Company detail pages
- ✅ Responsive design
- ✅ MongoDB integration
- ✅ Sample data seeding
- ✅ Search indexing
- ✅ Error handling
- ✅ Modern UI/UX

## Sample Data

The application comes with 20 sample companies including major tech companies like Apple, Microsoft, Google, Amazon, Tesla, and more. Each company includes realistic data such as:

- Company information
- Director details
- Financial information
- Business activities

## Development

### Project Structure
```
python-project/
├── app.py                 # Main Flask application
├── seed_data.py          # Database seeding script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── templates/           # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── search_results.html
│   ├── company_detail.html
│   └── error.html
└── static/             # Static assets
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

### Adding New Companies

To add new companies to the database, you can either:

1. **Modify the seed_data.py file** and re-run it
2. **Use MongoDB directly** to insert new documents
3. **Create an admin interface** (future enhancement)

## Future Enhancements

- [ ] User authentication and accounts
- [ ] Company registration functionality
- [ ] Advanced search filters
- [ ] Export search results
- [ ] Company comparison feature
- [ ] Real-time data updates
- [ ] API rate limiting
- [ ] Admin dashboard

## License

This project is for educational purposes. Please ensure you comply with any applicable terms of service when using real company data.

## Support

For questions or issues, please create an issue in the repository or contact the development team.
