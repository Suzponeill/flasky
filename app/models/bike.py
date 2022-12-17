from app import db


class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    size = db.Column(db.Integer)
    type = db.Column(db.String)
    cyclist_id = db.Column(db.Integer, db.ForeignKey('cyclist.id'))
    cyclist = db.relationship("Cyclist", back_populates="bikes")

    def to_dict(self):
        # bikes_list = [bike.to_dict() for bike in self.bikes]
        bike_dict = {"id": self.id,
                     "name": self.name,
                     "price": self.price,
                     "size": self.size,
                     "type": self.type,
                     #  "bikes" : bikes_list
                     }

        return bike_dict
