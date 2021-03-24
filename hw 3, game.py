import random
class statbar():
    def __init__(self, hunger, happiness, health, stamina, money):
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.stamina = stamina
        self.money = money
    def feed():
        global fe
        fe = random.randint(2,7)
        d.hunger = d.hunger + fe
        d.money = d.money - 20
    def walk():
        global wa1, wa2
        wa1 = random.randint(1,3)
        d.happiness = d.happiness + wa1
        d.health = d.health + 1
        wa2 = random.randint(2,7)
        d.stamina = d.stamina - wa2
    def play():
        global pl1, pl2
        pl1 = random.randint(2,7)
        d.happiness = d.happiness + pl1
        d.health = d.health + 1
        pl2 = random.randint(2,7)
        d.stamina = d.stamina - pl2
        d.money = d.money - 20
    def heal(): 
        global he
        he = random.randint(5, 10)
        d.health = d.health + he
        d.money = d.money - 30
    def sleep():
        global sl
        sl = random.randint(1,10)
        d.stamina = d.stamina + sl
def statnow(d):
    print('hunger:',d.hunger,'| happiness:',d.happiness,'| health:',d.health,'| stamina:',d.stamina,'| money',d.money)
d = statbar(20,20,20,20,50)
a = True
wave = 1
print('Welcome to "Try Not To Upset Your Pet" RPG, made by 10912175, 10912108, 10912107 \nTake care your pet so you will survive\n')
while a == True:
    print("The pet's stat for today:")
    statnow(d)
    print("Please choose your activity(feed, walk, play, heal), 'stats' to check stats, type 'done' if you're finish your move for today")
    while True:
        act = input("Act: ")
        if act == "feed":
            statbar.feed()
            if fe < 4:
                print("hunger +",fe, "*BAD LUCK*\nYou pet spills over its food while it's eating")
            elif fe > 5:
                print("hunger +",fe, "*good luck*\nYou added extra food")
            else:
                print("hunger +",fe, "\nYou fed your dog...")
        elif act == "walk":
            statbar.walk()
            if wa1 == 1:
                print("happiness +",wa1, "*BAD LUCK*\nYour pet don't wanna walk today")
            elif wa1 == 3:
                print("happiness +",wa1, "*good luck*\nYour pet is delighted on its walk")
            else:
                print("happiness +",wa1, "You walk your dog...")
            if wa2 < 4:
                print("stamina -",wa2, "Your pet still have plenty of strength left")
            elif wa2 > 5:
                print("stamina -",wa2, "Your pet is somehow exhausted")
            else:
                print("stamina -",wa2, "Your dog got a work out")
        elif act == "play":
            statbar.play()
            if pl1 < 4:
                print("happiness +",pl1 , "*BAD LUCK*\nYour played yourself instead with your pet")
            elif pl1 > 5:
                print("happiness +",pl1 , "*good luck*\nYour pet is quite fond of the new toy you bought.")
            else:
                print("happiness +",pl1 , "You played with pet...")
            if pl2 < 4:
                print("stamina -",pl2 , "Your pet still running around")
            elif pl2 > 5:
                print("stamina -",pl2 , "Your pet lay down almost like a corpse")
            else:
                print("stamina -",pl2 , "Your dog sat down and rest")
        elif act == "heal":
            statbar.heal()
            if he < 7:
                print("health +",he , "*BAD LUCK*\nThe vet sucked and scammed your money")
            elif he > 8:
                print("health +",he , "*good luck*\nThe vet flexed his skill at you")
            else:
                print("health +",he , "\nYou brought your dog to the vet")
        elif act == "stats":
            statnow(d)
        elif act == "done":
            break
        else:
            print("What did you say?")
        if d.stamina <= 0:
            print("Your pet fainted from exhaution")
            break
        
    statbar.sleep()
    if sl < 5:
        print("It seems your pet got insomnia from vision about your future")
    elif sl >= 5:
        print("Your pet went to sleep")
    if d.stamina >= 20:
        d.stamina = 20
    wave += 1
    print("A day's over, prepare yourself for tomorrow \nDay ", wave)
    mo = random.randint(20,80)
    if mo < 40:
        print("*BAD LUCK* You accidentally dropped part of your salary on the street")
    elif mo > 60:
        print("*good luck* You got extra dividend")
    else:
        print("You got your salary")
    print("Money +", mo)
    d.money = d.money + mo
    hu = random.randint(5, 15)
    if hu < 9:
        print("Your pet doesn't feel like eating much today")
    elif hu > 12:
        print("Your pet got parasites and felt more hungry")
    else:
        print("Your dog got hungry")
    print("Hunger -", hu)
    mood = random.randint(1,9)
    if mood < 4:
        print("Your pet got a good mood today")
    elif mood > 6:
        print("Your pet got waken up forcefully and felt mad")
    else:
        print("Your pet woken up like normal")
    d.happiness = d.happiness - mood
    print("Happiness -", mood)
    d.hunger = d.hunger - hu
    if d.hunger <= 15:
        print("You pet feels hungry\n happiness -2")
        d.happiness = d.happiness - 2
        if d.hunger <= 10:
            d.happiness = d.happiness - 2
            print("You really should feed your pet\n happiness -2")
            if d.hunger <= 5:
                d.happiness = d.happiness - 4
                print("or YOU will die\n happiness -2")
    elif d.happiness <= 15:
        print("Your pet got a bit upset\n health -2")
        d.health = d.health - 2
        if d.happiness <= 10:
            print("please entertain your pet\n health -2")
            d.health = d.health - 2
            if d.happiness <= 5:
                print("or YOU will get depressed\n health -4")
                d.health = d.health - 4
    elif d.health <= 15:
        print("Your pet isn't feeling very good\n stamina -2")
        d.stamina = d.stamina - 2
        if d.happiness <= 10:
            print("go find a vet ASAP\n stamina -2")
            d.stamina = d.stamina - 2
            if d.happiness <= 5:
                print("or YOU will suffer\n stamina -4")
                d.stamina = d.stamina - 4
    if d.hunger <= 0:
        print("Since you haven't feed your pet well enough, your flesh becomes the substitude instead, and you regret your wrongdoings while your pet tears your apart(You died)")
        break
    elif d.money <= -100:
        print("You owed too much money that your can't even feed yourself, you got starved to death before your pet do(You died)")
        break
    elif d.happiness <= 0:
        print("Your pet got so bored that it torn your important paperworks to pieces, you then got fired from your job, got depression and suicided(You died)")
        break
    elif d.health <= 0:
        print("The intense sickness of your pet infected you, you died a few days later while your pet somehow took a full recovery")
        break
    elif d.hunger > 50:
        print("You stuffed so much food to you pet that its liver became FOIE GRA(Pet died)")
        break
    elif d.happiness > 40:
        print("Your pet got so exited it jump of the residential building and died(Pet died)")
        break
    elif d.health > 40:
        print("Your pet got so much vaccine to the point its bones wither and decayed(Pet died)")
        break
print("*WASTED* \n...GAMEOVER...\nYou survived", wave, "days")
