
from random import choice, randint, uniform

from app import app
from models import db, Vendor, Sweet, VendorSweet

with app.app_context():
    Vendor.query.delete()
    Sweet.query.delete()
    VendorSweet.query.delete()

    real_vendors = [
    "Sweet Delights Bakery",
    "Heavenly Treats Confections",
    "Sugar Rush Sweets",
    "Divine Desserts Emporium",
    "Blissful Bites Patisserie",
    "Confectionery Creations",
    "Gourmet Sweet Haven",
    "Delectable Delights Dessert Shop",
    "Sugary Wonders Confections",
    "Delish Sweets & Treats Co."
]
    
    sweet_brands = [
    "JuicyFruit Delights",
    "CandyCraze Confections",
    "LusciousLollipops",
    "DivineChocoJoy",
    "FruityBliss Sweets",
    "GourmetGummy Galore",
    "VelvetTruffle Treats",
    "SugarSpark Confections",
    "CaramelHeaven Sweets",
    "ChocoMingle Delicacies",
    "HoneyHarmony Sweets",
    "MintyMarvel Confections",
    "CrunchyCrisps Delights",
    "ZestyZingy Sweets",
    "BerryBurst Confections",
    "SweetyCitrus Delights",
    "ToffeeTwirl Sweets",
    "NougatNest Confections",
    "MarshmallowMagic Sweets",
    "CitrusSqueeze Delights"
]

   

    vendors = []
    for n in range(10):
        owner = Vendor(name=choice(real_vendors))
        vendors.append(owner)

    db.session.add_all(vendors)

    sweets = []
    for n in range(20):
        sweet = Sweet(name=choice(sweet_brands))
        sweets.append(sweet)

    db.session.add_all(sweets)
    db.session.commit()

    for rp in range(20):
        vnd_sweet = VendorSweet(
            price =randint(100, 300),
            vendor_id = randint(1, 10),
            sweet_id = randint(1, 20)
        )

        db.session.add(vnd_sweet)

    db.session.commit()


 

