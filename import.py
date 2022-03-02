



def import_inline():
    with open('test.txt', 'r', encoding='utf-8') as data:
            with open('C:\Pratice_code\phonebook\generation_data copy.txt', 'a', encoding='utf-8') as file:
                file.write('\n')
                for line in data:
                    file.write(line)
            data.close()

import_inline()