from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent  
        self.action = action  
        self.cost = cost
        if parent is None:
            self.depth = 0  
        else:
            self.depth = parent.depth + 1  

    def __hash__(self):
        if isinstance(self.state, list):
            return hash(tuple(map(tuple, self.state)))
        return hash(self.state)

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __gt__(self, other):
        return self.cost > other.cost
    
class Hospital:
    def __init__ (self, name, location, coordinates, capacity, services):
        self.name = name
        self.location = location
        self.coordinates = coordinates
        self.capacity = capacity
        self.services = services

class AmbulanceRouteProblem:
    def __init__(self, initial_state, goal_state, state_transition_model):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.state_transition_model = state_transition_model

    def get_initial_state(self):
        return Node(self.initial_state)

    def is_goal_state(self, node):
        return node.state == self.goal_state
    
    def possible_moves(self, state):
        moves = []
        for file in self.state_transition_files:
            with open(file, 'r') as f:
                for line in f:
                    parts = line.strip().split(': ')
                    if parts[0] == state:
                        moves.append(parts[1])
        return moves

    """""
    def apply_action(self, state, action):
     if action in self.state_transition_model[state]:
       return action  
     else:
        return None
    """""
    def apply_action(self, state, action):
      return action
    def expand(self, node):
     state = node.state  # Extract the state from the node object
     valid_moves = self.possible_moves(state)
     child_nodes = []
     for action in valid_moves:
        child_state = self.apply_action(state, action)
        child_node = Node(child_state, parent=node, action=action, cost=node.cost + 1)
        child_nodes.append(child_node)
     print("Expanding state:", state)
     print("Valid moves:", valid_moves)
     print("Child states:", [child.state for child in child_nodes])
     return child_nodes

"""
def read_locations( locations_file):
        state_transition_model = {}
        with open(locations_file, 'r') as file:
            for line in file:
                parts = line.strip().split(': Coordinates - (')
                location_name = parts[0]
                coordinates_part = parts[1].split('), Distance - ')
                coordinates = tuple(map(float, coordinates_part[0].split(', ')))
                state_transition_model[location_name] = coordinates
        return state_transition_model
"""

def GraphSearchAlgorithm(Problem, Extra=None):
    data_struct_type = Extra.get('data_struct') if Extra and 'data_struct' in Extra else deque
    if data_struct_type == list:
        frontier = [Problem.get_initial_state()]
    explored_set = set()
    while frontier:
        if data_struct_type == list:
            node = frontier.pop() # FIFO
        if Problem.is_goal_state(node):  
            print("Goal State Reached:")
            print(node.state)
            return node
        explored_set.add(node.state)  # Add the state to the explored set
        children = Problem.expand(node)
        for child_state in children:
            if child_state.state not in explored_set and child_state not in frontier:  
                frontier.append(child_state)  # Append the child state to the frontier
    return None





"""""

state_transition_model = {
    'Algiers': ['Oran', 'Constantine', 'Tizi Ouzou', 'Bechar', 'Setif'],
    'Oran': ['Algiers', 'Tlemcen', 'Mascara', 'Skikda', 'Bejaia'],
    'Constantine': ['Algiers', 'Annaba', 'Setif', 'Ghardaia'],
    'Tizi Ouzou': ['Algiers', 'Bejaia', 'Bouira', 'Adrar'],
    'Tlemcen': ['Oran', 'Sidi Bel Abbes', 'Mascara', 'Guelma'],
    'Annaba': ['Constantine', 'Guelma', 'Skikda', 'El Oued'],
    'Bechar': ['Algiers', 'Adrar', 'Tindouf'],
    'Setif': ['Algiers', 'Constantine', 'Ghardaia', 'El Oued'],
    'Bejaia': ['Oran', 'Tizi Ouzou', 'Bouira', 'Tindouf'],
    'Mascara': ['Oran', 'Tlemcen', 'Guelma', 'El Oued'],
    'Guelma': ['Tlemcen', 'Annaba', 'Mascara', 'Tindouf'],
    'Skikda': ['Oran', 'Annaba', 'El Oued', 'Tindouf'],
    'Ghardaia': ['Constantine', 'Setif', 'Adrar'],
    'Bouira': ['Tizi Ouzou', 'Bejaia', 'Tindouf'],
    'Adrar': ['Bechar', 'Tizi Ouzou', 'Ghardaia'],
    'Tindouf': ['Bechar', 'Bejaia', 'Guelma', 'Skikda', 'Bouira']
}

Problem = AmbulanceRouteProblem('Algiers','Guelma',state_transition_model)
extra = {'data_struct': list}
solution = GraphSearchAlgorithm(Problem, extra)
if solution:
    print("Solution found:")
    path = []
    current_node = solution
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
    print("Path:", path[::-1])
else:
    print("Solution not found")
  
initial_state = 'Hydra Hotel'
goal_state = 'Hôtel Dar El Ikram'
locations_file = 'Hydra Hotel.txt'

state_transition_model = read_locations(locations_file)
for location, info in state_transition_model.items():
        coordinates = info['coordinates']
        distance = info['distance']
        print(f"Location: {location}, Coordinates: {coordinates}, Distance: {distance} meters")

Problem = AmbulanceRouteProblem(initial_state, goal_state, state_transition_model)
extra = {'data_struct': list}
solution = GraphSearchAlgorithm(Problem, extra)
if solution:
    print("Solution found:")
    path = []
    current_node = solution
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
    print("Path:", path[::-1])
else:
    print("Solution not found")
"""
def read_locations(locations_file):
    landmarks = []
    coordinates = []
    distances = []
    
    with open(locations_file, 'r') as file:
        landmark = None
        coord = None
        distance = None
        for line in file:
            line = line.strip()
            if line.startswith("Nearby Landmark:"):
                if landmark is not None:
                    landmarks.append(landmark)
                landmark = line.split(": ")[1]
            elif line.startswith("Coordinates:"):
                coord = tuple(map(float, line.split(": ")[1][1:-1].split(", ")))
            elif line.startswith("Distance:"):
                distance = float(line.split(": ")[1].split()[0])
                landmarks.append(landmark)
                coordinates.append(coord)
                distances.append(distance)
                landmark = None
                coord = None
                distance = None
    
    return landmarks, coordinates, distances

locations_file = 'grande_mosquée_de_alger_nearby.txt'
landmarks, coordinates, distances = read_locations(locations_file)

for landmark, coord, distance in zip(landmarks, coordinates, distances):
    print(f"Location: {landmark}, Coordinates: {coord}, Distance: {distance} meters")
