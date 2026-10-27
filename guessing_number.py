import random
num=random.randint(1,100)
while True:
 try:
    guess_num=int(input("Guess the number between 1 and 100-"))
    if guess_num > num:
        print("Too high")
    elif guess_num < num:
        print("Too low")
    elif guess_num == num:
        print('congratulation! you guessed right')
        break
 except ValueError:
    print("please enter valid value")




