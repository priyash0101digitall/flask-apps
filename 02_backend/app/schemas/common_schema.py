from marshmallow import fields, Schema

class ResponseSchema(Schema):
    response_code=fields.Integer(dump_only=True)
    message=fields.String(dump_only=True)

