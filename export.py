
def mr_exporter():
    with open('C:\Pratice_code\phonebook\generation_data.txt', 'r', encoding='utf-8') as data:
        with open('C:\Pratice_code\phonebook\exp_folder\exp.txt', 'w', encoding='utf-8') as file:
            for line in data:
                file.write(line)
        data.close()

mr_exporter()
