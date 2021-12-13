my_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = min(row)
    minimum = min(row)

print(maximum + minimum)

users = [
    {
        "user_name": "asd",
        "grades": {
            "2011": 5,
            "2012": 4
        },
        "cars": [
            'bmw',
            'subaru'
        ]
    },
    {
        "user_name": "ivan",
        "cars": [
            'mercedes',
            'volvo'
        ]
    }
]

for user in users:
    print(user['user_name'])
    for car in user['cars']:
        print(car)
