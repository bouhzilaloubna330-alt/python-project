import random
while True:
    level = input("chose level ( easy/medium/hard):")
    if level == "easy":
        secret = random.randint(1,10)
        print("chose 1,10")
    elif level == "medium":
        secret = random.randint(1,50)  
        print("chose 1,50")
    elif level == "hard":
        secret = random.randint(1,100)  
        print("chose 1,100")
    else:
        print("chose invalide")  
        continue   
    
    lives = 3
    while lives:
        geuse = int(input("chose the geuse nember:"))
        if geuse == secret:
            print("goood")
            break
        elif geuse <secret:
            print("too low")
        else:
            print("too high")

        
        lives=lives-1 
        print("lives left ",lives)
        if lives ==0:
            print("you lost the geuss number was:", secret)
    playagain = input("play-again yes/ no")     
    if playagain == "no":
            break
print ("finish")              
     