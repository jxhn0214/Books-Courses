from pathlib import Path
import json

def store_information(path, dict):
    value = input("What is your name? ")
    dict['Name'] = value
    contents = json.dumps(dict)
    path.write_text(contents)
    

def retrieve_information(path):
    """Get stored information if any"""
    if path.exists():
        contents = path.read_text()
        information = json.loads(contents)
        return information
    else:
        None


def main():
    information = {}
    path = Path('stored_information.json')
    if path.exists():
        print(f"Youre information has already been stored: it says {retrieve_information(path)}")
    else:
        store_information(path, information)
        print("your entered information will now be stored")

main()