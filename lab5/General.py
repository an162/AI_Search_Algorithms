from collections import deque
from puzzle import EightPuzzle
from lab6.Travel import Node
from lab6.Travel import Travel
# Implement the graph search algorithm
def graph_search(problem, data_struct='fifo'):
    frontier = deque() if data_struct == 'fifo' else []
    explored = []

    # Initialize the frontier using the initial state of the problem
    initial_node = Node(problem.state)
    frontier.append(initial_node)

    while True:
        if not frontier:
            return "failure"
         
        
        if data_struct == 'fifo' :  #bfs
           node= frontier.popleft()
        else:
            node=frontier.pop() #dfs
        problem.printNode(" currently in :", node)
        if problem.is_goal_test(node.state):
            return node  # Solution found

        explored.append(node.state)

        children = problem.expand_node(node)

        for child in children:
            if child.state not in explored and child not in frontier:
                frontier.append(child)
# Initial state of the 8-puzzle (example)
              
initial_state = [
    [1, 2, 3],
    [4, 0, 6],  # 0 represents the empty space
    [7, 5, 8]
]

# Goal state of the 8-puzzle (example)
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # Goal is to reach this configuration
]

# State transition model for the 8-puzzle (actions that can be taken from each state)
state_transition_model = {
    "up": (-1, 0),    # Move the empty space up
    "down": (1, 0),   # Move the empty space down
    "left": (0, -1),  # Move the empty space left
    "right": (0, 1)   # Move the empty space right
}

# Initialize an 8-puzzle object and shuffle it
eight_puzzle = EightPuzzle(initial_state, goal_state, state_transition_model)
eight_puzzle.shuffle()

# Now you can use the graph_search function to solve the shuffled 8-puzzle
solution = graph_search(eight_puzzle, "lifo")
if solution == "failure":
    print("Failed to find a solution.")
else:
    
    eight_puzzle.printNode("Solution found:", solution)



initial_state = "Algiers"
goal_state = "Guelma"

state_transition_model = {
    "Algiers": ["Oran", "Constantine", "Tizi Ouzou", "Bechar", "Setif"],
    "Oran": ["Algiers", "Tlemcen", "Mascara", "Skikda", "Bejaia"],
    "Constantine": ["Algiers", "Annaba", "Setif", "Ghardaia"],
    "Tizi Ouzou": ["Algiers", "Bejaia", "Bouira", "Adrar"],
    "Tlemcen": ["Oran", "Sidi Bel Abbes", "Mascara", "Guelma"],
    "Annaba": ["Constantine", "Guelma", "Skikda", "El Oued"],
    "Bechar": ["Algiers", "Adrar", "Tindouf"],
    "Setif": ["Algiers", "Constantine", "Ghardaia", "El Oued"],
    "Bejaia": ["Oran", "Tizi Ouzou", "Bouira", "Tindouf"],
    "Mascara": ["Oran", "Tlemcen", "Guelma", "El Oued"],
    "Guelma": ["Tlemcen", "Annaba", "Mascara", "Tindouf"],
    "Skikda": ["Oran", "Annaba", "El Oued", "Tindouf"],
    "Ghardaia": ["Constantine", "Setif", "Adrar"],
    "Bouira": ["Tizi Ouzou", "Bejaia", "Tindouf"],
    "Adrar": ["Bechar", "Tizi Ouzou", "Ghardaia"],
    "Tindouf": ["Bechar", "Bejaia", "Guelma", "Skikda", "Bouira"]
}
# Initialize an 8-puzzle object and shuffle it
eight_puzzle = Travel(initial_state, goal_state, state_transition_model)


# Now you can use the graph_search function to solve the shuffled 8-puzzle
solution = graph_search(eight_puzzle, "lifo")
if solution == "failure":
    print("Failed to find a solution.")
else:
    
    eight_puzzle.printNode("Solution found:", solution)

