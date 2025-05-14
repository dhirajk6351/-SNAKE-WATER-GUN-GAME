import random
print("Select 1 for snake")
print("Select 2 for water")
print("Select 3 for gun")
user_input=int(input("Enter your choice: "))
if(user_input>3):
    print("Invalid input")
cpu_input=random.randint(1,3)
if(cpu_input==user_input):
    print("It's a tie")
elif(user_input==1 and cpu_input==2):
    print("you choice snake and enemy choice is water")
    print("You win")
elif(user_input==2 and cpu_input==1):
    print("you choice water and enemy choice is snake")
    print("You lose")
elif(user_input==2 and cpu_input==3):
    print("you choice water and enemy choice is gun")
    print("You win")
elif(user_input==3 and cpu_input==2):
    print("you choice gun and enemy choice is water")
    print("You lose")
elif(user_input==3 and cpu_input==1):
    print("you choice gun and enemy choice is snake")
    print("You win")
elif(user_input==1 and cpu_input==3):
    print("you choice snake and enemy choice is gun")
    print("You lose")

