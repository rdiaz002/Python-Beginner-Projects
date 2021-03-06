##Connect-4 Python Edition
##Ronuel Diaz
##CSC113
##5/15/17

import random
while(True):
    global gameloop
    global StaleMate            
    StaleMate = 0;
    gameloop=1;
    token="";
    p1_name= input("what is player ones name?:");
    p2_name= input("what is player twos name?:");
    first = random.randint(0,1);
    inc = ([0,0],[-1,0],[0,1],[1,-1],[1,1]); # The location where we check to see if there is a matching piece 
    gameboard = (["|","|","|","|","|","|","|"],["|","|","|","|","|","|","|"]
                 ,["|","|","|","|","|","|","|"],["|","|","|","|","|","|","|"]
                 ,["|","|","|","|","|","|","|"],["|","|","|","|","|","|","|"]
                 ,["|","|","|","|","|","|","|"]); # The empty Game Board 

    def is_winner(x,y,token):
        for k in range(1,4): 
            if((x+3*inc[k][0])>=0 and (x+3*inc[k][0])<7 and (y+3*inc[k][1])>=0 and (y+3*inc[k][1])<7 and gameboard[x+inc[k][0]][y+inc[k][1]]==token and gameboard[x+2*inc[k][0]][y+2*inc[k][1]]==token and gameboard[x+3*inc[k][0]][y+3*inc[k][1]]==token):
                return 1;
        
        return 0;

    
    if(first):
        print(p1_name,"will go first")
    else:
        print(p2_name,"will go first")
   

    for i in range(len(gameboard)):#prints the empty board
                print(gameboard[0][i],gameboard[1][i],gameboard[2][i],gameboard[3][i],gameboard[4][i],gameboard[5][i],gameboard[6][i]);
         
    while(gameloop):#the game loop that controls the flow of the game 
        if(sum(x.count("|") for x in gameboard)==0):
            StaleMate = 1;
            break;
        if(first):
            print("its",p1_name,"turn"); 
            token="X";
        else:
            print("its",p2_name,"turn");
            token="O";
            
        while True:
            try:
                col = int(input("what column would you like to place your piece in?(1-7)"))-1;
                break;
            except:
                print("You made a mistake. Numbers only");
                
        while(col>=7):
            try:
                print("this isnt a possible column. Try Again");
                col = int(input())-1;
            except:
                print("Must Be A Number");
                col=11;
                
        while(col>=7 or gameboard[col].count("|")==0):
            try:
                print("that column is full try a different column(1-7)");
                col = int(input())-1;
            except:
                print("Must Be A Number");
                col=11;
                
        #inserts the players piece into their desired column    
        gameboard[col].insert(gameboard[col].count("|"),token);
        gameboard[col].pop(gameboard[col].count("|")-1);

        #checks the board for game winning moves 
        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                if(gameboard[i][j]==token):
                    if(is_winner(i,j,token)==1):
                        gameloop=0;
         #prints the board at the end of the players turn for the next player               
        for i in range(len(gameboard)):
                print(gameboard[0][i],gameboard[1][i],gameboard[2][i],gameboard[3][i],gameboard[4][i],gameboard[5][i],gameboard[6][i]);
                
        first=first^1;
        
    #decides who the winner is by what token was played last before the loop exited
    if(StaleMate):
        print("this is a stalemate");
    elif(token=="X"):
        print(p1_name,"wins!!!!");
    else:
        print(p2_name,"wins!!!!");
    redo=input("Wanna Play Agian? y OR n:  ")
    if(redo.upper() == "N"):
        break;









#  ________/\\\\\\\\\_____/\\\\\\\\\\\__________/\\\\\\\\\______/\\\______/\\\_____/\\\\\\\\\\__        
#   _____/\\\////////____/\\\/////////\\\_____/\\\////////___/\\\\\\\__/\\\\\\\___/\\\///////\\\_       
#    ___/\\\/____________\//\\\______\///____/\\\/___________\/////\\\_\/////\\\__\///______/\\\__      
#     __/\\\_______________\////\\\__________/\\\_________________\/\\\_____\/\\\_________/\\\//___     
#      _\/\\\__________________\////\\\______\/\\\_________________\/\\\_____\/\\\________\////\\\__    
#       _\//\\\____________________\////\\\___\//\\\________________\/\\\_____\/\\\___________\//\\\_   
#        __\///\\\___________/\\\______\//\\\___\///\\\______________\/\\\_____\/\\\__/\\\______/\\\__  
#         ____\////\\\\\\\\\_\///\\\\\\\\\\\/______\////\\\\\\\\\_____\/\\\_____\/\\\_\///\\\\\\\\\/___ 
#          _______\/////////____\///////////___________\/////////______\///______\///____\/////////_____
