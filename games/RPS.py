import random;
#setting up game loop
quit = False
while quit == False:
    if(quit == True):
        break
    #Options are selected
    while 1==1:
        PlrSelect = input('Rock, Paper, or Scissors ');
        print("...............");
        PlrSelect = PlrSelect.upper();
        BotChoice = ["ROCK","PAPER","SCISSORS"];
        BotSelect = BotChoice[random.randint(0, 2)];

    #Display plr and bot choices
        if(PlrSelect == 'ROCK' or PlrSelect == 'PAPER' or PlrSelect == 'SCISSORS'):
            print('YOU SELECTED ' + PlrSelect);
            print('THE BOT SELECTED ' + BotSelect);
            print("...............");
            break
        else:
            print('INVALID INPUT GIVEN');
            print("...............");

    #Figure out and announce who won
    if(PlrSelect == BotSelect):
        print("IT'S A TIE");
    elif(PlrSelect == 'PAPER' and BotSelect != 'SCISSORS'):
        print('YOU WON');
    elif(PlrSelect == 'SCISSORS' and BotSelect != 'ROCK'):
        print('YOU WON');
    elif(PlrSelect == 'ROCK' and BotSelect != 'PAPER'):
        print('YOU WON');
    else:
        print('YOU LOST');
    #ask if player will play again
    while 1==1:
        print("...............");
        PlayerPlayAgain = input('would you like to play again, "Yes" or "No"');
        PlayerPlayAgain = PlayerPlayAgain.upper();
        if(PlayerPlayAgain == 'NO'):
           quit = True;
           break
        elif(PlayerPlayAgain == 'YES'):
            break
        else:
            print('INVALID INPUT')
print('Thanks for playing!');
exit();

                            
