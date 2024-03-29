import copy
from random import choice



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
class Travel:
    def __init__(self, initial_state, goal_state, state_transition_model, coordinates=(0,0), distances=0, path_cost=0, actions=""):
        self.state = initial_state
        self.goal_state = goal_state
        self.state_transition_model = state_transition_model
        self.coordinates = coordinates
        self.distances = distances
        self.actions = actions
        self.path_cost = path_cost

    def is_goal_test(self, goal_test):
        return goal_test == self.goal_state
    
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
       
        child_nodes = []
        
        keys_array = list(valid_neighbors.keys())

        for action in keys_array:
                    
                    child_state = action
                    child_node = Node(child_state, parent=node, action=action, cost=node.cost + 1)
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
    
    # Check if the state has coordinates in the state transition model
      if node.state in self.state_transition_model:
          print("Coordinates:", self.state_transition_model[node.state]['Coordinates'])
          print("Neighbors:", self.state_transition_model[node.state]['Neighbors'])
      else:
        print("Coordinates: N/A")
        print("Neighbors: N/A")
