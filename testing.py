from datetime import date
 
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age



dob = "1987-06-03"

year = int (dob.split("-")[0])
month = int (dob.split("-")[1])
day = int (dob.split("-")[-1])


print(age(date(year, month, day)))