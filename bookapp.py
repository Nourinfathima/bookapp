import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'librarydb')
mycursor = mydb.cursor()

while True:
    print("select an option from the menu")
    print('1 add book')
    print('2 view all books')
    print('3 search a book')
    print('4 update the book')
    print('5 delete a book')
    print('6 exit')

    choice = int(input('Enter an option: '))
    if(choice == 1):
        print('Book enter selected')
        book_name = input('Enter the book name : ')
        bookauthor = input('Enter the author of the book : ')
        bookcategory = input('Enter the category for each day : ')
        book_rentprice = input('Enter the price  : ')
        sql = 'INSERT INTO `books`(`bookname`, `bookauthor`, `bookcategory`, `book_rentprice`) VALUES(%s,%s,%s,%s) '
        data = (book_name,bookauthor,bookcategory,book_rentprice)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice == 2):
        print('view all book selected')
        sql = 'SELECT * FROM `books`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
        print('Sucessfully !!!!')
    elif(choice==3):
        print('search a book selected')
        category = input('Enter the category of the book you needed : ')
        sql = "SELECT `bookname`, `bookauthor`, `bookcategory`, `book_rentprice` FROM `books` WHERE `bookcategory`='"+category+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the book selected')
    elif(choice==5):
        print('delete the book selected')
    elif(choice==6):
        break    