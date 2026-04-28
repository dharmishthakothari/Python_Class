class Book:
    def __init__(self,isbnNo , title , auther , no_of_pages):
        self.isbnNo=isbnNo
        self.title=title
        self.author=auther
        self.no_of_pages=no_of_pages
    
    def display(self):
        print(f"{self.isbnNo} - {self.title} - {self.author} - {self.no_of_pages}")

book_list=[]
no_of_books=int(input("Enter no of books "))
for i in range(no_of_books):
    isbn=input("Enter isbn ")
    title=input("Enter title ")
    aut=input("Enter Auther")
    pages=int(input("Enter no of Pages "))
    b1=Book(isbn,title,aut,pages)        
    book_list.append(b1)

print("BOOK LIST IS ")
for i in range(no_of_books):
    book_list[i].display()

