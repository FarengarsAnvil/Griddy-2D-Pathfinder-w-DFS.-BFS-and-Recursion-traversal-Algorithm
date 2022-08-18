from collections import deque


class grid():

    # Initialises the attributes that each grid object will have, which is null and then set by the user.
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.startingPoint = 0
        self.current = 0
        self.destination = 0
        self.gridNodes = []
        self.obstacleList = []
        self.nodes2D = []
        self.availableNodes = []
        self.visited = []
        self.pathList = []

    # Method initialises the Grid, the Grid Nodes, and the number of rows and columns.
    def makeGrid(self):
        # Catch Invalid input error and recall makeGrid func. Stops incorrect user input and crashing.
        try:
            rows = int(input("Enter number of rows for the Grid:"))
            columns = int(input("Enter number of columns for the Grid:"))
            self.rows = rows
            self.columns = columns
            # Boolean Array Check if we've visited Node. FOR DFS ONLY.
            self.visited = [[False for i in range(self.rows)] for i in range(self.columns)]
            # Ensures only valid Integer > 0 is allowed.

            # Ensure Grid Size is Positive X, Y only.
            if rows <= 0 or columns <= 0:
                print("\nInvalid Grid Size\n")
                self.makeGrid()

            # Self.gridNodes array contains all the available nodes in the grid.
            for i in range(rows):
                for j in range(columns):
                    self.gridNodes.append((i, j))

        except ValueError:
            print("Invalid Input. try again")
            self.makeGrid()

    # Allows User to set start and destination point.
    def setPoints(self):

        # Catch invalid input errors from user and recall func.
        try:
            # Checks that Start co-ordinates are  > 0 but < Row or Column to ensure it's within Grid Bounds.
            start = input("Enter X and Y Co-ordinates of starting point in the form X,Y:")
            if int(start[0]) < self.rows and int(start[2]) < self.columns:
                if int(start[0]) >= 0 and int(start[2]) >= 0:
                    self.startingPoint = (int(start[0]), int(start[2]))
                    print("Start is: ", self.startingPoint)


            else:
                print("Invalid start co-ordinates")
                self.setPoints()

            # Checks the destination co-ordinates are != Start co-ordinates.
            # Checks destination co-ordinates are within Grid bounds.

            destination = input("Enter X and Y Co-ordinates of Destination point in the form X,Y:")
            if int(destination[0]) != int(start[0]) or int(destination[2]) != int(start[2]):
                if int(destination[0]) < self.rows and int(destination[2]) < self.columns:
                    if int(destination[0]) >= 0 and int(destination[2]) >= 0:
                        self.destination = (int(destination[0]), int(destination[2]))
                        print("Destination: ", self.destination)

                    else:
                        print("Invalid destination co-ordinates")
                        self.setPoints()
                else:
                    print("Invalid destination co-ordinates")
                    self.setPoints()

            else:
                print("Invalid destination co-ordinates")
                self.setPoints()




        except ValueError:
            print("Invalid Co-ordinate entry")
            self.setPoints()

        self.pathList.append(self.startingPoint)

    # Function responsible for allowing the user to add Obstacles to the Grid.
    def addObstacles(self):
        while True:
            try:
                cartesian = input(
                    "Enter X and Y co-ordinates of obstacle in the form X,Y: or press e key to exit:")
                # First ensure obstacle X co-ordinate != start or destination X co-ordinate
                if int(cartesian[0]) != self.startingPoint[0] or int(cartesian[0]) != self.destination[0]:
                    # Second ensure obstacle Y co-ordinate != start or destination X co-ordinate
                    if int(cartesian[2]) != self.startingPoint[1] or int(cartesian[2]) != self.destination[1]:
                        # Next 2 Lines ensure co-ordinate is bound within the grid and does not exceed.
                        if int(cartesian[0]) < self.rows and int(cartesian[2]) < self.columns:
                            if int(cartesian[0]) >= 0 and int(cartesian[2]) >= 0:

                                # Adds the Co-ordinates to the self.obstacleList list
                                cartesian = (int(cartesian[0]), int(cartesian[2]))
                                self.obstacleList.append(cartesian)


                            # Handling illegal input from user, if the user inputs invalid co-ordinate locations, the function addObstacles() is called and error msg is printed.
                            else:
                                print("Invalid Location on Grid:")
                                self.addObstacles()
                        else:
                            print("Invalid Location on Grid:")
                            self.addObstacles()
                    else:
                        print("Invalid Location on Grid:")
                        self.addObstacles()

                else:
                    print("Invalid Location on Grid:")
                    self.addObstacles()

            # User can cease adding obstacles by pressing any key.
            except ValueError:
                break
        # List contains all Available Nodes for traversal, excluding those nodes that are Obstacles.
        self.availableNodes = [x for x in self.gridNodes if x not in self.obstacleList]

    def traversal(self, curr):
        # Parsing the starting and final co-ordinates as a List item to traverse the grid when a position vector is applied to current position.
        final = list(self.destination)
        current = list(curr)
        # Loop through Self.availableNodes List and convert elements from tuple to list to become mutable for same type comparison.
        for i in range(len(self.availableNodes)):
            self.availableNodes[i] = list(self.availableNodes[i])

        # Positive Adjacent Nodes visited by going +1 in either X,Y or Z axis on GRID.
        newX = [current[0] + 1, current[1]]
        newZ = [current[0] + 1, current[1] + 1]
        newY = [current[0], current[1] + 1]

        for i in range(len(self.availableNodes)):
            # Base Case 1: Current = Destination, so we break.
            if current == final:
                break
            # Base Case 2: Destination is appended to self.pathList, so we can stop making recursive calls.
            if final in self.pathList:
                break

            elif self.availableNodes[i] == newX:
                current = newX
                self.pathList.append(current)
                self.traversal(current)

            elif self.availableNodes[i] == newY:
                current = newY
                self.pathList.append(current)
                self.traversal(current)


            elif self.availableNodes[i] == newZ:
                current = newZ
                self.pathList.append(current)
                self.traversal(current)

    # Function simply displays solution to Traversal in formatted easily comprehensible form.
    def display(self):
        # Converts list elements back into tuple from List. Loops through self.availablePaths
        for i in range(len(self.pathList)):
            self.pathList[i] = tuple(self.pathList[i])
        if self.destination in self.pathList:
            print(self.pathList)
        else:
            print("Could not find")

    # Converts self.pathList into a 2D array for a Depth first search.
    def arrayConversion(self):
        self.nodes2D = []
        start = 0
        end = self.columns
        for i in range(self.rows):
            self.nodes2D.append(self.availableNodes[start:end])
            start += self.columns
            end += self.columns

    # Function contains the Pre req checks for the DFS and BFS.
    def isValid(self, row, col):
        # Checks if Node is within Bounds of Grid.
        if row < 0 or col < 0 or row >= self.rows or col >= self.columns:
            return False

        # Checks if we've already visited the Node.
        if self.visited[row][col]:
            return False

        return True

    # Function implements Depth First Search to go from start to Destination on the Grid.
    def DFS(self, row, col, grid):
        # Direction Vectors
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]

        # Used for holding Nodes. Initialised with Grid Starting Point.
        # We Push Grid nodes in Self.nodes2D onto stack and then later pop them in the while Loop and then splice [0] and [1]
        # The X and Y Co-ordinates and assign them to the row and col parameters so they can be passed to the isValid function when it's called.
        stack = []
        stack.append(grid[row][col])
        solution = []
        while len(stack) != 0:
            # Breaks loop once Destination is found in the DFS.
            if self.destination in solution:
                break

            current = stack[len(stack) - 1]
            stack.remove(current)
            row = current[0]
            col = current[1]

            if not self.isValid(row, col):
                continue

            self.visited[row][col] = True
            solution.append(grid[row][col])

            # Iterate thru Direction Vectors and apply direction to current row and col and append to stack as a list.
            for i in range(4):
                xPos = row + dRow[i]
                yPos = col + dCol[i]
                stack.append([xPos, yPos])

        # Solution: List holds all the Nodes in order of the DFS of the 2D Array self.nodes2D and returns it.
        print(solution)

    # Implements BFS On a 2D Array matrix.
    def BFS(self, row, col, grid):
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        queue = deque()
        solution = []
        queue.append((row, col))
        self.visited[row][col] == True

        while len(queue) != 0:

            if self.destination in solution:
                break

            node = queue.popleft()
            x = node[0]
            y = node[1]
            solution.append(grid[x][y])

            for i in range(4):
                xPos = x + dRow[i]
                yPos = y + dCol[i]
                if self.isValid(xPos, yPos):
                    queue.append((xPos, yPos))
                    self.visited[xPos][yPos] = True

        print(solution)


def main():
    print("Griddy: A 2D grid pathfinding console program\n")

    grid1 = grid()
    grid1.makeGrid()
    grid1.setPoints()
    print("Options List: Please Run options 2 and 3 before Option 1:\n")
    print("1) Recursive approach")
    print("2) Depth first search")
    print("3) Breadth first search")

    usrResponse = input("\nChoose option by entering a value from 1-3 or press e to exit:\n")

    if usrResponse == '1':
        grid1.addObstacles()
        grid1.traversal(grid1.startingPoint)
        grid1.display()
        main()

    if usrResponse == '2':
        print("Note: do not add any obstacles when using DFS or BFS else it will not work")
        grid1.addObstacles()
        grid1.arrayConversion()
        grid1.DFS(grid1.startingPoint[0], grid1.startingPoint[1], grid1.nodes2D)
        main()

    if usrResponse == '3':
        print("\nNote: do not add any obstacles when using DFS or BFS else it will not work\n")
        grid1.addObstacles()
        grid1.arrayConversion()
        grid1.BFS(grid1.startingPoint[0], grid1.startingPoint[1], grid1.nodes2D)
        main()

    if usrResponse == 'e' or usrResponse == 'E':
        print("\nExiting")
        exit()


# Calls main().
if __name__ == '__main__':
    main()
