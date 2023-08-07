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

    for user in users:
        birthday = user['birthday']
        if start_of_week <= birthday <= end_of_week:
            day_index = birthday.weekday()
            if day_index > 4:
                day_index = 0
            day_name = days_of_week[day_index]
            print(f"{day_name}: {user['name']}")

test_users = [
    {'name': 'Bill', 'birthday': datetime(2023, 8, 8)},
    {'name': 'Tom', 'birthday': datetime(2023, 8, 8)},
    {'name': 'Jill', 'birthday': datetime(2023, 8, 9)},
    {'name': 'Kim', 'birthday': datetime(2023, 8, 10)},
    {'name': 'Jan', 'birthday': datetime(2023, 8, 12)},
    {'name': 'Saul', 'birthday': datetime(2023, 8, 13)}
]

get_birthdays_per_week(test_users)