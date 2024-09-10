from app.entities.phone_entity import PhoneEntity
from db import db


class PhoneService:
    @staticmethod
    def get():
        return PhoneEntity.query.filter_by(status=1).all()

    @staticmethod
    def create(data):
        phone = PhoneEntity(**data)
        db.session.add(phone)
        db.session.commit()
        return phone

    @staticmethod
    def update(data):
        phone = PhoneEntity.query.filter_by(id=data["id"], status=1)
        phone.modelname = data["modelname"]
        phone.brand = data["brand"]
        phone.price = data["price"]
        phone.about = data["about"]
        phone.is_smart_phone = data["is_smart_phone"]
        db.session.commit()
        return phone

    @staticmethod
    def update_partially(req, id):
        phone = PhoneEntity.query.filter_by(id=id, status=1)
        phone.modelname = req["modelname"]
        phone.brand = req["brand"]
        phone.price = req["price"]
        phone.about = req["about"]
        phone.is_smart_phone = req["is_smart_phone"]
        db.session.commit()
        return phone

    @staticmethod
    def delete(id):
        phone = PhoneEntity.query.filter_by(id=id, status=1).first()
        if phone is not None:
            phone.status = 0
            db.session.commit()
            return {"response code": 200, "message": "successfully deleted Phone"}
        return {"response code": 204, "message": "no Phone found"}

    @staticmethod
    def search(qry):
        qry = qry.get("qry")
        phones = PhoneEntity.query.filter(
            (
                (PhoneEntity.brand.like("%" + qry + "%"))
                | (PhoneEntity.modelname.like("%" + qry + "%"))
                | (PhoneEntity.about.like("%" + qry + "%"))
            )
            & (PhoneEntity.status == 1)
        ).all()
        return phones
