
# This application is used by librarian

import datetime

# Getting the current date
date = datetime.date.today()
day = date.day
mon = date.month
year = date.year
full_date = str(day) + "/" + str(mon) + "/" + str(year)

# --------------------------------------------------------- #

# Function for issuing book
def issue_book():
    book_num = input('Enter book number : ')
    stud_enr = input('Enter student enrollment number : ')
    ret_status = 'NO'
    ret_date = 'NA'

    fobj = open('all_issued.txt', 'a')
    fobj.write(book_num + ',' + stud_enr + ',' + full_date + ',' + ret_date + ',' + ret_status + '\n')
    fobj.close()

    print('Book issued...')

# Function for book returning
def return_book():
    pass

# Function to view not returned books
def view_not_ret():
    fobj = open('all_issued.txt', 'r')
    fdata = fobj.readlines()
    fobj.close()

    for i in fdata:
        ls = i.split(',')
        if ls[4] == 'NO\n':
           print('Book number :', ls[0]) 
           print('Student enrollment number :', ls[1])
           print('Book issued date :', ls[2])
           print('Return date :', ls[3])
           print('Return status :', ls[4])
        

# Function to search student 
def search_stud():
    pass

# Function to search book 
def search_book():
    pass

# Function to see the history of student 
def stud_history():
    pass

# Function to see book history
def book_history():
    pass

# Function to add new book
def add_new_book():
    pass

# Function to add new student 
def add_new_stud():
    pass

# List of options
def operations():
    print('\nSelect operation')
    print('1 - Issue Book')
    print('2 - Return Book')
    print('3 - View Not Returned Book')
    print('4 - Search Student')
    print('5 - Search Book')
    print('6 - Student History')
    print('7 - Book History')
    print('8 - Add New Book')
    print('9 - Add New Student')
    print('0 - Exit')

# Cheching the user choice
def check_op():
    if ch == 1 : issue_book()
    elif ch == 2: return_book()
    elif ch == 3: view_not_ret()
    elif ch == 4: search_stud()
    elif ch == 5: search_book()
    elif ch == 6: stud_history()
    elif ch == 7: book_history()
    elif ch == 8: add_new_book()
    elif ch == 9: add_new_stud()
    elif ch == 0: exit(0)


while True:
    operations()
    ch = int(input('Enter the operation you want to perform : '))
    check_op()
    

