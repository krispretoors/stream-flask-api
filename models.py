from app import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    surname = db.Column(db.String())
    tests = db.relationship("TestResult", backref="student_tests", lazy='dynamic')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }

class TestResult(db.Model):
    __tablename__ = 'testresults'
    
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.String())
    result = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship('Student')

    def __init__(self, test, result, student_id):
        self.test = test
        self.result = result
        self.student_id = student_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'test': self.test,
            'result': self.result,
            'student_id': self.student_id
        }