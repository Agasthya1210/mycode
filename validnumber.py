number=int(input('Enter your mobile number: '))
mobilenum=str(number)
if len(mobilenum)==10:
    print('valid mobile number: '+ str(number))
else:
    print('invalid mobile number')
