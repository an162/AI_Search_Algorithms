# AI_Search_Algorithms
informed, uninformed, local and adversarial searches are used
dfs, bfs, ids, A*, ucs, hill climbing, minimax...
Minimax: (The MiniMaxAgent represents an AI agent that utilizes the minimax algorithm to play optimally against a human player in a game of Tic-Tac-Toe in lab10)

some of the algorithms used to solve the problems:


Algorithm 1: Depth Limited Search algorithm
Input: P roblem, M ax_depth ;
Output: Solution;
Call DFS algorithm with M ax_depth ;
Explore a node only if it has depth less than M ax_depth ;


Algorithm 2: Iterative Deepening Search algorithm
Input: P roblem, M ax_depth ;
Output: Solution;
Initialize solution to None ;
Initialize M ax_depth;
while solution == None do
solution = Depth_Limited_Search(Problem, M ax_depth);
Increment M ax_depth ;
end


algorithm for Uniform Cost Search:

Uniform Cost Search Algorithm:
Input: Graph G, start node start, goal node goal.
Output: Shortest path from start to goal.
Create an empty priority queue frontier to store nodes to be explored. Initialize it with the start node start and its cost, which is initially 0.
Create an empty set explored to keep track of visited nodes.
While frontier is not empty:
Pop the node current_node with the lowest cost from the frontier.
If current_node is the goal node goal, return the path from start to goal.
Add current_node to the explored set.
Expand current_node by considering all its neighbors:
For each neighbor neighbor of current_node, calculate the cost of reaching neighbor from that node to current_node.
If neighbor is not in the frontier and explored set, add neighbor to the frontier with its calculated cost.
If neighbor is already in the frontier with a higher cost, update its cost to the lower value.
If the frontier becomes empty without reaching the goal node, return failure.
