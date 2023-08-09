from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    days_of_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    current_date = datetime.now()
    current_weekday = current_date.weekday()
    start_of_week = current_date - timedelta(days=current_weekday)
    end_of_week = start_of_week + timedelta(days=6)

    birthday_dict = {}

    for user in users:
        birthday = user['birthday']
        birthday = birthday.replace(year=current_date.year)

        if start_of_week <= birthday <= end_of_week:
            day_index = birthday.weekday()
            day_name = days_of_week[day_index]
            if day_index > 4:
                day_index = 0

            if birthday.date() not in birthday_dict:
                birthday_dict[birthday.date()] = [user['name']]
            else:
                birthday_dict[birthday.date()].append(user['name'])

            print(f"{day_name}: {user['name']}")

    print(birthday_dict)

test_users = [
    {'name': 'Bill', 'birthday': datetime(1998, 8, 8)},
    {'name': 'Tom', 'birthday': datetime(1998, 8, 7)},
    {'name': 'Jill', 'birthday': datetime(1997, 8, 9)},
    {'name': 'Kim', 'birthday': datetime(1999, 8, 10)},
    {'name': 'Jan', 'birthday': datetime(1996, 8, 12)},
    {'name': 'Saul', 'birthday': datetime(1998, 8, 13)}
]

get_birthdays_per_week(test_users)