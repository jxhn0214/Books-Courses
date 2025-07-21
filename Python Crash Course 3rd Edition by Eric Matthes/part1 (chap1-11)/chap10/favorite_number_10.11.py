from pathlib import Path
import json

def store_favorite_number(path):
    favorite_number = input("what's your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number

def get_stored_fav_number(path):
    if path.exists():
        contents = path.read_text()
        stored_fav_number = json.loads(contents)
        print(f"Welcome back, your favorite number is {stored_fav_number}")
    else:
        return None

def main():
    path = Path("favorite_number.json")
    fav_number = get_stored_fav_number(path)
    if fav_number:
        print(f"Welcome back, your favorite number was {fav_number}")
    else:
       fav_number = store_favorite_number(path)
       print(f"we will remember your favorite number is {fav_number} from now on")
    
main()