#Making a list of text messages
messages = ['Hello', 'Bye', 'How are you?', 'What day is it?']
sent_messages = []

def send_message():
	"""Send the texts and moves them to send_message list"""
	print(messages)
	while messages:
		current_message = messages.pop()
		sent_messages.append(current_message)

send_message()
print(messages)
print(sent_messages)