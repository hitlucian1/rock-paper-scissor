import random
print("welcome here user!")
your_choice=input("enter R for rock, enter P for paper,enter S for scissor:")
mychoice=random.choice(['R','P','S'])
if your_choice==mychoice:
    print("its a tie")
elif (your_choice == 'R' and mychoice == 'S') or (your_choice == 'P' and mychoice == 'R') or (your_choice == 'S' and mychoice == 'P'):
    result = "Congratulations, you won!"

else:
    result = "Sorry, you lost."

print("You chose:", your_choice)
print("Computer chose:", mychoice)
print(result)

