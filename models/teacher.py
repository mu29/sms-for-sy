from app import db

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    subject = db.Column(db.String())
    age = db.Column(db.String())
    school = db.Column(db.String())
    phone = db.Column(db.String())
    reject = db.Column(db.Boolean())

    def __init__(self, name, subject, age, school, phone, reject):
        self.name = name
        self.phone = phone
        self.university = university
        self.gender = gender

    def __repr__(self):
        return '<id {}>'.format(self.id)
