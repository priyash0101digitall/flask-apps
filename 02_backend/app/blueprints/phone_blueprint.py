from flask_smorest import Blueprint
from flask.views import MethodView

from app.services.phone_service import PhoneService
from app.schemas import (
    PhoneSchema,
    PhoneUpdateSchema,
    PhoneOneFiendUpdateSchema,
    PhoneSearchSchema,
)
from app.schemas import ResponseSchema

# initialize blueprint
phones_blp = Blueprint(
    "phones",
    "phones",
    url_prefix="/phones",
    description="Phones",
)


@phones_blp.route("/")
class PhoneBlueprint(MethodView):
    # get data
    @phones_blp.response(200, PhoneSchema(many=True))
    def get(self):
        return PhoneService.get()

    # submit data/create
    @phones_blp.response(201, PhoneSchema)
    @phones_blp.arguments(PhoneSchema)
    def post(self, new_phone_data):
        return PhoneService.create(new_phone_data)

    # update data
    @phones_blp.response(200, PhoneSchema(many=False))
    @phones_blp.arguments(PhoneUpdateSchema)
    def put(self, update_phone_data):
        return PhoneService.update(update_phone_data)


@phones_blp.route("/<int:id>")
class PhoneBlueprint(MethodView):
    # update spacific field data
    @phones_blp.response(200, PhoneSchema)
    @phones_blp.arguments(PhoneOneFiendUpdateSchema)
    def patch(self, req, id):
        return PhoneService.update_partially(req, id)

    @phones_blp.response(200, ResponseSchema)
    def delete(self, id):
        return PhoneService.delete(id)


@phones_blp.route("/search")
class PhoneBlueprintByQuery(MethodView):
    @phones_blp.arguments(PhoneSearchSchema, location="query")
    @phones_blp.response(200, PhoneSchema(many=True))
    def get(self, query_data):
        return PhoneService.search(query_data)
