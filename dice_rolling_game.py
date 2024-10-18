import random

while True:
  choice = input("Roll the dice? (y/n):").lower()
  if choice == "y":
       dice1 = random.randint(1,10)
       dice2 = random.randint(1,10)
       print(f'({dice1},{dice2})')
  elif choice == "n":
        print("thank you for playing")
        break
  else:
       print("Invalid choice")