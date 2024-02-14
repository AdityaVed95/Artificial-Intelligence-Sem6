import copy
n = 3

# neatly prints the puzzle : 
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)

def create_initial_puzzle():
    initial_puzzle = [ ["#" for i in range(3)] for j in range(3)]

    # 0 represents blank
    initial_puzzle[0][0] = 0
    initial_puzzle[0][1] = 2
    initial_puzzle[0][2] = 3
    initial_puzzle[1][0] = 1
    initial_puzzle[1][1] = 8   
    initial_puzzle[1][2] = 4
    initial_puzzle[2][0] = 7
    initial_puzzle[2][1] = 6
    initial_puzzle[2][2] = 5
    
    return initial_puzzle

def create_goal_puzzle():
    goal_puzzle = [ ["#" for i in range(3)] for j in range(3)]
    
    # 0 represents blank
    goal_puzzle[0][0] = 1
    goal_puzzle[0][1] = 2
    goal_puzzle[0][2] = 3
    goal_puzzle[1][0] = 8
    goal_puzzle[1][1] = 0   
    goal_puzzle[1][2] = 4
    goal_puzzle[2][0] = 7
    goal_puzzle[2][1] = 6
    goal_puzzle[2][2] = 5
    
    return goal_puzzle

# this fxn returns the allowed movements of zeron for a particular puzzle
def get_movements_allowed(puzzle):
    
    i,j = get_position_of_zero(puzzle)
    allowed_movements = ['l','r','u','d']
    
    if i == 0:
        allowed_movements.remove('u')
    
    if i == n-1:
        allowed_movements.remove('d')
    
    if j == 0:
        allowed_movements.remove('l')
    
    if j == n-1:
        allowed_movements.remove('r')
    
    return allowed_movements
    
# this fxn returns the key for a given value in a dictionary
def key_from_value(dictionary,val):
    
    for key, value in dictionary.items():
        if val == value:
            return key
    
    return "key does not exist"

# this fxn returns the position of zero in the puzzle
def get_position_of_zero(puzzle):
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 0:
                return (i,j)
            
def main():
    initial_puzzle = create_initial_puzzle()
    goal_puzzle = create_goal_puzzle()
    print("\nInitial puzzle is :")
    print_puzzle(initial_puzzle)
    print("\nGoal Puzzle is :")
    print_puzzle(goal_puzzle)
    
    print("\nNow calculating the path to go from initial puzzle to goal puzzle using BFS approach: \n")
    
    # flag to break the while True loop : 
    found_goal_puzzle = False
    
    # a dictionary of visited puzzle id as key and visited puzzle as value
    visited_puzzles = {}
    
    # the bfs queue to perform breadth first search:
    bfs_queue = [initial_puzzle]
    
    id_of_puzzle = 0
    
    visited_puzzles[id_of_puzzle] = initial_puzzle
    id_of_puzzle += 1
    
    # dictionary to store the child puzzle id as key and the parent puzzle id as the value: 
    child_puzzle_id_parent_puzzle_id = {}
    
    # to be found : 
    id_of_goal_puzzle = float('inf')
    
    while (True):
        current_puzzle = bfs_queue.pop(0)
        
        # get all the movements that the zero can make
        allowed_movements = get_movements_allowed(current_puzzle)
        
        row_of_zero,column_of_zero = get_position_of_zero(current_puzzle)
        
        # do each movement of zero and check if it gives the goal puzzle:
        for allowed_movement in allowed_movements:
            child_puzzle = copy.deepcopy(current_puzzle)
            if allowed_movement == "r":
                child_puzzle[row_of_zero][column_of_zero] = current_puzzle[row_of_zero][column_of_zero+1]
                child_puzzle[row_of_zero][column_of_zero+1] = 0

            elif allowed_movement == "d":
                child_puzzle[row_of_zero][column_of_zero] = current_puzzle[row_of_zero + 1][column_of_zero]
                child_puzzle[row_of_zero+1][column_of_zero] = 0
            
            elif allowed_movement == "u":
                child_puzzle[row_of_zero][column_of_zero] = current_puzzle[row_of_zero - 1][column_of_zero]
                child_puzzle[row_of_zero-1][column_of_zero] = 0
            
            elif allowed_movement == "l":
                child_puzzle[row_of_zero][column_of_zero] = current_puzzle[row_of_zero][column_of_zero-1]
                child_puzzle[row_of_zero][column_of_zero-1] = 0
            
            # if child puzzle is already visited, don't visit it again, thus this puzzle won't be expanded further. thus this puzzle will never be a parent puzzle of any child puzzle
            if child_puzzle in list(visited_puzzles.values()):
                continue
            
            # add the child puzzle to the dictionary of visited puzzles: 
            visited_puzzles[id_of_puzzle] = child_puzzle
            # technically we should add when we visit that child puzzle, but in the code, we are adding it now since we want to keep track of visited puzzles to avoid revisiting the duplicate puzzles among the child puzzles of the same level
            
            # add the child puzzle id and parent puzzle id to this dictionary ; child_puzzle_id_parent_puzzle_id
            child_puzzle_id_parent_puzzle_id[id_of_puzzle] = key_from_value(visited_puzzles,current_puzzle)
            
            id_of_puzzle += 1
            
            # append the child puzzle to the bfs queue : 
            bfs_queue.append(child_puzzle)
            
            
                
            if child_puzzle == goal_puzzle:
                found_goal_puzzle = True
                print("Found goal puzzle !!!! : ")
                print_puzzle(child_puzzle)
                print()
                break
                
        
        if found_goal_puzzle == True:
            id_of_goal_puzzle = id_of_puzzle - 1
            break
        
    
    print("id of goal puzzle is : ",id_of_goal_puzzle,"\n")
    print("The dictionary mapping of child puzzle id and it's corresponding parent puzzle id is : ",child_puzzle_id_parent_puzzle_id,"\n")
    print("All the visited puzzles id and the corresponding visited puzzles can be represented by the below dictionary : ")
    print(visited_puzzles,"\n\n")
    
    # calculating the order of puzzles from initial to goal : 
    
    opposite_order_of_puzzles_from_goal_to_initial = []
    opposite_order_of_puzzles_from_goal_to_initial.append(id_of_goal_puzzle)
    id_of_child = id_of_goal_puzzle
    id_of_parent = float('inf')
    
    while True:
        id_of_parent = child_puzzle_id_parent_puzzle_id[id_of_child]
        opposite_order_of_puzzles_from_goal_to_initial.append(id_of_parent)
        
        if id_of_parent == 0:
            break
        
        id_of_child = id_of_parent

    order_of_puzzles_from_initial_to_goal = opposite_order_of_puzzles_from_goal_to_initial[::-1]
    print("The order of puzzle id's selected from initial puzzle to goal puzzle is : ")    
    print(order_of_puzzles_from_initial_to_goal,"\n")
        
        
    print("The order of puzzles from initial to final are : \n")
    for puzzle_id in order_of_puzzles_from_initial_to_goal:
        print_puzzle(visited_puzzles[puzzle_id])
        print()
        

if __name__ == "__main__":
    main()
    
    
