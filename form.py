import pandas as pd
from openpyxl import load_workbook
from espfunc import *
wb = load_workbook('list_form.xlsx')
ws = wb.worksheets[0]


#MAIN MENU
while True:
    title('MAIN MENU')
    options('See list of People,Add new People,Exit')
    opti = readInt('Choose your Option: ')


#READ THE LIST
    if opti == 1:
        read = pd.read_excel('list_form.xlsx', usecols='B, C')
        list_name = read[0].tolist()
        list_age = read[1].tolist()
        title('List of People')
        for i, v in enumerate(list_name):
            print(f'{list_name[i]:<36} {list_age[i]:<3} anos')



#NEW DATA ENTRY
    elif opti == 2:
        data = []
        while True:
            name = input('Name: ').strip().title()
            if name.isnumeric():
                print(f'\'{name}\' is not a name, please try again.')
                continue
            else:
                break
        age = readInt('Age: ')
        data.append(name)
        data.append(age)
        print(f'{name} was added to the DataBase')
        ws[pers()] = data[0]
        ws[birt()] = data[1]
        wb.save('list_form.xlsx')
        data.clear()
    elif opti == 3:
        break
    else:
        line('+', 40)
        print(f'\'{opti}\' is not an option please chose again')
        line('+', 40)
