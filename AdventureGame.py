startingGame = input("Do You Want To Play This Adventure Game? [YES/ NO] :").lower();

if startingGame == "yes":
    print("Wellcome Buddy");
    answer = input("Do You Want To Explore Cave / Jungle? [Cave / Jungle] :").lower();
    if answer == "cave":
        goNow = input("You go into the cave and see bear sleeping [Fight/ Run] :").lower();
        if goNow == "fight":
            print("Bears Are Relly Strong..! You Lose");
        else:
            print("Wow! You Are Still Alive");
    else:
        print("You See The Hungry Tiger. Tiger Will Eat You..! Game Closed")


else:
    print("Thank You For Your Answer...!");


