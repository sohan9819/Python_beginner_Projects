array = [ 1 , 2, 3 , 4 , 5 ,6 , 7, 8, 9]
played_moves = []

player_1 = input("Enter your name(player_1) : ")
player_2 = input("Eneter your name(player_2) : ")

# player_1 = "Sohan"
# player_2 = "Akhil"

scores = {
    player_1 : 0,
    player_2 : 0
}


def inputs():
    print("lets start the game")
    gameboard(array)
    i = 0
    while i < 9 :
        # print (i)
        if i%2 ==  0 :
            position = input("Enter the position of X {} : ".format(player_1))
            move = [ "X" , int(position)-1 ]
            player = player_1
        
        else :
            position = input("Enter the position of O {} : ".format(player_2))
            move = [ "O" , int(position)-1 ]
            player = player_2

        i += 1

        Player_moves(move)
        gameboard(array)
        if gameChecker(array , player) == True:
            i = 0
            quit()
        #     scoreboard()
        #     Again()
        # scoreboard()
    print("GameOver!!! Its  a Tie")
    


def gameboard(array):
    print("       |       |       \n    {}  |   {}   |   {}    \n ______|_______|______ \n       |       |       \n    {}  |   {}   |   {}    \n ______|_______|______ \n       |       |       \n    {}  |   {}   |   {}    \n       |       |       ".format(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7],array[8]))

def Player_moves(move):
    array[move[1]] = move[0]

def gameChecker(array , player):
    if array[0] == array[1] == array[2] or  array[0] == array[4] == array[8] or array[0] == array[3] == array[6] :
        print(" Game over ")
        print( player + " won the game")
        # scoreAdder(player)
        return True
    elif array[3] == array[4] == array[5] :
        print("Game over")
        print( player + " won the game")
        # scoreAdder(player)
        return True
    elif array[6] == array[7] == array[8] or array[6] == array[4] == array[2] :
        print("Game over")
        print( player + " won the game")
        # scoreAdder(player)
        return True
    elif array[2] == array[5] == array[8] : 
        print("Game over")
        print( player + " won the game")
        # scoreAdder(player)
        return True
    elif array[1] == array[4] == array[7] : 
        print("Game over")
        print( player + " won the game")
        # scoreAdder(player)
        return True
    else :
        None


# def scoreboard():
#     print("Name   :   Score\n{}     :   {}\n{}      :   {}" .format(player_1,scores[player_1],player_2,scores[player_2]))

# def scoreAdder(player):
#     scores[player] +=1 

# def Again():
#     ans = input("Want To Play one more match ? Yes or No : ")
#     if ans.lower() == "yes" : 
#         # boardReset(array)
#         inputs()
#     else :
#         quit()

# def boardReset(array):
#     i = 0
#     while i < len(array) :
#         array[i] = " "
#         i += 1

# gameboard(array)

inputs()
Again()
