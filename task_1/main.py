from datetime import datetime

users = [
    {"name": "Albert Einstein", "birthday": datetime(1879, 3, 14)},
    {"name": "Beyoncé", "birthday": datetime(1981, 9, 4)},
    {"name": "Abraham Lincoln", "birthday": datetime(1809, 2, 12)},
    {"name": "Elvis Presley", "birthday": datetime(1935, 1, 8)},
    {"name": "Nelson Mandela", "birthday": datetime(1918, 7, 18)},
    {"name": "Marilyn Monroe", "birthday": datetime(1926, 6, 1)},
    {"name": "Monday Gates", "birthday": datetime(1955, 10, 30)},
    {"name": "Tuesday Gates", "birthday": datetime(1955, 10, 31)},
 #  {"name": "Wednesday Gates", "birthday": datetime(1955, 11, 1)},
    {"name": "Thursday Gates", "birthday": datetime(1955, 10, 26)},
    {"name": "Friday Gates", "birthday": datetime(1955, 10, 27)},
    {"name": "Saturday Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Sunday Gates", "birthday": datetime(1955, 10, 29)},
    {"name": "Trouble Gates", "birthday": datetime(1955, 11, 2)}
]

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthday_dict = {"Monday" : [], "Tuesday" : [], "Wednesday" : [], "Thursday" : [], "Friday" : []}
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if today.weekday()+delta_days <= 6:
                to_birthday = (today.weekday()+delta_days)
            else:
                to_birthday = ((today.weekday()+delta_days))-7
            if to_birthday >= 5 or to_birthday == 0:
                birthday_dict["Monday"].append(name)
            elif to_birthday == 1:
                birthday_dict["Tuesday"].append(name)
            elif to_birthday == 2:
                birthday_dict["Wednesday"].append(name)
            elif to_birthday == 3:
                birthday_dict["Thursday"].append(name)
            elif to_birthday == 4:
                birthday_dict["Friday"].append(name)
    i = 0
    for day, name in birthday_dict.items():
        if len(name) > 0:
            print(f"{day}: {str(name).replace("[", "").replace("]", "").replace("'", "")}")
            i += 1
        else:
            i += 1
            continue

get_birthdays_per_week(users)