from Add_Book import add_book
from show_book import show_book
from issue_books import issue_book
from return_book import return_book
def library():
    while True:
        print("\n 1. Add Book")
        print("\n 2. Show Book")
        print("\n 3. Issue Book")
        print("\n 4. Return Book")
        print("\n 5. Exit")
        choice = input("Enter Your Choice: ")
        if choice.isdigit():
          choice=int(choice)
          if choice==1:
            add_book()
          elif choice==2:
            show_book()
          elif choice==3:
            issue_book()
          elif choice==4:
            return_book()
          elif choice==5:
            print("Thank you")
            break
        else:
            print("Invalid Choice..!!")
    else:
        print("Invalid Input..!!")
#Function call
library()
