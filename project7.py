"""
CIS 15 Project 7
The Monty Hall Problem
Caitlin Baker
"""
import random


def monty_door(win_num, player_num):
    """ The monty_door function takes the randomly selected winning number and the
    user inputed choice of door (player_num) as arguments and decides which door Monty will open. 
    It returns an integer of Monty's choice of door"""
    
    if win_num == player_num:
        monty_num = int(random.randrange(1,4))
        while monty_num == win_num:
            monty_num = int(random.randrange(1,4))
            
    elif win_num != player_num:
        
        monty_num = int(random.randrange(1,4))
        while monty_num == win_num or monty_num == player_num:
            monty_num = int(random.randrange(1,4))
            
    return monty_num

def has_won(win_num, player_num, player_move):
    """ The has_won function takes the random winning number, the user inputed player number
    and the player's decision to stay or switch doors as arguments. It decides if the player 
    won the car or won a goat. It returns a boolean value of either True or False"""
    
    
    if win_num == player_num: 
        if player_move == "switch":
            result = False
        elif player_move == "stay":
            result = True
    elif win_num != player_num:
        if player_move == "switch":
            result = True
        elif player_move == "stay":
            result = False
    
    return result

def main():
    """The main funtion contains the winning number generator, all the print and input statements
    and all the calls to the two above functions"""
    
    
    win_num = int(random.randrange(1,4))
    
    player_num = int(input("Pick a door: "))
    
    monty_num = int(monty_door(win_num, player_num))
    
    print(f"Monty opened door #",monty_num)
   
    player_move = input("Do you wish to stay or switch?: ")
    
    result = bool(has_won(win_num, player_num, player_move))
    
    if result == True:
        print("You won the car!")
    elif result == False:
        print("You won a goat!")
    
if __name__ == '__main__' :
     main()
    
    