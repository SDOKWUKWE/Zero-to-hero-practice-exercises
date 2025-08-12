#Adventure Game Introduction: Create a very simple text-based adventure game.
#Start with a scenario, e.g., "You are at a crossroads. Do you want to go 'left' or 'right'?"
#Based on the user's choice, present another choice. 
# For example, if they go 'left', they might find a 'cave' or a 'river'.
#Use nested if statements to create a small, branching story 
# with at least two levels of choices.

print("You are at a crossroad".upper())
print("Do you want to go Left or Right?")

#1. Left
#2. right

choice_1=int(input("enter 1 for left or 2 for right"))

if choice_1==1:
    #1 "cave"
    #2 "river"
    choice_1_2=int(input("enter 1 for cave or 2 for river"))
    if choice_1_2==1:
        print("WELCOME TO THE EVIL CAVE!")
        choice_1_3=str(input("to enter cave press OK, to go back press back"))
        if choice_1_3=="OK":
            print("Entered cave")
        else:
            print(choice_1_2)
    elif choice_1_2==2:
        print("WELCOME TO THE RIVER!")
        print("BEWARE OF CROCODILES")
    

