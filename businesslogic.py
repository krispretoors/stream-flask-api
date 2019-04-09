from models import Student, TestResult

class DatabaseCalls:
    def __init__(self, payload):
        self.payload = payload

    def persist_data_to_db(self, payload):
        try:
            newd = json.loads(self.payload)
            student_list = newd['students']
    
            for student in student_list:
                test_list = student['tests']
                student = Student(
                    name = student['firstName'],
                    surname = student['lastName']
                )
                db.session.add(student)

                for key, value in test_list.items():
                    student_test = TestResult(
                        test = key,
                        result = value,
                        student_id = student.id
                    )
                    db.session.add(student_test)
                    db.session.commit()
        except Exception as e:
            return(str(e))
