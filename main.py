# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# You are tasked with developing a program for a local library that helps in managing the books and members. The library maintains a record of books and their authors, the quantity available, and the members who have borrowed them. The system should be able to:
#
# 1 Display the list of books available.
# 2 Allow the user to input a book they want to borrow.
# 3 Keep track of the books borrowed by each member.
# 4 Update the quantity of books when borrowed/returned.
# 5 Display the books borrowed by a specific member.
# The library has a collection of 10 books with their titles, authors, and quantities. Each member can borrow up to 3 books at a time. There are in total 50 students, each with a unique student id from 1 to 50.

# OOP: object-oriented programming 面向对象编程 class
# Functional programming: functions
#
# balances = [100
# addresses = ["singapore xxx street"
# ids = [65432
#
# def deposit(amount, i):
#     balances[i] = balances[i] + amount
#     print("deposited xxx dollars")
#
# def withdraw(amount, i):
#     balances[i] = balances[i] - amount
#     print("withdrew xxx dollars")
#
# def checkBalance(i):
#     return balances[i]
#
# for i in range(len(balances)):
#     if balances[i] < 10000:
#         deposit(10000 - balances[i], i)
#
#
# class ATM() {
#     # attributes
#     private int balance;
#     private string address;
#     private int id;
#
#
#     # methods
#     ATM(int balance, string address, int id) {
#         this.balance = balance;
#         this.address = address;
#         this.id = id;
#     }
#     int deposit(int amount) {
#         balance = balance + amount;
#     }
#     void topupIfNeeded() {
#         if (this.balance < 10000) {
#             this.deposit(10000 - this.balance);
#         }
#     }
#     # ...
# }
#
# class Bank{}
# class BankBranch{}
# class Customer{}
# class BankAccount{}
# class BankCard{}
#
#
# ATM atm1 = new ATM(10000, "NUS", 1234);
#
# atm2, atm3
# List<ATM> atms = new List<>([atm1, atm2, atm3]);
# for (ATM atm : atms) {
#     atm.topupIfNeeded();
# }
#
# # C
# # Java, Python, C++, Golang


book_names = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "The Hobbit",
    "The Lord of the Rings",
    "Brave New World",
    "The Hunger Games",
    "Harry Potter and the Sorcerer's Stone"]
book_authors = [
    "J.D. Salinger",
    "Harper Lee",
    "George Orwell",
    "Jane Austen",
    "F. Scott Fitzgerald",
    "J.R.R. Tolkien",
    "J.R.R. Tolkien",
    "Aldous Huxley",
    "Suzanne Collins",
    "J.K. Rowling"]

book_quantities = [6, 7, 8, 10, 4, 6, 7, 3, 4, 5]
student_books = []
max_amount = 3
for i in range(50):
    placeholder = ["NA", "NA", "NA"]
    student_books.append(placeholder)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def borrowedLessThanMax(stu_id):
    for book_name in student_books[stu_id]:
        if book_name == "NA":
            return True
    return False


def addBookToStu(stu_id, book_name):
    for i in range(3):
        if student_books[stu_id][i] == "NA":
            student_books[stu_id][i] = book_name
            return 0


def isValidStuId(stu_id):
    if stu_id >= 1 and stu_id <= 50:
        return True
    else:
        return False


def borrowBook(stu_id, book_name):
    if not isValidStuId(stu_id):
        return "invalid student id"

    for i in range(len(book_names)):
        if book_names[i] == book_name:
            if book_quantities[i] > 0:
                if borrowedLessThanMax(stu_id):
                    addBookToStu(stu_id, book_name)
                    book_quantities[i] -= 1


def studentHasBook(stu_id, book_name):
    for stu_book_name in student_books[stu_id]:
        if stu_book_name == book_name:
            return True

    return False


def removeBookFromStu(stu_id, book_name):
    for i in range(3):
        if student_books[stu_id][i] == book_name:
            student_books[stu_id][i] = "NA"
            return 0


def returnBook(stu_id, book_name):
    if studentHasBook(stu_id, book_name):
        removeBookFromStu(stu_id, book_name)
        for i in range(len(book_names)):
            if book_names[i] == book_name:
                book_quantities[i] += 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
