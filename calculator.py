from random import choice
import mysql.connector



conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin@1234",
    database="school"
)
cursor=conn.cursor()

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Not divisible"
    return x/y
def menu():
    print("select operation")
    print("1 Add")
    print("2 Sub")
    print("3 Mul")
    print("4 div")

choice=input("Enter choice(1,2,3,4): ")
num1=int(input("enter 1 st number:"))
num2=int(input("enter 2 nd number:"))
if choice=='1':
    print(f"the result is :{add(num1,num2)}")
elif choice=='2':
    print(f"the result is :{sub(num1,num2)}")
elif choice=='3':
    print(f"the result is :{mul(num1,num2)}")
elif choice=='4':
    print(f"the result is :{div(num1,num2)}")
else:
    print("Invalid")
menu()