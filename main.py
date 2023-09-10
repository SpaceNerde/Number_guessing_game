import random

def pick_range():
    print("pick the range\n")
    range_1 = input("From: ")
    range_2 = input("To: ")

    return range_1, range_2

def check_guess(goal_):
    print("Guess your number")
    guess = int(input(">> "))

    if guess == goal_:
        print("YOU WON!!")
        return False
    elif guess < goal_:
        print("Try Again! You guessed too low")
        return True
    elif guess > goal_:
        print("Try Again! You guessed too high")
        return True
    else:
        print("Something went wrong")
        return False

if __name__ == "__main__":
    print("Space's Number Guessing Game")

    (from_, to_) = pick_range()
    goal = random.randrange(int(from_), int(to_))

    while check_guess(goal):
        continue