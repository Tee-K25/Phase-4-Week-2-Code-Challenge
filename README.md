# Sweet Vendors API
This is a Flask RESTful API for managing sweet vendors, sweets, and relationships between them.

# Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

# Prerequisites
Ensure you have the following installed:

Python 3.10 or later.
Visual Studio Code or an IDE of your choice.
Postman or Insomnia for testing.

# Installing
### Installing
1. Clone the repository:

```bash
git clone https://github.com/jeffetale/Phase-4-Week-1-Code-Challenge.git
```
* Run a virtual environment:
```bash
pipenv shell
```
* Install the dependencies:
```bash
pip install -r requirements.txt
```
* Navigate to the project code:
```bash
cd Phase-4-Week-2-Code-Challenge
```
* Run the application:
```bash
python python.py
```

Click on the link created in the terminal, e.g., http://127.0.0.1:5555/

### Running the Tests
Run the automated tests for this system using Postman or Insomnia.

### API Endpoints
* GET /vendors: Returns a list of all vendors.
* GET /vendors/<int:id>: Returns a single vendor by ID.
* GET /sweets: Returns a list of all sweets.
* GET /sweets/<int:id>: Returns a single sweet by ID.
* GET /vendor_sweets: Returns a list of all vendor-sweet relationships.
* POST /vendor_sweets: Adds a new vendor and sweet relationship to the list.
* DELETE /vendor_sweets/<int:id>: Deletes a single vendor-sweet relationship by ID.

## Web Browser Interaction
You can view a JSON response of all the vendors, sweets, and the vendor-sweet relationships on the web browser by visiting http://127.0.0.1:5555/.

http://127.0.0.1:5555/vendors - Get all the vendors. Add an ID at the end of the URL to get a single vendor.
http://127.0.0.1:5555/sweets - Get all the sweets. Add an ID at the end of the URL to get a single sweet.
http://127.0.0.1:5555/vendor_sweets - Get all the vendor-sweets relationships.

## Built With
- Flask - The web framework used.
- Flask_SQLAlchemy - SQL Toolkit and ORM.
## Authors
Tony Kiplagat - tony.kiplagat@moringaschool.com