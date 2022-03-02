def export_file(info_format):
		if info_format == 'csv':
			with open('phonebook.csv', 'r') as data:
				with open('export.csv', 'w') as data_export:
					data_export.write(data.read())
		elif info_format == 'txt':
			with open('phonebook.csv', 'r') as data:
				with open('export.txt', 'w') as data_export:
					lines = data.readlines()
					for line in lines:
						elements = line.split(';')
						for el in elements:
							data_export.write(el + '\n')