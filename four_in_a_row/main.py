import numpy as np #import to work with Arrays

# create matrix to hold pieces from the board
def playspace():
    gameboard = np.zeros((6, 7)) #create initial matrix of 6 rows and 7 columns
    return gameboard;

playspace = playspace()
print(playspace)
