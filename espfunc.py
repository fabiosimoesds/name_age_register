# Title fuction
def line(a='-', x=45):
    print(a * x)


def title(txt):
    line()
    print(txt.center(45))
    line()


def options(mylist):
    mylist = mylist.split(',')
    for ind, value in enumerate(mylist):
        print(f'{ind + 1} - {value}')
    line()


def pers():
    import pandas as pd
    import openpyxl
    df2 = pd.read_excel("list_form.xlsx", index_col=1)
    no_rows = df2.shape[0] + 2
    no_rows = str(no_rows)
    name = "B" + no_rows
    return name


def birt():
    import pandas as pd
    import openpyxl
    df2 = pd.read_excel("list_form.xlsx", index_col=1)
    no_rows = df2.shape[0] + 2
    no_rows = str(no_rows)
    name = "C" + no_rows
    return name


def readInt(msg='Input a number'):
    while True:
        try:
            vari = int(input(msg))
        except ValueError:
            line('+', 40)
            print(f'Please, make sure you digit an integer')
            line('+', 40)
            continue
        except:
            print('An Error occured, please try again.')
            vari = 3
            break
        else:
            break
    return vari

