favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")
print("\n")

list=['jen','wasif','sarah','moosa','edward','rana','phil','shakoor']

for name in list:
    if(name in favorite_languages):
        print("thankyou "+ name +" for taking our poll")
    else:
        print("kindly take our poll "+name)