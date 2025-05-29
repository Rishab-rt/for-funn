def handCricket(overs):
    import random
    if overs <= 0:
        exit()
    totalBalls = overs*6
    botBalls = overs*6
    ballsLeft = overs*6
    toss = int(input("Pick 1 for heads and 2 for tails: "))
    toss1 = random.randint(1,2)
    userScore = 0
    botScore = 0
    if toss==toss1:
        decision = input("You won the toss! Would you like to bat or bowl?: ")
        if decision == "bat":
            while ballsLeft>0:
                play = int(input("Bat!: "))
                botPlay = random.randint(0,6)
                ballsLeft-=1
                if play == botPlay:
                    print("You are out after a score of",userScore,"in",totalBalls-ballsLeft,"deliveries")
                    break
                else:
                    userScore += play
                    print("Current score is",userScore,"in",totalBalls-ballsLeft,"balls with",ballsLeft,"balls remaining")

            print("You have to now defend",userScore,"in",totalBalls,"balls")
            while botBalls>0:
                userPlay = int(input("Bowl!: "))
                botplay = random.randint(0,6)
                botBalls-=1
                if botScore>userScore:
                    print("Sorry, the Bot beat you with",botBalls,"left")
                if botplay == userPlay:
                    print("Bot is out! Congratulations, you win by",userScore-botScore)
                    exit()
                else:
                    botScore+=botplay
                    print("Current score is",botScore,"in",totalBalls-botBalls,"balls with",botBalls,"balls remaining")
            if userScore>botScore:
                print("Congratulations, you win by",userScore-botScore,"runs")
                exit()
                
        else:
            while botBalls>0:
                userPlay = int(input("Bowl!: "))
                botplay = random.randint(0,6)
                botBalls-=1
                if botplay == userPlay:
                    print("Bot is out, you have to chase",botScore+1)
                    break
                else:
                    botScore += botplay
                    print("Current score is",botScore,"in",totalBalls-botBalls,"balls with",botBalls,"balls remaining")
           
            while ballsLeft>0:
                userPlay = int(input("Bat!: "))
                botplay = random.randint(0,6)
                botBalls-=1
                if botplay == userPlay:
                    print("You lost by",botScore-userScore)
                    exit()
                else:
                    userScore+=userPlay
                    if userScore > botScore:
                        print("Congratulations! You beat the bot with",ballsLeft,"balls left")
                        exit()
            
    else:
        if toss1 == 1:
            print("Bot has won the toss and has decided to bat first: ")
            while botBalls>0:
                userPlay = int(input("Bowl!: "))
                botplay = random.randint(0,6)
                botBalls-=1
                if botplay == userPlay:
                    print("Bot is out, you have to chase",botScore+1)
                    break
                else:
                    botScore += botplay
                    print("Current score is",botScore,"in",totalBalls-botBalls,"balls with",botBalls,"balls remaining")
                    
            while ballsLeft>=0:
                userPlay = int(input("Bat!: "))
                botplay = random.randint(0,6)
                ballsLeft-=1
                if botplay == userPlay:
                    print("You lost by",botScore-userScore)
                    exit()
                else:
                    userScore+=userPlay
                    print("Current score is",userScore,"in",totalBalls-ballsLeft,"balls with",ballsLeft,"balls remaining")
                    if userScore > botScore:
                        print("Congratulations! You beat the bot with",ballsLeft,"balls left")
                        exit()
        else:
            print("You lost the toss, and the bot has decided to bowl first")
            while ballsLeft>0:
                userPlay = int(input("Bat!: "))
                botplay = random.randint(0,6)
                ballsLeft-=1
                if botplay == userPlay:
                    print("You are out. Score:",userScore)
                    break
                else:
                    userScore += userPlay
                    print("Current score is",userScore,"in",totalBalls-ballsLeft,"balls with",ballsLeft,"balls remaining")
                
           
            while botBalls>0:
                userPlay = int(input("Bowl!: "))
                botplay = random.randint(0,6)
                botBalls-=1
                if botplay == userPlay:
                    print("Congratulations! You beat the bot by",userScore-botScore)
                    exit()
                else:
                    botScore+=botplay
                    if userScore < botScore:
                        print("Sorry, you lost to the bot")
                        exit()

time = int(input("How many overs would you like to play?: "))
handCricket(time)