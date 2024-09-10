from marshmallow import Schema, fields

# phone schema
class PhoneSchema(Schema):
    id = fields.Integer(dump_only=True)
    modelname = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Float(required=True)
    about = fields.String(required=False)
    is_smart_phone = fields.Boolean(default=True)
    status=fields.Integer(required=False,default=1, missing=1)

# phone schema for update
class PhoneUpdateSchema(Schema):
    id = fields.Integer(required=True)
    modelname = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Float(required=True)
    about = fields.String(required=False)
    is_smart_phone = fields.Boolean(default=True)

# phone schema for single data/field
class PhoneOneFiendUpdateSchema(Schema):
    modelname = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Float(required=True)
    about = fields.String(required=False)
    is_smart_phone = fields.Boolean(default=True)

# phone schema find-data
class PhoneSearchSchema(Schema):
    qry = fields.String(required=True)