#https://stackoverflow.com/questions/61825892/python-multiplication-quiz-invalid-syntax

import random


score = 0
continue_ = True
while continue_:
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    product = a * b
    guess =int(input("What is %d times %d,press -1 to quit  "% (a,b)))
    if guess ==-1:
        break
    if int(guess) != product:
        print("Sorry, this is wrong. It should be %d"%(product))
        #continue_ = False
    if   guess == product:
        print('Good job. You got it right.')
        score += 1

print("Thanks for playing! You score is %d"%(score))
          
	          
 
 

	
	
   
    

