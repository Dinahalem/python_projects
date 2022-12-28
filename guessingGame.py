secret_word="pythonGame"    #guess word
guess=""

guess_count = 0     #counter
guess_limit= 3     # Every user has 3 tries to guess the word
out_of_guesses=False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
       guess= input("enter guess: ")
       guess_count +=1
    else:
      out_of_guesses=True   # if user used 3 tries wrong then print ("you lose out of guess")
    
if out_of_guesses:
        print("you lose out of guess")

else:
        print("you win")   #if user guesses the correct word then  print("you win")
 
