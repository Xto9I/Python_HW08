from datetime import datetime, date, timedelta


# ВИБАЧТЕ ЩО ТАК ПІЗНО, БУЛИ ВЕЛИКІ ПРОБЛЕМИ ЗІ СВІТЛОМ ТА ПРОВАЙДЕРОМ (ІНТЕРНЕТ)


users = [{'name': 'Bohdan', 'birthday': date(year=1989, month=3, day=14)},
         {'name': 'Andriy', 'birthday': date(year=1998, month=11, day=10)},
         {'name': 'Oleksi', 'birthday': date(year=1995, month=11, day=7)},
         {'name': 'Yana', 'birthday': date(year=1998, month=11, day=15)},
         {'name': 'Dana', 'birthday': date(year=1991, month=10, day=12)},
         {'name': 'Tom', 'birthday': date(year=2001, month=12, day=11)},
         {'name': 'Emmy', 'birthday': date(year=1991, month=11, day=12)},
         {'name': 'Cory', 'birthday': date(year=1988, month=11, day=5)},
         {'name': 'Henry', 'birthday': date(year=1991, month=9, day=10)},
         {'name': 'Anna', 'birthday': date(year=2001, month=11, day=11)}
         ]

day_list = {'Monday': [],
            'Tuesday': [],         
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],         
            'Saturday': [],
            'Sunday': []
         }

def list_birthday(users : list):

    seventh_day = datetime.now()
    interval = seventh_day + timedelta(weeks=1)
    
    for user in  users:
        year_HB = user.get('birthday') 
        list1 = str(year_HB).split('-')
        this_year = datetime.now().year
        dbtd = datetime(year=int(this_year), month=int(list1[1]), day=int(list1[2]))

        if ( seventh_day < dbtd <= interval ):
            weekday_string = dbtd.strftime("%A")
            if weekday_string in ['Saturday', 'Sunday']:
                weekday_string = 'Monday'
            day_list.get(weekday_string).append(user.get('name'))
            
    return day_list


def note(days : dict):  
    with open('output.txt', 'w') as f:
        for key, value in days.items():
            if value:
                d = ', '.join(value)
                f.write(f'{key}: {d}\n')     

if __name__ == '__main__':
    list_birthday(users)
    note(day_list)