from pymongo import MongoClient
import random
from datetime import datetime, timedelta

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['companies_house']
companies_collection = db.companies

# Sample company data
sample_companies = [
    {
        "company_name": "Apple Inc UK",
        "company_number": "12345678",
        "status": "Active",
        "incorporation_date": "2010-03-15",
        "company_type": "Private Limited Company",
        "registered_address": "1 Apple Park Way, Cupertino, CA 95014, United States",
        "business_activity": "Technology and Consumer Electronics",
        "directors": [
            {
                "name": "Tim Cook",
                "role": "Chief Executive Officer",
                "appointment_date": "2011-08-24"
            },
            {
                "name": "Luca Maestri",
                "role": "Chief Financial Officer",
                "appointment_date": "2014-06-01"
            }
        ],
        "financial_info": {
            "turnover": 365817000000,
            "profit": 94680000000,
            "employees": 164000
        }
    },
    {
        "company_name": "Microsoft Corporation UK",
        "company_number": "23456789",
        "status": "Active",
        "incorporation_date": "1981-04-04",
        "company_type": "Public Limited Company",
        "registered_address": "One Microsoft Way, Redmond, WA 98052, United States",
        "business_activity": "Software Development and Cloud Services",
        "directors": [
            {
                "name": "Satya Nadella",
                "role": "Chief Executive Officer",
                "appointment_date": "2014-02-04"
            },
            {
                "name": "Amy Hood",
                "role": "Chief Financial Officer",
                "appointment_date": "2013-05-08"
            }
        ],
        "financial_info": {
            "turnover": 168088000000,
            "profit": 61271000000,
            "employees": 221000
        }
    },
    {
        "company_name": "Google LLC UK",
        "company_number": "34567890",
        "status": "Active",
        "incorporation_date": "1998-09-04",
        "company_type": "Limited Liability Company",
        "registered_address": "1600 Amphitheatre Parkway, Mountain View, CA 94043, United States",
        "business_activity": "Internet Services and Advertising",
        "directors": [
            {
                "name": "Sundar Pichai",
                "role": "Chief Executive Officer",
                "appointment_date": "2015-10-02"
            },
            {
                "name": "Ruth Porat",
                "role": "Chief Financial Officer",
                "appointment_date": "2015-05-26"
            }
        ],
        "financial_info": {
            "turnover": 282836000000,
            "profit": 76033000000,
            "employees": 190234
        }
    },
    {
        "company_name": "Amazon UK Services Ltd",
        "company_number": "45678901",
        "status": "Active",
        "incorporation_date": "1994-07-05",
        "company_type": "Private Limited Company",
        "registered_address": "410 Terry Avenue North, Seattle, WA 98109, United States",
        "business_activity": "E-commerce and Cloud Computing",
        "directors": [
            {
                "name": "Andy Jassy",
                "role": "Chief Executive Officer",
                "appointment_date": "2021-07-05"
            },
            {
                "name": "Brian Olsavsky",
                "role": "Chief Financial Officer",
                "appointment_date": "2015-06-01"
            }
        ],
        "financial_info": {
            "turnover": 469822000000,
            "profit": 33364000000,
            "employees": 1541000
        }
    },
    {
        "company_name": "Tesla Motors UK Ltd",
        "company_number": "56789012",
        "status": "Active",
        "incorporation_date": "2003-07-01",
        "company_type": "Public Limited Company",
        "registered_address": "1 Tesla Road, Austin, TX 78725, United States",
        "business_activity": "Electric Vehicles and Energy Storage",
        "directors": [
            {
                "name": "Elon Musk",
                "role": "Chief Executive Officer",
                "appointment_date": "2008-10-01"
            },
            {
                "name": "Zachary Kirkhorn",
                "role": "Chief Financial Officer",
                "appointment_date": "2019-01-01"
            }
        ],
        "financial_info": {
            "turnover": 81562000000,
            "profit": 15000000000,
            "employees": 127855
        }
    },
    {
        "company_name": "Meta Platforms UK Ltd",
        "company_number": "67890123",
        "status": "Active",
        "incorporation_date": "2004-02-04",
        "company_type": "Public Limited Company",
        "registered_address": "1 Hacker Way, Menlo Park, CA 94025, United States",
        "business_activity": "Social Media and Virtual Reality",
        "directors": [
            {
                "name": "Mark Zuckerberg",
                "role": "Chief Executive Officer",
                "appointment_date": "2004-02-04"
            },
            {
                "name": "Susan Li",
                "role": "Chief Financial Officer",
                "appointment_date": "2022-11-01"
            }
        ],
        "financial_info": {
            "turnover": 134902000000,
            "profit": 39370000000,
            "employees": 86482
        }
    },
    {
        "company_name": "Netflix UK Ltd",
        "company_number": "78901234",
        "status": "Active",
        "incorporation_date": "1997-08-29",
        "company_type": "Public Limited Company",
        "registered_address": "100 Winchester Circle, Los Gatos, CA 95032, United States",
        "business_activity": "Streaming Entertainment Services",
        "directors": [
            {
                "name": "Ted Sarandos",
                "role": "Co-Chief Executive Officer",
                "appointment_date": "2020-07-01"
            },
            {
                "name": "Greg Peters",
                "role": "Co-Chief Executive Officer",
                "appointment_date": "2023-01-01"
            }
        ],
        "financial_info": {
            "turnover": 31615000000,
            "profit": 5508000000,
            "employees": 12800
        }
    },
    {
        "company_name": "Uber Technologies UK Ltd",
        "company_number": "89012345",
        "status": "Active",
        "incorporation_date": "2009-03-01",
        "company_type": "Public Limited Company",
        "registered_address": "1455 Market Street, San Francisco, CA 94103, United States",
        "business_activity": "Transportation and Delivery Services",
        "directors": [
            {
                "name": "Dara Khosrowshahi",
                "role": "Chief Executive Officer",
                "appointment_date": "2017-08-30"
            },
            {
                "name": "Nelson Chai",
                "role": "Chief Financial Officer",
                "appointment_date": "2018-09-10"
            }
        ],
        "financial_info": {
            "turnover": 31757000000,
            "profit": 1885000000,
            "employees": 32200
        }
    },
    {
        "company_name": "Airbnb UK Ltd",
        "company_number": "90123456",
        "status": "Active",
        "incorporation_date": "2008-08-01",
        "company_type": "Public Limited Company",
        "registered_address": "888 Brannan Street, San Francisco, CA 94103, United States",
        "business_activity": "Online Marketplace for Short-term Rentals",
        "directors": [
            {
                "name": "Brian Chesky",
                "role": "Chief Executive Officer",
                "appointment_date": "2008-08-01"
            },
            {
                "name": "Dave Stephenson",
                "role": "Chief Financial Officer",
                "appointment_date": "2018-01-01"
            }
        ],
        "financial_info": {
            "turnover": 8390000000,
            "profit": 1890000000,
            "employees": 6600
        }
    },
    {
        "company_name": "Spotify Technology UK Ltd",
        "company_number": "01234567",
        "status": "Active",
        "incorporation_date": "2006-04-23",
        "company_type": "Public Limited Company",
        "registered_address": "Birger Jarlsgatan 61, 113 56 Stockholm, Sweden",
        "business_activity": "Music Streaming and Audio Content",
        "directors": [
            {
                "name": "Daniel Ek",
                "role": "Chief Executive Officer",
                "appointment_date": "2006-04-23"
            },
            {
                "name": "Paul Vogel",
                "role": "Chief Financial Officer",
                "appointment_date": "2020-01-01"
            }
        ],
        "financial_info": {
            "turnover": 11726000000,
            "profit": -430000000,
            "employees": 9000
        }
    },
    {
        "company_name": "Twitter UK Ltd",
        "company_number": "11223344",
        "status": "Dissolved",
        "incorporation_date": "2006-03-21",
        "company_type": "Public Limited Company",
        "registered_address": "1355 Market Street, San Francisco, CA 94103, United States",
        "business_activity": "Social Media and Microblogging",
        "directors": [
            {
                "name": "Elon Musk",
                "role": "Chief Executive Officer",
                "appointment_date": "2022-10-27"
            }
        ],
        "financial_info": {
            "turnover": 4040000000,
            "profit": -221000000,
            "employees": 7500
        }
    },
    {
        "company_name": "LinkedIn Corporation UK",
        "company_number": "22334455",
        "status": "Active",
        "incorporation_date": "2002-12-28",
        "company_type": "Subsidiary Company",
        "registered_address": "1000 W Maude Ave, Sunnyvale, CA 94085, United States",
        "business_activity": "Professional Networking and Recruitment",
        "directors": [
            {
                "name": "Ryan Roslansky",
                "role": "Chief Executive Officer",
                "appointment_date": "2020-06-01"
            }
        ],
        "financial_info": {
            "turnover": 10000000000,
            "profit": 2000000000,
            "employees": 21000
        }
    },
    {
        "company_name": "Zoom Video Communications UK Ltd",
        "company_number": "33445566",
        "status": "Active",
        "incorporation_date": "2011-04-21",
        "company_type": "Public Limited Company",
        "registered_address": "55 Almaden Blvd, San Jose, CA 95113, United States",
        "business_activity": "Video Conferencing and Communication Software",
        "directors": [
            {
                "name": "Eric Yuan",
                "role": "Chief Executive Officer",
                "appointment_date": "2011-04-21"
            },
            {
                "name": "Kelly Steckelberg",
                "role": "Chief Financial Officer",
                "appointment_date": "2017-01-01"
            }
        ],
        "financial_info": {
            "turnover": 4260000000,
            "profit": 1375000000,
            "employees": 8500
        }
    },
    {
        "company_name": "Slack Technologies UK Ltd",
        "company_number": "44556677",
        "status": "Active",
        "incorporation_date": "2009-08-01",
        "company_type": "Subsidiary Company",
        "registered_address": "500 Howard Street, San Francisco, CA 94105, United States",
        "business_activity": "Business Communication and Collaboration",
        "directors": [
            {
                "name": "Stewart Butterfield",
                "role": "Chief Executive Officer",
                "appointment_date": "2009-08-01"
            }
        ],
        "financial_info": {
            "turnover": 902000000,
            "profit": -147000000,
            "employees": 2000
        }
    },
    {
        "company_name": "Shopify UK Ltd",
        "company_number": "55667788",
        "status": "Active",
        "incorporation_date": "2004-09-28",
        "company_type": "Public Limited Company",
        "registered_address": "150 Elgin Street, Ottawa, ON K2P 1L4, Canada",
        "business_activity": "E-commerce Platform and Online Store Solutions",
        "directors": [
            {
                "name": "Tobias Lütke",
                "role": "Chief Executive Officer",
                "appointment_date": "2004-09-28"
            },
            {
                "name": "Amy Shapero",
                "role": "Chief Financial Officer",
                "appointment_date": "2018-09-01"
            }
        ],
        "financial_info": {
            "turnover": 4600000000,
            "profit": 291000000,
            "employees": 10000
        }
    },
    {
        "company_name": "Square UK Ltd",
        "company_number": "66778899",
        "status": "Active",
        "incorporation_date": "2009-02-01",
        "company_type": "Public Limited Company",
        "registered_address": "1455 Market Street, San Francisco, CA 94103, United States",
        "business_activity": "Financial Services and Payment Processing",
        "directors": [
            {
                "name": "Jack Dorsey",
                "role": "Chief Executive Officer",
                "appointment_date": "2009-02-01"
            },
            {
                "name": "Amrita Ahuja",
                "role": "Chief Financial Officer",
                "appointment_date": "2019-01-01"
            }
        ],
        "financial_info": {
            "turnover": 17520000000,
            "profit": 166000000,
            "employees": 8000
        }
    },
    {
        "company_name": "Stripe UK Ltd",
        "company_number": "77889900",
        "status": "Active",
        "incorporation_date": "2010-09-01",
        "company_type": "Private Limited Company",
        "registered_address": "510 Townsend Street, San Francisco, CA 94103, United States",
        "business_activity": "Online Payment Processing and Financial Infrastructure",
        "directors": [
            {
                "name": "Patrick Collison",
                "role": "Chief Executive Officer",
                "appointment_date": "2010-09-01"
            },
            {
                "name": "John Collison",
                "role": "President",
                "appointment_date": "2010-09-01"
            }
        ],
        "financial_info": {
            "turnover": 12000000000,
            "profit": 2000000000,
            "employees": 8000
        }
    },
    {
        "company_name": "Palantir Technologies UK Ltd",
        "company_number": "88990011",
        "status": "Active",
        "incorporation_date": "2003-05-01",
        "company_type": "Public Limited Company",
        "registered_address": "1200 17th Street, Denver, CO 80202, United States",
        "business_activity": "Data Analytics and Software for Government and Enterprise",
        "directors": [
            {
                "name": "Alex Karp",
                "role": "Chief Executive Officer",
                "appointment_date": "2003-05-01"
            },
            {
                "name": "David Glazer",
                "role": "Chief Financial Officer",
                "appointment_date": "2020-01-01"
            }
        ],
        "financial_info": {
            "turnover": 1900000000,
            "profit": -373000000,
            "employees": 3000
        }
    },
    {
        "company_name": "Snowflake UK Ltd",
        "company_number": "99001122",
        "status": "Active",
        "incorporation_date": "2012-07-01",
        "company_type": "Public Limited Company",
        "registered_address": "106 East Babcock Street, Bozeman, MT 59715, United States",
        "business_activity": "Cloud Data Platform and Analytics",
        "directors": [
            {
                "name": "Frank Slootman",
                "role": "Chief Executive Officer",
                "appointment_date": "2019-05-01"
            },
            {
                "name": "Mike Scarpelli",
                "role": "Chief Financial Officer",
                "appointment_date": "2019-05-01"
            }
        ],
        "financial_info": {
            "turnover": 1900000000,
            "profit": -680000000,
            "employees": 6000
        }
    },
    {
        "company_name": "Apple Technology Solutions UK",
        "company_number": "11111111",
        "status": "Active",
        "incorporation_date": "2015-01-15",
        "company_type": "Private Limited Company",
        "registered_address": "2 Apple Park Way, Cupertino, CA 95014, United States",
        "business_activity": "Technology Consulting and Solutions",
        "directors": [
            {
                "name": "John Smith",
                "role": "Managing Director",
                "appointment_date": "2015-01-15"
            }
        ],
        "financial_info": {
            "turnover": 50000000,
            "profit": 10000000,
            "employees": 500
        }
    },
    {
        "company_name": "Apple Retail UK Ltd",
        "company_number": "22222222",
        "status": "Active",
        "incorporation_date": "2012-03-20",
        "company_type": "Private Limited Company",
        "registered_address": "3 Apple Park Way, Cupertino, CA 95014, United States",
        "business_activity": "Retail and Consumer Electronics",
        "directors": [
            {
                "name": "Sarah Johnson",
                "role": "Retail Director",
                "appointment_date": "2012-03-20"
            }
        ],
        "financial_info": {
            "turnover": 200000000,
            "profit": 40000000,
            "employees": 2000
        }
    },
    {
        "company_name": "Apple Software Development UK",
        "company_number": "33333333",
        "status": "Active",
        "incorporation_date": "2018-06-10",
        "company_type": "Private Limited Company",
        "registered_address": "4 Apple Park Way, Cupertino, CA 95014, United States",
        "business_activity": "Software Development and Engineering",
        "directors": [
            {
                "name": "Michael Brown",
                "role": "Technical Director",
                "appointment_date": "2018-06-10"
            }
        ],
        "financial_info": {
            "turnover": 75000000,
            "profit": 15000000,
            "employees": 800
        }
    },
    {
        "company_name": "Apple Cloud Services UK",
        "company_number": "44444444",
        "status": "Active",
        "incorporation_date": "2019-09-05",
        "company_type": "Private Limited Company",
        "registered_address": "5 Apple Park Way, Cupertino, CA 95014, United States",
        "business_activity": "Cloud Computing and Infrastructure",
        "directors": [
            {
                "name": "Emily Davis",
                "role": "Cloud Services Director",
                "appointment_date": "2019-09-05"
            }
        ],
        "financial_info": {
            "turnover": 120000000,
            "profit": 25000000,
            "employees": 1200
        }
    },
    {
        "company_name": "Apple Research UK Ltd",
        "company_number": "55555555",
        "status": "Active",
        "incorporation_date": "2020-02-14",
        "company_type": "Private Limited Company",
        "registered_address": "6 Apple Park Way, Cupertino, CA 95014, United States",
        "business_activity": "Research and Development",
        "directors": [
            {
                "name": "Dr. Robert Wilson",
                "role": "Research Director",
                "appointment_date": "2020-02-14"
            }
        ],
        "financial_info": {
            "turnover": 30000000,
            "profit": 5000000,
            "employees": 300
        }
    }
]

def seed_database():
    """Seed the database with sample company data"""
    print("Starting to seed the database...")
    
    # Clear existing data
    companies_collection.delete_many({})
    print("Cleared existing data.")
    
    # Insert sample companies
    result = companies_collection.insert_many(sample_companies)
    print(f"Inserted {len(result.inserted_ids)} companies.")
    
    # Create indexes for better search performance
    companies_collection.create_index("company_name")
    companies_collection.create_index("company_number")
    companies_collection.create_index("registered_address")
    companies_collection.create_index("business_activity")
    companies_collection.create_index([("company_name", "text"), ("business_activity", "text")])
    print("Created search indexes.")
    
    print("Database seeding completed successfully!")
    print(f"Total companies in database: {companies_collection.count_documents({})}")

if __name__ == "__main__":
    seed_database()
