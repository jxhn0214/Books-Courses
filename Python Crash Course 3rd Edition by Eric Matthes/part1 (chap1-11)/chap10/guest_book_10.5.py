from pathlib import Path

print("type 'qq' to stop entering guests")
content = input("what's your name?")

while True:
   guest_name = input("what's your name?")
   if guest_name == 'qq':
      break
   content += "\n" + guest_name

path = Path('guest_book.txt')
path.write_text(content)
