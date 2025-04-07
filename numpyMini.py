# Ethan Brown
# 04/05/25
# Numpy Mini Project

import numpy as np
from numpy import random

row = int(input("Please enter the number of rows for the seating chart: "))
column = int(input("Now, please enter the number of columns in the seating chart as well: "))

if __name__ == '__main__' :
	grid = np.array ( [] )
	nameList = ["Mahely", "Miriam", "Abby", "Alberth", "Manali", "Venus", "Edison", "Andrew", "Ben", "Hannah", "Ethan", "Jalen",
	"Alex", "Jaxon", "John", "Jill", "Steve", "Gerry", "Robert", "Melissa", "Paul", "Olivia", "Harry", "Sophia", "Isaac", "Kyle", "Maddy",
	"Jacob", "Andrew", "Drew", "Brenda", "Susan", "Michelle", "Mike", "Chris", "Mary"]

        # Selecting random names from nameList to enter into the seating chart
	for e in range(row):
		for b in range(column):
			randName = random.choice(nameList)
                        # append randName to grid
			grid = np.append(grid, f"{randName} ({e}, {b})   ")
                        #remove randName from randList
			nameList.remove(randName)
	#Reshaping the grid for rows and columns
	grid = grid.reshape(row, column)
        #Printing out each student with their row and column position
	for e in range(row):
		for b in range(column):
			if b < column -1:
				print(grid[e, b], end =' ')
			else:
				print(grid[e, b], end ='\n \n')
