users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location':'princeton',
    },

    'mcurie' : {
        'first': 'marie',
        'last': 'curie',
        'location':'paris',
    },
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    print(f"\tFull name: {userinfo['first'].title()} {userinfo['last'].title()}")
    print(f"\tLocation: {userinfo['location'].title()}")

user1 = {
    'username' : 'kharsh',
    'first': 'komal',
    'last' : 'harshita',
}

for key, value in user1.items() :
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")