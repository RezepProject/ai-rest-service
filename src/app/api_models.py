from flask_restx import fields

from .extensions import api 

request_model = api.model("Request", {
    "uuid": fields.String,
    "content": fields.String,
})

response_model = api.model("Response", {
    "uuid": fields.String,
    "content": fields.String,
})