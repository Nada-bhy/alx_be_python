current_age = int(input("how old are you? "))
# print(f"you entered : {age}")

import datetime
current_year = datetime.datetime.now().year

target_year = 2050
age = current_age + (target_year - current_year)

print(f"In {target_year} you will be {age} years old.")