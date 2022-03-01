
from tabnanny import check


def get_info():
    text_vvod = 'Input action import or export: '
    info = input(text_vvod)
    return chek_input(info,('import','export'),'invalid info',text_vvod)

def chose_format():
    text_input='Input format txt or csv: '
    format = input(text_input)
    return chek_input(format,('txt','csv'),'Invalid format',text_input)

def chek_input(input_data, checking,invalid_text,for_input_text):
    while input_data not in checking:
        print(invalid_text)
        input_data = input(for_input_text)
    return input_data

def get_adress():
    return input('Enter adress: ')
    


def success():
    return print('Import/ export complete successfully')
