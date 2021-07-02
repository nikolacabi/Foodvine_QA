from datetime import datetime
import openpyxl
import random

# Function that generates unsername, email and password and returns them
def genuser():

    un = 'testnikola' + datetime.now().strftime("%d%m%Y%H%M%S")
    email = un + "@gmail.com"
    pw = '1234Test'

    wb = openpyxl.load_workbook('storage/data/Users.xlsx', read_only=True)
    ws = wb['Users']
    wb.close()
    row_count = ws.max_row      # row count can be read only in read_only=True so this is here and not in below part


    # wb = openpyxl.load_workbook('Users.xlsx')
    # ws = wb['Users']
    #
    # ws['A' + str(row_count + 1)] = un
    # ws['B' + str(row_count + 1)] = email
    # ws['C' + str(row_count + 1)] = pw
    #
    # wb.save('Users.xlsx')
    # wb.close()

    return un, email, pw


# Function that returns random user credentials
def getuser():

    wb = openpyxl.load_workbook('Users.xlsx', read_only=True)
    ws = wb['Users']
    row_count = ws.max_row

    n = random.randint(1, row_count - 1)

    un = ws['A' + str(n + 1)].value
    email = ws['B' + str(n + 1)].value
    pw = ws['C' + str(n + 1)].value

    wb.close()

    return un, email, pw

