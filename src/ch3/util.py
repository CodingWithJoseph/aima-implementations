from src.ch3.problems import Node


def expand(problem, node):
    state = node.state
    for action in problem.actions(state):
        successor = problem.result(state, action)
        cost = node.cost + problem.action_cost(state, action, successor)
        yield Node(successor, node, action, cost)

def is_cycle(node):
    ancestor = node.parent
    while ancestor:
        if ancestor.state == node.state:
            return True
        ancestor = ancestor.parent
    return False