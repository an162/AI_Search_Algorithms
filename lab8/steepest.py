from Travel import Node
from Travel import Travel
import random
def get_random_neighbor(state, travel_problem):


    valid_actions = travel_problem.get_valid_actions(state)
    random_action = random.choice(list(valid_actions))
    pri=travel_problem.heuristic(random_action,travel_problem.goal_state)
    node = Node(random_action,None,None,0 ,pri)
    return node

def get_best_neighbor(state1,priority, travel_problem):
    best_neighbor_state = None
    best_neighbor_value =priority
    initial = Node(state1,None,None,0,priority)
    neighbors = travel_problem.expand_node(initial)
    initial.priority=1000
    print("neighbors of  ",initial," is : ", neighbors)
    
    for neighbor in neighbors:
       
        if neighbor.priority < initial.priority:
            best_neighbor_state = neighbor.state
            best_neighbor_value = neighbor.priority
            initial.priority=neighbor.priority
    print("-------------------------------------  ", best_neighbor_state,"------",best_neighbor_value)
    return best_neighbor_state , best_neighbor_value

def steepest_ascent_search(travel_problem):
    path=[]
    initial_node = Node(travel_problem.state)
    current_state=initial_node.state
    while current_state!=travel_problem.goal_state:
        best_neighbor_state = None
        best_neighbor_value = float('inf') 
        

        neighbors = travel_problem.expand_node(initial_node)
        
  
        for neighbor in neighbors:
            if neighbor.priority < best_neighbor_value:
                best_neighbor_state = neighbor.state
                best_neighbor_value = neighbor.priority
        
        # If there is no better neighbor, return the current state
        if best_neighbor_value >= travel_problem.heuristic(current_state, travel_problem.goal_state):
            #return current_state
            print("path: ", path)
            path.append(current_state)
        # Update current state to the best neighbor state
        current_state = best_neighbor_state
    return path
        




def stochastic_hill_climbing(travel_problem):
    current_state = travel_problem.state
    current_state_priority = travel_problem.priority
    path=[]
    while True:
        neighbor_state = get_random_neighbor(current_state, travel_problem)
        if neighbor_state is None:  # No valid neighbor state found
            return current_state
        
        # Compare neighbor state value with current state value
        if neighbor_state.priority <= current_state_priority:
            #return current_state  # No better node among children states
            path.append(current_state)
            print("path: ", path)
        else:
            current_state = neighbor_state  # Assign the child node to explore further

    return current_state


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

def local_search(travel_problem, algorithm='steepest'):
    print("New search :")
    initial_node = Node(travel_problem.state)
    current_state = initial_node.state
    current_state_priority=initial_node.priority
    while True:
        
        if algorithm == 'steepest':
            neighbor_state ,best_neighbor_value= get_best_neighbor(current_state,current_state_priority, travel_problem)
        elif algorithm == 'stochastic':
            neighbor_state = get_random_neighbor(current_state, travel_problem)
        else:
            raise ValueError("Invalid algorithm specified.")
        
       # if neighbor_state is None:  # No valid neighbor state found
       #     return current_state
        
       
        if best_neighbor_value <= current_state_priority:
            print("-------------------Current state: ",neighbor_state)
            return neighbor_state  
        else:
            current_state = neighbor_state
            current_state_priority=best_neighbor_value
            print("-------------------Current state: ",current_state)
    return current_state

# Create a Travel instance
travel_problem = Travel(initial_state, goal_state, state_transition_model)

local_maximum_steepest = local_search(travel_problem, algorithm='steepest')
#local_maximum_stochastic = local_search(travel_problem, algorithm='stochastic')

print("Local maximum state (Steepest Ascent):", local_maximum_steepest)
#print("Local maximum state (Stochastic Hill Climbing):", local_maximum_stochastic)


#local_maximum_steepestt = stochastic_hill_climbing(travel_problem)
#print("Local maximum state (Steepest Ascent):", local_maximum_steepestt)