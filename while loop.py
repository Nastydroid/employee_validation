#k = 1

#while k <4 :
    #print('*' * k)
   # k = k + 1

#print('done')

secrete_number=12
guess_limit = 5
guess_count = 0

while guess_count < guess_limit:
    guess=int(input('Guess:'))
    guess_count += 1
    if guess == 12:
        print('you got it right!')
        break
else:
    print("try again")

