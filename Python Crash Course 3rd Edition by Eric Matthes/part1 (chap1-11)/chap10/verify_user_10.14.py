from pathlib import Path
import json

def get_stored_username(path):
    """get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username 
    else:
        return None
    

def get_new_username(path):
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username 


def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    verification = input("Just to verify you are the correct user, enter your username: ")

    if username == verification:
        print(f"welcome back {username}")
    else:
        username = get_new_username()
        print(f"we will remember you when you come back {username}")


greet_user()