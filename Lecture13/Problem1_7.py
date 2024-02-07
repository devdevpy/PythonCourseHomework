class Student:
    num_student = 0

    def __init__(self,
                 names="",
                 course="",
                 major="",
                 university=None,
                 email="", telephone_number=None):
        self._names = names
        self._course = course
        self._major = major
        self._university = university
        self._email = email
        self._telephone_number = telephone_number
        Student.num_student += 1

    def info_student(self):
        print(self._names,
              self._course,
              self._major,
              self._university,
              self._email,
              self._telephone_number)

    @property
    def names(self):
        return self._names

    @property
    def course(self):
        return self._course

    @property
    def major(self):
        return self._major

    @property
    def university(self):
        return self._university

    @property
    def email(self):
        return self._email

    @property
    def telephone_number(self):
        return self._telephone_number


john = Student("John", "test", "test", "test", "test", "test")
print(john.names)
print(john.course)
print(john.major)
print(john.university)
print(john.email)
print(john.telephone_number)
