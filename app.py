
message= '''

hello,we heard you are interested in buying the house.
the house cost 1$m.
but if your credit score meets our requirements,
we have a good 
payment plan for you.
'''
print (message)
user =input('what is your credit score?:')
credit =int(user)
cost_of_house= 1000000
ten = (10/100) * 1000000
twenty = (20/100) * 1000000

if credit >= 25:
    print ('you have a good credit score')
    print ('you will pay $' + str(ten) + '  for the house as downpayment')

elif credit <= 25:
    print("your credit score doesn't meet our requirements")
    print('you will pay $' + str(twenty) + " for the house as downpayment")

else:
    print('you are ineligible for this offer')