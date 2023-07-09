from employeemanager import db


class Department(db.Model):
    # schema for hr model
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(25), unique=True, nullable=False)
    staff = db.relationship("Staff", backref="department", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.department_name



class Staff(db.Model):
    # Schems for programmers model
    id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(25), unique=True, nullable=False)
    staff_position = db.Column(db.String(25), unique=True, nullable=False)
    staff_skills = db.Column(db.String(40), unique=True, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    department.id = db.Column(db.Integer, db.ForeignKey("department.id", ondelete="CASCADE"), nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "{0} - Staff: {1} | Skills:{2}".format(
            self.id, self.staff_name, self.staff_skills
        )





