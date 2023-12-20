#rock paper scissor game in python
#import the random module to get randomness in game
import random
#initialise the variables
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#take the input from the user
choice=int(input("what do u choose! 1 for rock , 2 for paper, 3 for scissors :"))
#print the ascii diagrams of the choice selected
if choice==1:
  print(rock,"u chose rock")
elif choice==2:
  print(paper,"u chose paper")
else:
  print(Scissors,"u chose Scissors")
#get the random choice from the computer  
decision=random.choice([rock,paper,Scissors])
print(decision)
#print the random choice of the computer
if decision==rock:
  print("computer chose rock")
elif decision==paper:
  print("computer chose paper")
else:
  print("computer chose scissors")
print("\n\n")
#result of the game
if (choice==1 and decision==rock) or (choice==2 and decision==paper) or \
 (choice==3 and decision==Scissors):
  print("it's a draw")
elif (choice==1 and decision==paper) or (choice==2 and decision==Scissors) or \
   (choice==3 and decision==rock):
   print("computer wins")
else:
  print("you win")             
  


