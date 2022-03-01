import random

def create_phone_list(count, type_separator):
	path = r'C:\Stepan\teamwork\phonebook\generation_data_2.txt'
	with open(path, 'w', encoding='utf-8') as data:
		for i in range(count):
			data_value = ''
			data_value += create_surname() + type_separator
			data_value += create_name() + type_separator
			data_value += create_phone() + type_separator
			data_value += create_description()
			data.write(data_value + '\n')
			if type_separator == '\n':
				data.write('\n')

def create_name():
	path = r'C:\Stepan\teamwork\phonebook\generation\name.txt'
	with open(path, 'r', encoding='utf-8') as data:
		lines = data.readlines()
		index = random.randint(0, len(lines))
		return lines[index].strip()

def create_surname():
	path = r'C:\Stepan\teamwork\phonebook\generation\surname.txt'
	with open(path, 'r', encoding='utf-8') as data:
		lines = data.readlines()
		index = random.randint(0, len(lines))
		return lines[index].strip()

def create_phone():
	tel = '+7'
	for j in range(2):
		tel += '-'
		for i in range(3):
			tel += str(random.randint(0, 9))
	for j in range(2):
		tel += '-'
		for i in range(2):
			tel += str(random.randint(0, 9))
	return tel

def create_description():
	count_world = random.randint(1, 4)
	path = r'C:\Stepan\teamwork\phonebook\generation\text_generation.txt'
	description = ''
	with open(path, 'r', encoding='utf-8') as data:
		lines = data.readlines()
		for i in range(count_world):
			index = random.randrange(len(lines))
			description += lines[index].strip()
			description += ' '
	return description
