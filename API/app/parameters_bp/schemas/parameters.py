from marshmallow import Schema, fields, validates, ValidationError


class CreateParametersSchema(Schema):
    """
    Schema class used for describing and validating parameters data
    before insertion into DB
    """
    param1 = fields.String(required=True)


    @validates('parameters')
    def validate_parameters(self, param1):
  
        if param1 == None:
            raise ValidationError(
                "Parameters is None")
