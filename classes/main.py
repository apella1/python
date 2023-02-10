import datetime


class User:
    '''Classes are used to create objects
        Features: methods, initialization, help text
        The init method is like a constructor in js
        Grouping related data - fields
        Groupint related functions - methods
    '''

    def __init__(self, first_name, last_name, age, birthday):
        # self is a reference to the new object being created
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday

    def work(self):
        '''Returns the the age of the defined user'''
        print(f'{self.first_name} is {self.age} years old')

    def compute_age(self):
        '''Calculates the age of user using birthday'''
        today = datetime.date(2023, 11, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


# doctor is an isinstance of the class User

doctor = User("Howard", "Holowitz", 33, 19991112)
first_name = "Peter"
last_name = "Dill"

print(doctor.compute_age())
print(doctor.first_name)
print(doctor.work())
print(first_name, last_name)
# displays the docstring included as the first line after defining a class
help(User)

