from marshmallow import Schema, fields, validates, ValidationError


class CreateMeasurementSchema(Schema):
    """
    Schema class used for describing and validating measurement data
    before insertion into DB
    """
    front_left_weel = fields.Float(required=True)
    front_right_weel = fields.Float(required=True)
    back_left_weel = fields.Float(required=True)
    back_right_weel = fields.Float(required=True)
    servo_angle = fields.Float(required=True)

    @validates('front_left_weel')
    def validate_front_left_weel_value(self, front_left_weel):
  
        if front_left_weel == None:
            raise ValidationError(
                "Front_left_weel is None")

    @validates('front_right_weel')
    def validate_front_right_weel_value(self, front_right_weel):
  
        if front_right_weel == None:
            raise ValidationError(
                "Front_right_weel is None")

    @validates('back_right_weel')
    def validate_back_right_weel_value(self, back_right_weel):
  
        if back_right_weel == None:
            raise ValidationError(
                "Back_right_weel is None")
    
    @validates('servo_angle')
    def validate_servo_angle_value(self, servo_angle):
  
        if servo_angle == None:
            raise ValidationError(
                "Servo_angle is None")



class GetMeasurementSchema(Schema):
    """
    Schema class used for serializing data pulled from DB for our
    GET endpoint
    """
    id = fields.Int(required=True)
    front_left_weel = fields.Float(required=True)
    front_right_weel = fields.Float(required=True)
    back_left_weel = fields.Float(required=True)
    back_right_weel = fields.Float(required=True)
    servo_angle = fields.Float(required=True)
    timestamp = fields.DateTime(required=True)
