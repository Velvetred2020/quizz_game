print("Welcome to my quizz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okey! Let's play :D")
score = 0

answer = input("What does CLI stands for? ")

if answer.lower() == "command line interpreter":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What does IP stands for? ")

if answer.lower() == "internet protocol":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("Whtat does SSH stand for? ")

if answer.lower() == "secure shell":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What does SSID stand for? ")

if answer.lower() == "service set identifier":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


print("You got " + str(score) + " questions correct!")
