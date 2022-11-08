from app import db

class Cyclist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String)
    bikes = db.relationship("Bike", back_populates="cyclist")



    def to_dict(self):
        cyclist__dict = {"id" : self.id,
            "name" : self.name
        }

        return cyclist__dict
    
