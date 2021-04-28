# We will import the necessary libraries
from getpass import getuser
from datetime import datetime
import json
import secrets

result = 0

hour = datetime.now().hour  # Will give us the current hour (0-23)
print(
    f"Good {'morning' if hour < 12 else ('afternoon' if hour < 16 else 'evening')}, {getuser()}!")

# For example, if the time of day is morning, and the username is 'admin', it will say 'Good morning, admin!'


# Questions

def age(result):
    q1 = input("Enter your age: ")
    try:
        q1 = int(q1)
    except:
        print("Age must be a number!")
        age()
    else:
        if q1 > 35:
            result += 1

    return result


result = age(result)

q2 = input("Do you go outside often? (y/n): ")
if q2 == "y":
    result += 1

q3 = input("Do you wear a mask when going out, even for short durations? (y/n): ")
if q3 == "n":
    result += 1

q4 = input("Do you wash your hands often? (y/n): ")
if q4 == "n":
    result += 1

q5 = input("Have you been in contact with someone who has COVID-19? (y/n): ")
if q5 == "y":
    result += 1

# Printing results

if result == 0:
    print("Congrats! You have almost zero chances of catching COVID-19.")
elif result == 1:
    print("You have very little chances of catching COVID-19.")
elif result in [2, 3]:
    print("You have moderate chances of catching COVID-19.")
elif result == 4:
    print("You have quite high chances of catching COVID-19.")
else:
    print("Stay safe! You have an extremely high risk of catching COVID-19.")

# Storing result

with open("database.json") as f:
    db = json.load(f)

s = secrets.token_hex(3)
db[s] = result

with open("database.json", "w") as f:
    json.dump(db, f)
