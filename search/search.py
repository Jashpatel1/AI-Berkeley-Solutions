# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # A visited set stores the visited states
    visited = set()
    if(problem.isGoalState(problem.getStartState())):
        return []
    s = problem.getStartState()
    # A stack(DFS) to store state and its corresponding path
    st = util.Stack()
    # A list to store path to the current state being worked upon
    Ans = []
    st.push([s, Ans])

    while st.isEmpty() == False:
        x, y = st.pop()
        if problem.isGoalState(x) == True:
            return y
        else:
            if (x in visited) == True:
                continue
            else:
                visited.add(x)
                for i, j, k in problem.getSuccessors(x):
                    if (i in visited) == True:
                        continue
                    else:
                        # Cocatenate the path to the sucessor node with path to its parent
                        st.push([i, y + [j]])

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # A visited set stores the visited states
    visited = set()
    if(problem.isGoalState(problem.getStartState())):
        return []
    s = problem.getStartState()
    # A queue(BFS) to store state and its corresponding path
    que = util.Queue()
    # A list to store path to the current state being worked upon
    Ans = []
    que.push([s, Ans])

    while que.isEmpty() == False:
        x, y = que.pop()
        if problem.isGoalState(x) == True:
            return y
        else:
            if (x in visited) == True:
                continue
            else:
                visited.add(x)
                for i, j, k in problem.getSuccessors(x):
                    if (i in visited) == True:
                        continue
                    else:
                        # Cocatenate the path to the sucessor node with path to its parent
                        que.push([i, y + [j]])

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # A visited set stores the visited states
    visited = set()
    if(problem.isGoalState(problem.getStartState())):
        return []
    s = problem.getStartState()
    # A Priority Queue(UCS) to store state and its corresponding path,
    # where priority being the cost of the path
    pq = util.PriorityQueue()
    # A list to store path to the current state being worked upon
    Ans = []
    Cost = 0
    pq.push([s, Ans, Cost], Cost)

    while pq.isEmpty() == False:
        x, y, z = pq.pop()
        if problem.isGoalState(x) == True:
            return y
        else:
            if (x in visited) == True:
                continue
            else:
                visited.add(x)
                for i, j, k in problem.getSuccessors(x):
                    if (i in visited) == True:
                        continue
                    else:
                        # Cocatenate the path to the sucessor node with path to its parent,
                        # and the cost of current state to the cost of the path
                        pq.push([i, y + [j], z + k], z + k)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # A visited set stores the visited states
    visited = set()
    if(problem.isGoalState(problem.getStartState())):
        return []
    s = problem.getStartState()
    # A Priority Queue(UCS) to store state and its corresponding path,
    # where priority being the heuristic function
    pq = util.PriorityQueue()
    # A list to store path to the current state being worked upon
    Ans = []
    pq.push([s, Ans, heuristic(s, problem)], heuristic(s, problem))

    while pq.isEmpty() == False:
        x, y, z = pq.pop()
        if problem.isGoalState(x) == True:
            return y
        else:
            if (x in visited) == True:
                continue
            else:
                visited.add(x)
                for i, j, k in problem.getSuccessors(x):
                    if (i in visited) == True:
                        continue
                    else:
                        # Cocatenate the path to the sucessor node with path to its parent,
                        # the cost of current state to the cost of the path, and update the heuristic
                        pq.push([i, y + [j], heuristic(i, problem) + problem.getCostOfActions(
                            y + [j])], heuristic(i, problem) + problem.getCostOfActions(y + [j]))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
