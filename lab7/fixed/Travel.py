import copy
from random import choice
from math import radians, sin, cos, sqrt, atan2


class Node:
    def __init__(self, state, parent=None, action=None, cost=0, priority=0):#add priority
        self.state = state
        self.parent = parent  # Parent node
        self.action = action  # Action performed to reach this node
        self.cost = cost  # Cost to reach this node
        self.depth = 0  # Depth of the node, initialized to 0
        self.priority=priority
        if parent is not None:
            self.depth = parent.depth + 1

    def __hash__(self):
        # Hash method to enable the use of nodes as keys in dictionaries or sets
        if isinstance(self.state, list):
            return hash(tuple(map(tuple, self.state)))
        return hash(self.state)

    def __eq__(self, other):
        # Equality method to compare nodes
        return isinstance(other, Node) and self.state == other.state

    def __gt__(self, other):
        # Greater than method to compare nodes
        if isinstance(other, Node):
            return self.cost > other.cost
        else:
            # If 'other' is not a Node, return NotImplemented
            return NotImplemented

    def __repr__(self):
        # String representation of the Node object
        return f"Node(state={self.state}, depth={self.depth})"

class Travel:
    def __init__(self, initial_state, goal_state, state_transition_model, coordinates=(0,0), distances=0, path_cost=0, actions=""):
        self.state = initial_state
        self.goal_state = goal_state
        self.state_transition_model = state_transition_model
        self.coordinates = coordinates
        self.distances = distances
        self.actions = actions
        self.path_cost = path_cost
    def heuristic(self, state, goal_state, method=False):
        # Calculate heuristic distance between two states
        # Use the provided get_cowl_flew_distance function to calculate heuristic estimate
        coordinates = self.state_transition_model[state]['Coordinates']
        goal_coordinates = self.state_transition_model[goal_state]['Coordinates']
        return self.get_cowl_flew_distance(coordinates, goal_coordinates)

  
    def is_goal_test(self, goal_test):
        return goal_test == self.goal_state
    # get the cowl flew distance from the current node to the goal node
    def get_cowl_flew_distance(self, coordinates, goal_coordinates):
   # Get latitude and longitude coordinates for each city
     lat1, lon1 = coordinates
     lat2, lon2 = goal_coordinates
 # Convert latitude and longitude from degrees to radians
     lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
 # Calculate the straight-line distance using Haversine formula
     dlat = lat2 - lat1
     dlon = lon2 - lon1
     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
     c = 2 * atan2(sqrt(a), sqrt(1 - a))
     h = 6371 * c # Radius of the Earth in kilometers
     return h

    def find_empty_position(self, state):
        for i, row in enumerate(state):
            for j, cell in enumerate(row):
                if cell == 0:
                    return i, j
                
    def get_valid_actions(self, state):
        if state not in self.state_transition_model:
            return []
        return self.state_transition_model[state]['Neighbors'].keys()

    
    def apply_action(self, state, action):
        # Check if the action is valid for the current state
        if action not in self.get_valid_actions(state):
            return None  # Invalid action
        
        # Use the action to determine the new state based on the state transition model
        new_states = self.state_transition_model[state]
        for new_state in new_states:
            if new_state == action:  # Assuming 'action' is the desired state to find
                return new_state
        return None 
    def get_valid_actions2(self, state):
      if state not in self.state_transition_model:
        return {}, ()
      state_info = self.state_transition_model[state]
      return state_info.get('Neighbors', {}), state_info.get('Coordinates', ())
    
    def expand_node(self, node):
        state = node.state
        valid_actions = self.get_valid_actions(state)
        valid_neighbors ,coordinates = self.get_valid_actions2(state)
        valid_neighbors_goal ,coordinates_goal = self.get_valid_actions2(self.goal_state)
        child_nodes = []
        
        keys_array = list(valid_neighbors.keys())
        
        for action in keys_array:
            #class gene searcg problem ser fubc        
                    child_state = action
                    
                    g = node.cost + self.path_cost
                    
                    h = self.heuristic(child_state, self.goal_state)
                    pr = g + h      
                    child_node = Node(child_state, parent=node, action=action,  cost=(valid_neighbors[action]+node.cost), priority=pr)#get the cost right here
                    child_nodes.append(child_node)
        return child_nodes
    def expand_node_idA(self, node):
        state = node.state
        valid_actions = self.get_valid_actions(state)
        valid_neighbors ,coordinates = self.get_valid_actions2(state)
       
        child_nodes = []
        
        keys_array = list(valid_neighbors.keys())
        
        for action in keys_array:
                    
                    child_state = action
                    child_node = Node(child_state, parent=node, action=action, cost=node.cost + 1)#get the cost right here
                    child_nodes.append(child_node)
        return child_nodes

  
    def expand_node_bfs(self, node):
        state = node.state
        valid_actions = self.get_valid_actions(state)
        valid_neighbors ,coordinates = self.get_valid_actions2(state)
        valid_neighbors_goal ,coordinates_goal = self.get_valid_actions2(self.goal_state)
        child_nodes = []
        
        keys_array = list(valid_neighbors.keys())
        
        for action in keys_array:
                    
                    child_state = action
                    g = node.cost + self.path_cost
                    
                    h = self.heuristic(child_state, self.goal_state)
                    total_cost = g + h      
                    child_node = Node(child_state, parent=node, action=action, cost=h)#get the cost right here
                    child_nodes.append(child_node)
        return child_nodes

    def get_coordinates(self, state):
        return self.coordinates.get(state)
    
    def get_distance(self, state1, state2):
        return self.distances.get((state1, state2))
    def printNode(self, message, node):
      print("Node Information:")
      print("Message:", message)
      print("State:", node.state)
      if node.parent:
          print("Parent State:", node.parent.state)
      print("Action:", node.action)
      print("Cost:", node.cost)
      print("Depth:", node.depth)
      print("Priority:", node.priority)
    
    # Check if the state has coordinates in the state transition model
      if node.state in self.state_transition_model:
          print("Coordinates:", self.state_transition_model[node.state]['Coordinates'])
          print("Neighbors:", self.state_transition_model[node.state]['Neighbors'])
      else:
        print("Coordinates: N/A")
        print("Neighbors: N/A")
    