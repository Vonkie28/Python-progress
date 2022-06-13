#Making a glossary
python_glossary = {
	'print' : 'prints the action in a sentence',
	'string' : 'a string is an sentence',
	'loop' : 'cycles throught the whole object you want to cycle',
	'if statement' : 'when certain conditions are met a action is executed',
	'list' : 'this is a collection of elements in the form of a list',
	'elements' : 'elements are items',
	'key' : 'this are items in a dictionary',
	'value' : 'the meaning of a key',
	'slicing' : 'dividing a list',
	'sort' : 'sorting a list permamently'
}


#Looping through the glossary
for key, value in python_glossary.items():
	print(f"\n{key}:")
	print({value})