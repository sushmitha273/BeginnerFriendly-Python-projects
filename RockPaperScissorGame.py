import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameimages=[rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >=3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
    print(gameimages[user_choice])
    computer_choice=random.randint(0,2)
    print(computer_choice)
    print(gameimages[computer_choice])


    if (user_choice==0 and computer_choice==2) or (user_choice>computer_choice):
        print("You win")
    elif (user_choice==2 and computer_choice==0) or (user_choice<computer_choice):
        print("You lose")
    else:
        print("draw")
