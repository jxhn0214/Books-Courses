from pathlib import Path

dog_path = Path("dog.txt")
cat_path = Path("cats.txt")

try:
    dog_content = dog_path.read_text()
    cat_content = cat_path.read_text()

    print(dog_content)
    print(cat_content)
except FileNotFoundError:
    pass

