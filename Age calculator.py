# Age_Calculator
# Instagram @py_coder_wall
# Like | Comment | Share

from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

print(age(date(2000, 1, 1)))
