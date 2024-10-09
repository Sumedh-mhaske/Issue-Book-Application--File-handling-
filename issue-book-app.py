
# This application is used by librarian

'''
We need 3 files for this application
    1. all_books.txt
    2. all_stud.txt
    3. all_issued.txt

1. all_books.txt conatins :-
    book_num, book_title, book_author, book_publication

2. all_stud.txt :- 
    stud_enr, stud_name, stud_class, stud_email, stud_mob

3. all_issued.txt :-
    book_num, stud_enr, iss_date, ret_date, ret_status

'''
# ====================================================================


import datetime

# Getting the current date
date = datetime.date.today()
day = date.day
mon = date.month
year = date.year
full_date = str(day) + "/" + str(mon) + "/" + str(year)

# --------------------------------------------------------- #

s = ','

def book_file_in_r():
    fobj = open('all_book.txt', 'r')
    fdata = fobj.readlines()
    fobj.close()

    return fdata

def stud_file_in_r():
    fobj = open('all_stud.txt', 'r')
    fdata = fobj.readlines()
    fobj.close()

    return fdata

def issued_file_in_r():
    fobj = open('all_issued.txt', 'r')
    fdata = fobj.readlines()
    fobj.close()

    return fdata

# Function for issuing book
def issue_book():
    book_num = input('Enter book number : ')
    stud_enr = input('Enter student enrollment number : ')
    ret_status = 'NO'
    ret_date = 'NA'

    book_found = False
    book_data = book_file_in_r()
    for i in book_data:
        ls = i.split(s)
        if ls[0] == book_num:
            book_found = True
            break
    if book_found == False: print('Invalid Book Number')

    stud_found = False
    stud_data = stud_file_in_r()
    for i in stud_data:
        ls = i.split(s)
        if ls[0] == stud_enr:
            stud_found = True
            break
    if stud_found == False: print('Invalid student enrollment number')

    if book_found == True and stud_found == True:
        fobj = open('all_issued.txt', 'a')
        fobj.write(book_num + s + stud_enr + s + full_date + s + ret_date + s + ret_status + '\n')
        fobj.close()
        print('Book issued...')


# Function for book returning
def return_book():
    book_num = input('Enter book number : ')

    fdata = issued_file_in_r()
    found = False
    ind = 0
    for i in fdata:
        ls = i.split(s)
        if ls[0] == book_num:
            ls[3] = full_date
            ls[4] = 'YES'
            found = True
            fdata[ind] = ls
            break
        else: ind += 1
        
    if found == False: print('Invalid book number')
    elif found == True: print('Book returned succesfully')

# Function to view not returned books
def view_not_ret():
    fdata = issued_file_in_r()

    for i in fdata:
        ls = i.split(s)
        if ls[4] == 'NO\n':
           print('Book number :', ls[0]) 
           print('Student enrollment number :', ls[1])
           print('Book issued date :', ls[2])
           print('Return date :', ls[3])
           print('Return status :', ls[4])
        
# Function to search student 
def search_stud():
    enr = input("Enter student's enrollment number : ")

    fdata = stud_file_in_r()
    found = False 
    for i in fdata:
        ls = i.split(s)
        if ls[0] == enr:
            print('Student name :', ls[1])
            print('Student class :', ls[2])
            print('Student email :', ls[3])
            print('Student mobile number :', ls[4])
            found = True
            break
        
    if found == False: print('Invalid enrollment number')


# Function to search book 
def search_book():
    book_num = input('Enter book number : ')

    fdata = book_file_in_r()
    found = False
    for i in fdata:
        ls = i.split(s)
        if ls[0] == book_num:
            print('Book Title :', ls[1])
            print('Book Author Name :', ls[2])
            print('Book Publication Name :', ls[3])
            found = True
            break
    if found == False: print('Invalid book number')
    

# Function to see the history of student 
def stud_history():
    enr = input('Enter student enrollment number : ')

    fdata = issued_file_in_r()

    found = False
    for i in fdata:
        ls = i.split(s)
        if ls[1] == enr:
            found = True
            print('Student issued book :', ls[0])
            print('Issued on :', ls[2]) 
            print('Booked returned? :', ls[4])
            if ls[4] == 'YES\n':
                print('Returned date :', ls[3])
    
    if found == False: print('Invalid enrollment number')

# Function to see book history
def book_history():
    pass

# Function to add new book
def add_new_book():
    book_num = input('Enter book number : ')
    book_title = input('Enter book title : ')
    book_author = input('Enter book author name : ')
    book_publication = input('Enter book publications name : ')

    book_file = open('all_book.txt', 'a')
    book_file.close()

    book_data = book_file_in_r()
    book_found = False
    for i in book_data:
        ls = i.split(s)
        if ls[0] == book_num:
            book_found = True
            break

    if book_found == True: print('Book already present')
    elif book_found == False:
        fobj = open('all_book.txt', 'a')
        fobj.write(book_num + s + book_title + s + book_author + s + book_publication + '\n')
        fobj.close()

        print('New Book added succesfully...')


# Function to add new student 
def add_new_stud():
    s_enr = input('Enter student enrollment number : ')
    s_name = input('Enter student name : ')
    s_class = input('Enter student class : ')
    s_email = input('Enter student email : ')
    s_mob = input('Enter student mobile number : ')

    stud_file = open('all_stud.txt', 'a')
    stud_file.close()

    fstud = open('all_stud.txt', 'r')
    stud_data = fstud.readlines()
    fstud.close()
    
    stud_found = False
    for i in stud_data:
        ls = i.split(s)
        if ls[0] == s_enr:
            stud_found = True
            break

    if stud_found == True: print('Student already present')
    elif stud_found == False:
        fobj = open('all_stud.txt', 'a')
        fobj.write(s_enr + s + s_name + s + s_class + s + s_email + s + s_mob + '\n')
        fobj.close()

        print('New Student added succesfully...')

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
    

