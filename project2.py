import random
def userchoice(): 
    print("enter rock paper or scissior")
    return input("enter HERE...").lower().strip()
def compchoice():
    options=('rock','paper','scissior') 
    return random.choice(options)
def winner(user,computer):
    if(user == computer ):
      return "its a draw "
    elif(user=='rock'and computer=='scissior'or\
    user=='scissior'and computer=='paper'or\
    user=='paper'and computer=='rock'):
      return"you win"
    else:
       return"computer win"
def playgame():
    while True:
     user=userchoice()
     computer=compchoice()
     print(f"computer choose={computer}")
     result=winner(user,computer)
     print(result)

     again = input("yes or no to play again").lower().strip()
     if again != 'yes':
       print("game over")
       break 

playgame()