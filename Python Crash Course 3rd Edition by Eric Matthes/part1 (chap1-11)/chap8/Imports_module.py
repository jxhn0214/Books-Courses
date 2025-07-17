def send_messages(messages, sent_messages):
    while messages:
        pending_message = messages.pop()
        sent_messages.append(pending_message)
    return sent_messages