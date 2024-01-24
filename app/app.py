#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from serializer import serialize_sweet,serialize_vendor,serialize_vendor_sweet

from models import db, Vendor, Sweet, VendorSweet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to the sweetness industry'

@app.route('/vendors')
def vendors():
    vendors = []
    for vendor in Vendor.query.all():
        vendor_dict = {
            "id":vendor.id,
            "name":vendor.name
        }
        vendors.append(vendor_dict)

    response = make_response(jsonify(vendors),200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/vendors/<int:id>')
def vendor_by_id(id):
    vendor = Vendor.query.filter_by(id=id).first()
    if vendor == None:
        response_body = {
            "error": "Vendor not found"
            }
        response = make_response(jsonify(response_body),404)
        return response
    else:
        vendor_dict = serialize_vendor(vendor)
        response = make_response(jsonify(vendor_dict),200)
        response.headers["Content-Type"] = "application/json"
        return response

@app.route('/sweets')
def sweets():
    sweets = []
    for sweet in Sweet.query.all():
        sweet_dict = {
            "id":sweet.id,
            "name":sweet.name
        }
        sweets.append(sweet_dict)

    response = make_response(jsonify(sweets),200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/sweets/<int:id>')
def sweets_by_id(id):
    sweet = Sweet.query.filter_by(id=id).first()
    if sweet == None:
        response_body = {
            "error": "Sweet not found"
        }
        response = make_response(jsonify(response_body),404)
        return response
    else:
        sweet_dict = serialize_sweet(sweet)
        response = make_response(jsonify(sweet_dict),200)
        response.headers["Content-Type"] = "application/json"
        return response

@app.route('/vendor_sweets', methods=["GET","POST"])
def vendor_sweet():
    if request.method == "GET":
        vendor_sweets = []
        for vendor_s in VendorSweet.query.all():
            vendorS_dict = serialize_vendor_sweet(vendor_s)
            vendor_sweets.append(vendorS_dict)

        response = make_response(jsonify(vendor_sweets),200)
        response.headers["Content-Type"] = "application/json"
        return response
    elif request.method == "POST":
        data = request.get_data()
        if data:
            new_vendor_sweet = VendorSweet(
                price=data['price'],
                vendor_id=data['vendor_id'],
                sweet_id=data['sweet_id']
            )
            db.session.add(new_vendor_sweet)
            db.session.commit()

            new_dict = new_vendor_sweet.to_dict()
            response = make_response(jsonify(new_dict),200)
            response.headers["Content-Type"] = "application/json"
            return response
        else:
            response_body = {
                "errors": ["validation errors"]
            }
            response = make_response(jsonify(response_body),400)

@app.route('/vendor_sweets/<int:id>', methods=['DELETE'])
def delete_pair(id):
    pair = VendorSweet.query.filter_by(id=id).first()
    if not pair:
        response = make_response(jsonify({"error": "VendorSweet not found"}),404)
        return response
    else:
        db.delete(pair)
        db.commit()
        response =make_response(jsonify({}),200)
        return response
    

if __name__ == '__main__':
    app.run(port=5555)
