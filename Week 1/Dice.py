# import random numbers
from random import randint

# how many dices

atdiceno = int(input("How Many Units Attack:"))
defdiceno = int(input("How Many Units Defend:"))

# limit user to attack 1,2,3 and defender to 1 and 2
if atdiceno > 3:
    print("Please Choose number between 1 - 3 to Attack")
    exit()
elif defdiceno > 2:
    print("Please Choose number between 1 - 2 to Defend")
    exit()
    # random dices
attack1 = randint(1, 6)
attack2 = randint(1, 6)
attack3 = randint(1, 6)
defend1 = randint(1, 6)
defend2 = randint(1, 6)

# attacker

if atdiceno == 1:
    attacker = [attack1]
    print("Dice:\n ", "Attacker:", attacker[0])
elif atdiceno == 2:
    attacker = sorted([attack1, attack2], reverse=True)
    print("Dice:\n ", "Attacker:", attacker[0], '-', attacker[1])
elif atdiceno == 3:
    attacker = sorted([attack1, attack2, attack3], reverse=True)
    print("Dice:\n ", "Attacker:", attacker[0], '-', attacker[1], '-',
          attacker[2])

# defender
if defdiceno == 1:
    defender = [defend1]
    print("  Defender:", defender[0])
elif defdiceno == 2:
    defender = sorted([defend1, defend2], reverse=True)
    print("  Defender:", defender[0], '-', defender[1])


# print("Dice:\n ", "Attacker:", attacker[0], '-', attacker[1], '-',
#       attacker[2], "\n  Defender:", defender[0], '-', defender[1])

defLost = 0
atLost = 0

for i in range(0, min(atdiceno, defdiceno)):
    if (attacker[i] >= defender[i]):
        defLost += 1
    else:
        atLost += 1

print("Outcome:\n  Attacker: Lost %d units,\n  Defender lost %d units" %
      (atLost, defLost))


# if defend1 >= attack1 and defend2 <= attack2:
#     print("Outcome:\n", "Attacker: Lost 1 unit\n", "Defender: Lost 1 units")
# elif defend1 <= attack1 and defend2 <= attack2:
#     print("Outcome:\n", "Attacker: Lost 0 units\n", "Defender: Lost 2 units")
# elif attack1 <= defend1 and attack2 <= defend2:
#     print("Outcome:\n", "Attacker: Lost 2 unit\n", "Defender: Lost 0 units")
# elif attack1 >= defend1 and attack2 <= defend2:
#     print("Outcome:\n", "Attacker: Lost 1 unit\n", "Defender: Lost 1 units")
