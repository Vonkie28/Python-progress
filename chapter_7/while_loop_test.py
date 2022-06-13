#creating a prompt with a while loop
prompt = "\nTell me something and i will repeat it back."
prompt += "Enter 'quit' to end the program."

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)