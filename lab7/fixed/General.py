from collections import deque
from Travel import Node
from Travel import Travel
#from ucsTravel import Travel
#from ucsTravel import Node
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def append(self, item):
        heapq.heappush(self.elements, (item.cost, item))
    
    def pop(self):
        return heapq.heappop(self.elements)[1]

 
# Implement the graph search algorithm
def graph_search(problem, data_struct='fifo', depth=None, cost_lim=None):
    if data_struct == 'fifo':
        frontier = deque()  
    elif  data_struct == 'lifo' or  data_struct == 'cldfs': #dfs
        frontier =[]
        
    elif data_struct=='ucs' or  data_struct=="A*" or data_struct=="Best First Search" :
        frontier=PriorityQueue()
    explored = set()  # Track explored states using a set

    # Initialize the frontier using the initial state of the problem
    initial_node = Node(problem.state)
    initial_node.priority=0
    if data_struct == "A*":
       initial_node.priority=0
       cost_so_far = {initial_node.state: 0}
       
    elif data_struct == "Best First Search":
        initial_node.priority=problem.heuristic(initial_node.state,problem.goal_state)
    frontier.append(initial_node)
    
  
    while frontier:
        if data_struct == 'fifo' or data_struct == 'lifo':
            node = frontier.popleft() if data_struct == 'fifo' else frontier.pop()
        else:
            node = frontier.pop()  # Use pop operation for PriorityQueue
            problem.printNode("add message",node)
        if problem.is_goal_test(node.state):
            
            return node 
        
        explored.add(node.state)  # Add the current state to the explored set
        
        if depth is None or node.depth < depth or cost_lim is None or node.cost<cost_lim:
            children = problem.expand_node(node)
            for child in children:
                if child.state not in explored:
                    if isinstance(frontier, PriorityQueue):
                        if child not in list(frontier.elements):
                            frontier.append(child)
                    else:
                        if child not in frontier:
                            frontier.append(child)
                    
                    if data_struct=="A*":
                        child.priority= child.cost + problem.heuristic(child.state,problem.goal_state)
                        cost_so_far[child.state] = child.cost
                     
                    elif data_struct == "Best First Search":
                        child.priority= problem.heuristic(child.state, problem.goal_state)
                    
                    explored.add(child.state)  # Add the child state to the explored set
                   
        if depth == node.depth and not problem.is_goal_test(node.state):
            return "failure"
    return "failure"  # No solution found

def cost_limited_depth_first_search(problem, cost_limit):
    result = graph_search(problem, data_struct='lifo', cost_lim=cost_limit)
    if isinstance(result, Node):
        return result
    else:
        return cost_limit


def iterative_deepening_a_star(problem):
    solution = None
    cost_limit = 0
    while solution is None:
        response = cost_limited_depth_first_search(problem, cost_limit)
        if isinstance(response, Node):
            solution = response
        else:
            cost_limit = response
    return solution
initial_state = "Algiers"
goal_state = "Guelma"

state_transition_model = {
    "Algiers": {
        "Neighbors": {"Oran": 450, "Constantine": 320, "Tizi Ouzou": 80, "Bechar": 700, "Setif": 200},
        "Coordinates": (36.7528, 3.0420)
    },
    "Oran": {
        "Neighbors": {"Algiers": 450, "Tlemcen": 200, "Mascara": 150, "Skikda": 550, "Bejaia": 400},
        "Coordinates": (35.6969, -0.6331)
    },
    "Constantine": {
        "Neighbors": {"Algiers": 320, "Annaba": 210, "Setif": 120, "Ghardaia": 600},
        "Coordinates": (36.3650, 6.6147)
    },
    "Tizi Ouzou": {
        "Neighbors": {"Algiers": 80, "Bejaia": 150, "Bouira": 100, "Adrar": 800},
        "Coordinates": (36.7117, 4.0456)
    },
    "Tlemcen": {
        "Neighbors": {"Oran": 200, "Bejaia": 120, "Mascara": 180, "Guelma": 350},
        "Coordinates": (34.8888, -1.3153)
    },
    "Annaba": {
        "Neighbors": {"Constantine": 210, "Guelma": 100, "Skikda": 90, "El Oued": 450},
        "Coordinates": (36.9060, 7.7465)
    },
    "Bechar": {
        "Neighbors": {"Algiers": 700, "Adrar": 100, "Tindouf": 300},
        "Coordinates": (31.6304, -2.2687)
    },
    "Setif": {
        "Neighbors": {"Algiers": 200, "Constantine": 120, "Ghardaia": 300, "El Oued": 500},
        "Coordinates": (36.1869, 5.4175)
    },
    "Bejaia": {
        "Neighbors": {"Oran": 400, "Tizi Ouzou": 150, "Bouira": 250, "Tindouf": 600},
        "Coordinates": (36.7508, 5.0564)
    },
    "Mascara": {
        "Neighbors": {"Oran": 150, "Tlemcen": 180, "Guelma": 400, "El Oued": 550},
        "Coordinates": (35.3984, 0.1401)
    },
    "Guelma": {
        "Neighbors": {"Tlemcen": 350, "Annaba": 100, "Mascara": 400, "Tindouf": 700},
        "Coordinates": (36.4629, 7.4267)
    },
    "Skikda": {
        "Neighbors": {"Oran": 550, "Annaba": 90, "El Oued": 350, "Tindouf": 800},
        "Coordinates": (36.8796, 6.9036)
    },
    "Ghardaia": {
        "Neighbors": {"Constantine": 600, "Setif": 300, "Adrar": 400},
        "Coordinates": (32.4882, 3.6733)
    },
    "Bouira": {
        "Neighbors": {"Tizi Ouzou": 100, "Bejaia": 250, "Tindouf": 650},
        "Coordinates": (36.3724, 3.9007)
    },
    "Adrar": {
        "Neighbors": {"Bechar": 100, "Tizi Ouzou": 800, "Ghardaia": 400},
        "Coordinates": (27.8617, -0.2917)
    },
    "El Oued": {
        "Neighbors": {"Annaba": 450, "Mascara": 550, "Skikda": 350},
        "Coordinates": (33.3564, 6.8631)
    },
    "Tindouf": {
        "Neighbors": {"Bechar": 300, "Bejaia": 600, "Guelma": 700, "Skikda": 800, "Bouira": 650},
        "Coordinates": (27.6706, -8.1476)}}
"""""
# Initialize an 8-puzzle object and shuffle it
eight_puzzle = Travel(initial_state, goal_state, state_transition_model)


# Depth Limited Search (DLS) Function
def depth_limited_search(problem, max_depth):
    
    sol=graph_search(problem,'lifo', max_depth)
     
    if sol is not None:
     return sol
    else:
     return "failed to find solution ooooo"


# Iterative Deepening Search (IDS) Function
def iterative_deepening_search(problem,depth):
    solution = None
    max_depth = 0
    while solution is None or solution=="failure" and max_depth<=depth:
        solution = depth_limited_search(problem, max_depth)
        max_depth += 1
    return solution

# Main code
# Solve the Travel Planning problem using IDS

print("heuristic usage: +++++++++++++++++++++++++++++++++++++++")
solution = graph_search(eight_puzzle,'A*')

# Display solution information
if solution == "failure":
    print("Failed to find a solution.")
else:
    print("Solution Node Cost:", solution.cost)
    print("Number of Steps:", solution.depth)
    print("Depth of Solution Node:", solution.depth)
"""""

# Define the problem instance
problem = Travel(initial_state, goal_state, state_transition_model)

# Solve using A*
solution_astar = graph_search(problem, "A*")


# Display metrics for A* solution
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<A* Solution:")
print("Cost:", solution_astar.cost)
print("prioriry of the solution node:", solution_astar.priority)
print("Number of steps (explored nodes):", solution_astar.depth)
print("Depth of the solution node:", solution_astar.depth)
 
# Solve using Best First Search

solution_best_first_search = graph_search(problem, "Best First Search")
# Display metrics for Best First Search solution
print("\nBest First Search Solution:")
print("Cost:", solution_best_first_search.cost)
print("priority of the solution node:", solution_best_first_search.priority)
print("Number of steps (explored nodes):", solution_best_first_search.depth)
print("Depth of the solution node:", solution_best_first_search.depth)
#
"""""
cost_limit = 1000 # Set your desired cost limit

# Call the cost-limited depth-first search algorithm
result = cost_limited_depth_first_search(problem, cost_limit)

# Check the result
if isinstance(result, Node):
    print("Solution found:", result.state)
    print("Cost of the solution node:", result.cost)
    print("Depth of the solution node:", result.depth)
else:
    print("Cost limit reached:", result)

# Display solution information
solution_node = iterative_deepening_a_star(problem)
#aph_search(problem, data_struct='fifo', depth=None, cost_lim=None):
if isinstance(solution_node, Node):
    print("Solution found:")
    print("Cost of the solution node:", solution_node.cost)
    print("Number of steps (explored nodes) leading to the solution node:", solution_node.depth)
    print("Depth of the solution node:", solution_node.depth)
else:
    print("No solution found within the cost limit.")
   """""