def show_messages(messages):
    print("Pending Messages: ", end="")

    for message in messages: 
        print(message, end=", ")

def send_messages(messages, sent_messages):
    while messages:
        pending_message = messages.pop()
        sent_messages.append(pending_message)
    return sent_messages
messages = ['hi', 'hello', 'im good', 'what time is it?', "what's up?"]
sent_messages = []

sent = send_messages(messages[:], sent_messages)

print(f"Messages sent: {sent}")
print(f"Messages pending: {messages}")
