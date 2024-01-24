from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


db = SQLAlchemy()

class Vendor(db.Model, SerializerMixin):
    # __tablename__ = 'vendor'

    serialize_rules = ('-sweet.vendors',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sweets = db.relationship('VendorSweet',backref='vendor')

class Sweet(db.Model, SerializerMixin):

    # __tablename__='sweet'

    serialize_rules = ('-vendor.sweets',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    vendors = db.relationship('VendorSweet',backref='sweet')
    

class VendorSweet(db.Model,SerializerMixin):

    # __tablename__ = 'vendor_sweet'


    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    vendor_id = db.Column(db.Integer,db.ForeignKey('vendor.id'))
    sweet_id = db.Column(db.Integer,db.ForeignKey('sweet.id'))

    @validates('price')
    def validate_price(self, key, price):
        if price <= 0:
            raise ValueError("Price cannot be null or a negative number")
        return price

