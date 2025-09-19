
favourite_languages = {
    'komal': 'Python', 
    'pooja' : 'C',
    'sayali' : 'Java' ,
    'vaishnavi' : 'HTML' ,
    'anjali' : 'C++', 
}

print(favourite_languages)

print(f"Komal's favourite language is {favourite_languages['komal']}")
print(f"Pooja's favourite language is {favourite_languages['pooja']}")
print(f"Sayali's favourite language is {favourite_languages['sayali']}")
print(f"Vaishnavi's favourite language is {favourite_languages['vaishnavi']}")
print(f"Anjali's favourite language is {favourite_languages['anjali']}")

for name, language in favourite_languages.items() :
    print(f"\n{name.title()}'s favourite language is {language.title()}")

for name in favourite_languages.keys():
    print(name.title())

friends = [ 'komal', 'pooja']
print("\nFriends: ", friends)

for name in favourite_languages.keys():
    print(f"\nHi, {name.title()}")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"{name.title()}, I see you love {language}")

for name in sorted(favourite_languages.keys()) :
    print(f"{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned: ")
for language in favourite_languages.values():
    print(language.title())

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are: ")
    for language in languages :
        print(f"\t{language.title()}")