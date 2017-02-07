# A real world application of oop
# class and method inside demonstrate encapsulation
# Inheritance is demonstrated by medical info and contact emergency inheriting from person
# polymorphism is demonstrated by the ask question method

class Person(object):
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age


class MedicalInfo(Person):
    def __init__(self, first_name, last_name, gender, age, doctor, hospital, blood_type, condition, allergies):
        super().__init__(first_name, last_name, gender, age)
        self.doctor = doctor
        self.hospital = hospital
        self.blood_type = blood_type
        self.medical_condition = condition
        self.allergies = allergies

    def ask_question(self):
        print("Hello {0} would yoy like to see {1}".format(self.first_name, self.doctor))


class EmergencyContact(Person):
    def __init__(self, first_name, last_name, gender, age, contact_name, relationship, phone, address):
        super().__init__(first_name, last_name, gender, age)
        self.contact = contact_name
        self.relationship = relationship
        self.phone = phone
        self.address = address

    def ask_question(self):
        print("Hello {0} would you like to contact {1} on {2}".format(self.first_name, self.contact, self.phone))

a = MedicalInfo("Johan", "cruyff", "male", "72", "Dr.John", "Aga khan", "B+", "Heart disease", "none")
print(a.first_name)
print(a.doctor)
print(a.hospital)
print(a.medical_condition)
a.ask_question()

b = EmergencyContact("Wayne", "Rooney", "Male", "31", "Coleen", "wife", "+275712033", "cheshire 123 lane")
print(b.first_name)
print(b.contact)
print(b.relationship)
print(b.phone)
b.ask_question()
