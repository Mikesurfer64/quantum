#!/usr/bin/env python3
"""connect_four.py"""

# Goal: to write general checker for any checker board 
#possible idea is that if a 4x4 sub-arrays of "board" contain 4 "T"'s horizontally,diagonally, or vertically
# when then we can write that the player wins otherwise "No winner yet". 

# outline of code logic: if 4x4 sub array is iterated over the larger board array for every 4x4 sub-array
# of the larger array and each 4x4 sub array is checked against each of the 10 possible 4x4 solution array(s), then print T or F (win or not win)

import numpy as np

def check_winner(player, board):
    return False
    
def print_winner(board):
    print(*board, sep="\n")
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


solution_array = [
        [a[1,1], a[1,2], a[1,3], a[1,4]],
        [a[2,1], a[2,2], a[2,3], a[2,4]],
        [a[3,1], a[3,2], a[3,3], a[3,4]],
        [a[4,1], a[4,2], a[4,3], a[4,4]],
    ]

def a[i,j]:
    a[i,j] = solution_array[i,j]

# Write the 10 possible solution arrays  then check if 
# solution_array is subset of each board array
# this must be done for each player 1/2, can use arrays to assist more 

#Fix j, vertical solutions

print("Player 1 wins") if a[i,1]=a[i,j]=1 for i in range(4) or
print("Player 1 wins") if a[i,2]=a[i,j]=1 for i in range(4) or
print("Player 1 wins") if a[i,3]=a[i,j]=1 for i in range(4) or
print("Player 1 wins") if a[i,4]=a[i,j]=1 for i in range(4) or

#Fix i, horizontal solutions

print("Player 1 wins") if a[1,j]=a[i,j]=1 for j in range(4) or
print("Player 1 wins") if a[2,j]=a[i,j]=1 for j in range(4) or
print("Player 1 wins") if a[3,j]=a[i,j]=1 for j in range(4) or
print("Player 1 wins") if a[4,j]=a[i,j]=1 for j in range(4) or

# Fix i=j

print("Player 1 wins") if a[1,1], a[2,2], a[3,3], a[4,4]=[1,1,1,1] or

# Final solution type

print("Player 1 wins") if a[1,4], a[2,3], a[3,2], a[4,1]= [1,1,1,1] 

board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]

board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]

board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]

def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)

if __name__ == "__main__":
    main()

# I was able to obtain the solution from Gemini AI but missed
# the way to code this one the way 
# I wanted to solve the problem with subarrays and figured no point in 
# re-writing what AI gives me here