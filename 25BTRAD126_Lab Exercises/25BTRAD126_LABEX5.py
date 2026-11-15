# Number guessing game 

number = 25
guess = int(input("Guess the number: "))

while guess != number:

    if guess > number:
       print("Your guess is too high!")
    else:
       print("Your guess is too low!")
          
    guess = int(input("Guess again: "))

print(f"Congratulations! {number} is correct!")