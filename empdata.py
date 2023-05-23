import pandas as pd
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

table = [[first_name, last_name, sur_name, full_name, email, empid, mobilenum]]
df = pd.DataFrame(table, columns = ['First name', 'Last name', 'surname', 'Full name' , 'email', 'empID', 'mobile number'], index=['1'])
print(df)