import art
import game_data
import random
from replit import clear

def generate():
  """Generates a random thing from dictionary"""
  num = random.randint(0,36)
  value =  game_data.data[num]
  delete_dict(num)
  return value
 ############################################################################################## 
def delete_dict(num):
  """Deletes dictionary item after used"""
  del game_data.data[num]
  
###############################################################################################
def check_higher(A, B):
  """Checks which has higher follower count"""
  valueA = A["follower_count"]
  valueB = B["follower_count"]
  if(valueA > valueB):
    return A
  else:
    return B

###############################################################################################

def description(A, B):
  """Prints the dictionary list in appropriate description"""
  # Print A
  print(art.logo)
  nameA = A["name"]
  descriptionA = A["description"]
  countryA = A["country"]
  print(f"Choose A: {nameA}, a {descriptionA}, from {countryA}")

  #Print B
  print(art.vs)
  nameB = B["name"]
  descriptionB = B["description"]
  countryB = B["country"]
  print(f"Choose B: {nameB}, a {descriptionB}, from {countryB}")
  
###############################################################################################

winning = True
points = 0
A = generate()
while(winning == True):
  
  B = generate()

  #get which is higher
  higher = check_higher(A,B)
  #prints both choices
  description(A, B)

  #ask user to pick
  choice = input("Who has more followers? Type 'A' or 'B': ")

  if(choice == "A"):
    choice = A
  else:
    choice = B

  #checks if users guess was right
  if(choice == higher):
    points += 1
    print(f"\n----------------------- Thats correct! Score: {points} ----------------------------")
    A = choice
    clear()
  else:
    winning = False

print(f"\nSorry you were incorrect. Finished with a score of {points}")
    
    


