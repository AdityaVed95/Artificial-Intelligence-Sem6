import copy

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

def main():
    initial_puzzle = create_initial_puzzle()
    goal_puzzle = create_goal_puzzle()
    print("Initial puzzle is :")
    print_puzzle(initial_puzzle)
    print("Goal Puzzle is :")
    print_puzzle(goal_puzzle)
    
    visited_puzzles = []
    
    temp_puzzle1 = copy.deepcopy(initial_puzzle)
    temp_puzzle1[0][1] = 0
    temp_puzzle1[0][0] = 2
    
    temp_puzzle2 = copy.deepcopy(initial_puzzle)
    temp_puzzle2[1][0] = 0
    temp_puzzle2[0][0] = 1
    
    print_puzzle(initial_puzzle)
    print_puzzle(temp_puzzle1)
    print_puzzle(temp_puzzle2)
    
    visited_puzzles.append(temp_puzzle1)
    visited_puzzles.append(temp_puzzle2)
    
    print("Visited:")
    print(visited_puzzles)
    
    temp_puzzle3 = copy.deepcopy(temp_puzzle1)
    temp_puzzle3 [1][1] = 0
    temp_puzzle3 [0][1] = 8
    
    temp_puzzle4 = copy.deepcopy(temp_puzzle1)
    temp_puzzle4 [0][2] = 0
    temp_puzzle4 [0][1] = 3
    
    
    print(temp_puzzle3)
    print(temp_puzzle4)
    
    # if temp puzzle not in visited puzzles then append it: 
    visited_puzzles.append(temp_puzzle3)
    visited_puzzles.append(temp_puzzle4)

    temp_puzzle5 = copy.deepcopy(temp_puzzle2)
    temp_puzzle5 [1][0] = 8
    temp_puzzle5 [1][1] = 0
    
    temp_puzzle6 = copy.deepcopy(temp_puzzle2)
    temp_puzzle6[2][0] = 0
    temp_puzzle6[1][0] = 7
    
    print("Now:")
    print(temp_puzzle5)
    print(temp_puzzle6) 

    
    
    


if __name__ == "__main__":
    main()




