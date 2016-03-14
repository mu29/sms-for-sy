from app import db

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    subject = db.Column(db.String())
    age = db.Column(db.String())
    school = db.Column(db.String())
    phone = db.Column(db.String())
    contact = db.Column(db.Integer)

    def __init__(self, name, subject, age, school, phone, contact):
        self.name = name
        self.subject = subject
        self.age = age
        self.school = school
        self.phone = phone
        self.contact = contact

    def __repr__(self):
        return "<Teacher(name='%s', phone='%s')>" % (self.name, self.phone)
