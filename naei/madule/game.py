import random

ScoreX = 0
ScoreY = 0

while ScoreX < 3 and ScoreY < 3:
    x = random.randint(1,3)
    y = int(input("1.sang\n2.kaghaz\n3.gheychi\n"))

    if y > x:
        if y-1 == x:
            ScoreY += 1
            print("you")
        else:
            ScoreX += 1
            print("me")
    elif x > y:
        if x-1 == y:
            ScoreX += 1
            print("me")
        else:
            ScoreY += 1
            print("you")

if y>x:
    print("you won")
else:
    print("you lost")


