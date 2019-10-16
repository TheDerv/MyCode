#!/usr/bin/env python3

round = 0

while True:
    round += 1
    print('Finish the movie title, "Monty Python\'s The Life of _________"')
    answer = input("Well? GET ON WITH IT!:  ")

    if answer.lower() == 'brian':
        print('I do say, very good ol chap')
        break
    if answer.lower() == "shrubbery":
        print("A SHRUBBERY?! We now require you to cut down the mightiest tree in the forest with this....Herring!")
        break

    elif round==3:
        print('NI! Twas Brian you fool!')
        break
    else:
        print("NI! Get it right or I shall Ni you a another time!")
