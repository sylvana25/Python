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
    return  [s, s, w, s, w, w, s, w]
def findparent(pos,direc):
    if direc == 'North':
        return (pos[0],pos[1]+1)
    elif direc == 'South':
        return (pos[0],pos[1]-1)
    elif direc == 'West':
        return (pos[0],pos[1]-1)
    elif direc == 'East':
        return (pos[0],pos[1]+1)
    else: 
        return 'Fail'

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
    mystack = util.Stack()
    pastNodes=[]
    state=[problem.getStartState(),[]]
    mystack.push(state)                      #5,5--->getSuccessors--- (4,5),west,1            key:(4,5) value:((5,5),west,1)
    while True:
        if mystack.isEmpty():
            return []
        state=mystack.pop()
        if problem.isGoalState(state[0]):
            print "We reached the goal! Yay!"
            print state[1]
            return state[1]
        if not state[0] in pastNodes:
            pastNodes.append(state[0])
            for successor in problem.getSuccessors(state[0]):
                newNode=[successor[0],state[1]+[successor[1]]]
                mystack.push(newNode)
    """fringe = util.Stack()
    position = problem.getStartState()
    moves = [(position,'aaa')]
    pastspots = []
    fringe.push((position, 'aaa'))

    while True:
        temp = fringe.pop()
        print temp
        if problem.isGoalState(temp[0]):
            return ['South']
        for thing in problem.getSuccessors(temp[0]):
            if thing[0] not in pastspots:
                fringe.push(thing)
        print fringe.list
        pastspots.append(temp[0])
        print moves[len(moves)-1][0]
        while moves[len(moves)-1][0] != findparent(temp[0],temp[1]):
            if moves[len(moves)-1][0] != findparent(temp[0],temp[1]):
                moves.pop()
        moves.append(temp)

        resultlist = []
        for thing in moves:
            if thing[0] != problem.getStartState():
                resultlist.append(thing[1])





        successors = problem.getSuccessors(position)
        if problem.isGoalState(position):
            break
        for thing in successors:
            if not thing[0] in pastspots:
                fringe.push(thing[0]) 
            if len(fringe) == 0:
                return 'Failure


    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    util.raiseNotDefined()"""


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    mystack = util.Queue()
    pastNodes=[]
    state=[problem.getStartState(),[]]
    mystack.push(state)                      #5,5--->getSuccessors--- (4,5),west,1            key:(4,5) value:((5,5),west,1)
    while True:
        if mystack.isEmpty():
            return []
        state=mystack.pop()
        if problem.isGoalState(state[0]):
            print "We reached the goal! Yay!"
            print state[1]
            return state[1]
        if not state[0] in pastNodes:
            pastNodes.append(state[0])
            for successor in problem.getSuccessors(state[0]):
                newNode=[successor[0],state[1]+[successor[1]]]
                mystack.push(newNode)
    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    myqueue = util.PriorityQueue()
    pastNodes=[] 
    state=[problem.getStartState(),[],0]
    myqueue.update(state,0)                      #5,5--->getSuccessors--- (4,5),west,1            key:(4,5) value:((5,5),west,1)
    while True:
        if myqueue.isEmpty():
            return []
        state=myqueue.pop()
        if problem.isGoalState(state[0]): 
            print "We reached the goal! Yay!"
            print state[1]
            return state[1]
        if not state[0] in pastNodes:
            pastNodes.append(state[0])
            for successor in problem.getSuccessors(state[0]):
                cost = successor[2]+state[2]
                newNode=[successor[0],state[1]+[successor[1]],-1*cost]
                
                myqueue.update(newNode,-1*cost)
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    myqueue = util.PriorityQueue()
    pastNodes=[] 
    state=[problem.getStartState(),[],0]
    myqueue.update(state,0)                      #5,5--->getSuccessors--- (4,5),west,1            key:(4,5) value:((5,5),west,1)
    while True:
        if myqueue.isEmpty():
            return []
        state=myqueue.pop()
        if problem.isGoalState(state[0]): 
            print "We reached the goal! Yay!"
            print state[1]
            return state[1]
        if not state[0] in pastNodes:
            pastNodes.append(state[0])
            for successor in problem.getSuccessors(state[0]):
                cost = successor[2]+state[2]+heuristic(state[0],problem)
                newNode=[successor[0],state[1]+[successor[1]],cost]
                
                myqueue.update(newNode, -1*cost)
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
