from random import randint

for x in range(1,6):

    guessNumber = int(input("Enter your guess number : "))

    randomNumber = randint(1,5)

    if guessNumber == randomNumber:
        print("Congratulations!, you have won!")
        print("The random number was : ", randomNumber)

    else:
        print("Sorry!, You have lost!")

        print("The random number was : ", randomNumber)