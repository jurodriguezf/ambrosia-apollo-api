from marshmallow import Schema, fields, post_load, validate

from app.entities.subject_entity import SubjectEntity


class SubjectSchema(Schema):
    code = fields.String(required=True, validate=validate.Length(min=5, max=10))
    name = fields.String(required=True)

    @post_load
    def make_subject(self, data, **kwargs):
        return SubjectEntity(**data)
