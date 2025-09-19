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
