import random
# let the computer decide how many guests we have at the tea party

num_guests = random.randint(1, 20)

# i like practicing with user input and comparing to the computer's choice

print("how many cakes do we have?")
cake_count = int(input())
print("how much tea do we have?")
cups_of_tea = int(input())

# function to compare to the computer's choice of how many guests we have at the tea party

def cakes_and_tea(cake_count, cups_of_tea):
  if cake_count and cups_of_tea >= num_guests:
    print(f"we have enough cakes and tea for our {num_guests} guests")
  else:
    print(f"we need more cakes and tea for our {num_guests} guests!")
    
# call the function to see if we are fully prepared for the tea party!    

cakes_and_tea(cake_count, cups_of_tea)
