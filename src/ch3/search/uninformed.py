from src.ch3.problems import Node
from src.ch3.search.search import best_first_search
from src.ch3.util import expand, is_cycle

def uniform_cost_search(problem):
    return best_first_search(problem, lambda node: node.cost)

def breadth_first_search(problem):
    node = Node(problem.initial_state)

    if problem.goal_test(node.state):
        return node

    frontier = [node]
    reached = {node.state}
    while frontier:
        node = frontier.pop(0)
        for child in expand(problem,node):
            if problem.goal_test(child.state):
                return child
            if child.state not in reached:
                reached.add(child.state)
                frontier.append(child)
    return None

def depth_first_search(problem):
    node = Node(problem.initial_state)

    if problem.goal_test(node.state):
        return node

    frontier = [node]
    reached = {node.state}
    while frontier:
        node = frontier.pop()
        for child in expand(problem, node):
            if problem.goal_test(child.state):
                return child
            if child.state not in reached:
                reached.add(child.state)
                frontier.append(child)
    return None

def depth_limited_search(problem, limit, cutoff):
    node = Node(problem.initial_state)
    frontier = [node]
    result = None
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        if node.depth > limit:
            result = cutoff
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.append(child)
    return result

def iterative_deepening_search(problem, limit):
    cutoff = 'cutoff'
    for depth in range(limit):
        result = depth_limited_search(problem, depth, cutoff)
        if result != cutoff:
            return result
    return None