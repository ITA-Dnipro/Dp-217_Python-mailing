from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    subject = fields.String(required=True)
    text = fields.String(required=True)
    mail = fields.Email()
