import json


def get_stored_name():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_name()
    while True:
        verification = input('Is your user name "' + username + '"? (y/n) ')
        if verification == 'y':
            print('Welcome back, ' + username + '!')
            break
        elif verification == 'n':
            username = get_new_username()
            print('We will remember you when you come back, ' + username + '!')
            break


greet_user()
