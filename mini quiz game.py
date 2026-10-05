score = 0

answer = input("What is the capital of India? ")

if answer == "new delhi":
    score = score+1
else:
    print("wrong answer!")

answer = input("What is the largest planet in our solar system? ")
if answer == "jupiter":
    score = score+1
else:
    print("wrong answer!")

answer = input("Which language is primarily used to style web pages?")
if answer == "CSS":
    score = score+1
else:
    print("wrong answer!")
print(f"Your score is: {score}")
