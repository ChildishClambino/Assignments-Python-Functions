def quiz_game():
    score = 0
    answer1 = input("how many states are in the United States?: ")
    if answer1 == "50":
        print("correct")
        score += 1
    else:
        print("wrong!")

    answer2 = input("how many legs does a centepede have?: ")
    if answer2 == "100":
        print("nice you got it right!")
        score += 1
    else:
        print("wrong loser")
    
    answer3 = input("This is an easy one. what color is the sky?: ")
    if answer3.lower() == "blue":
        print("easy peasy lemon squeasy!")
        score += 1
    else:
        print("Dang you are Patrick Star")

    if score == 3:
        print("3 out of 3 you have a brain!")
    elif score == 2:
        print("2 of 3 could be worse")
    else:
        print(score," out of 3 smoooooth braiiinnnnn")

quiz_game()
    
