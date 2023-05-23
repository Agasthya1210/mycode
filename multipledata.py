import pandas as pd
i=int(input('Enter number of employees: '))
for emp in range(1,i+1):
    print('enter person'+ str(emp)+ 'details' )
    first_name=input('Enter your first name:')
    last_name=input('Enter your last name: ')
    sur_name=input('Enter your surname: ')
    full_name=first_name+' '+last_name +' '+sur_name
    email=input('Enter your email address: ')
    empid=input('Enter employee ID: ')
    number=int(input('Enter your mobile number: '))
    mobilenum=str(number)
    if len(mobilenum)==10:
        print('valid mobile number: ')
    else:
        print('invalid mobile number')
    for num in range(2):
        table = [[first_name, last_name, sur_name, full_name, email, empid, mobilenum]]
        df = pd.DataFrame(table, columns = ['First name', 'Last name', 'surname', 'Full name' , 'email', 'empID', 'mobile number'], index=[emp])
        print(df)
