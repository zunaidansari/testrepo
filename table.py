#ED mean employee details
i=0
n = int(input("Enter the number of employees detail you want to store: "))
while i<n:
    Name = str(input("Name: "))
    DOB = str(input("DOB: "))
    Salary = int(input("Salary: "))
    i = i+1
EDlist = [Name,DOB,Salary]
Menu = int(input("Enter a number between 2 to 8: "))
if (Menu==2) :
    print(EDlist)
if (Menu==3) :
    EDlist.insert(ABC,dd-mm-yyyy,XXXX)
    print(EDlist)
if (Menu== 4):
    print(EDlist.remove("Name"))
if (Menu ==5):
    print(EDlist.min(DOB))
if (Menu ==6) :
    print(EDlist.sort(Salary))
if (Menu ==8):
    exit
