# ввести данные
import UI

def import_file():
	path = UI.get_adress()
	with open(path, 'r') as data:
		check_format(data)

def check_format(data):
	lines = data.readlines()
	for line in lines:
		for c in line:
			if c == '\n':
				break
			if c == ';':
				return import_csv(lines)
	return import_txt(lines)

def import_txt(lines):
	data_import = ''
	with open('phonebook.csv', 'a', encoding='ANSI') as data_file:
		for line in lines:
			if line.strip() != '':
				data_import += ';' + line.strip()
			else:
				data_import = data_import.replace(';', '', 1)
				data_import += '\n'
				data_file.write(data_import)
				data_import = ''

def import_csv(lines):
	with open('phonebook.csv', 'a', encoding='ANSI') as data_file:
		for line in lines:
			data_file.write(line)