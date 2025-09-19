data = { 
    'komalh': {
        'first_name': 'Komal', 
        'last_name': 'Karanakota', 
        'age': 19, 
        'city': 'Pune' 
    },
    'ankitakr': { 
        'first_name': 'Ankitha', 
        'last_name': 'KR', 
        'age': 17,  
        'city': 'bangalore' 
    },
}

for username, user_info in data.items():
    name = f"{user_info['first_name']} {user_info['last_name']}"
    print(f"Name: {name}")
    print(f"Age: {user_info['age']}")
    print(f"City: {user_info['city']}")
