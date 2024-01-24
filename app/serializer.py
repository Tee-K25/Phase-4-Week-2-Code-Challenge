def serialize_vendor(vendor):
    return {
        'id': vendor.id,
        'name': vendor.name,
        'sweets': [serialize_vendor_sweet(sweet) for sweet in vendor.sweets]
    }

def serialize_sweet(sweet):
    return {
        'id': sweet.id,
        'name': sweet.name,
        'vendors': [vendor.id for vendor in sweet.vendors]
    }

def serialize_vendor_sweet(vendor_sweet):
    return {
        'id': vendor_sweet.id,
        'sweet_id': vendor_sweet.sweet_id,
        'vendor_id': vendor_sweet.vendor_id,
        'price': vendor_sweet.price
    }
