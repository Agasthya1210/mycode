import csv
f= open('C:\\Users\\Vedasri\\PYTHON\\data.csv', 'w')
wo=csv.writer(f,delimiter=',')
lr=[]
from prettytable import PrettyTable
i=int(input('Enter number of employees: '))
myTable = PrettyTable(["S.No", "First Name", "Last Name", "Surname", "Full name", "Email ID", "Emp ID", "Mobile"])
for emp in range(1,i+1):
    print('enter person '+ str(emp)+ ' details:' )
    
    first_name=input('Enter your first name:')
    last_name=input('Enter your last name: ')
    sur_name=input('Enter your surname: ')
    full_name=first_name+' '+last_name +' '+sur_name
    email=input('Enter your email address: ')
    empid=input('Enter employee ID: ')
    number=int(input('Enter your mobile number: '))
    mobilenum=str(number)
    lr.append([emp, first_name, last_name, sur_name, full_name, email, empid, number])
    if len(mobilenum)==10:
        print('valid mobile number: '+ str(number))
    else:
        print('invalid mobile number')
    for j in range(1):
        myTable.add_row([emp, first_name, last_name, sur_name, full_name, email, empid, number])    
    print(myTable)
wo.writerows(lr)
f.close() 