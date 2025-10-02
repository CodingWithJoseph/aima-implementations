import heapq
from src.ch3.problems import Node
from src.ch3.util import expand


def best_first_search(problem, evaluator):
    node = Node(problem.initial_state)

    if problem.goal_test(node.state):
        return node

    frontier = []
    reached = {node.state: node}

    heapq.heappush(frontier, (evaluator(node), node))
    while frontier:
        cost, node = heapq.heappop(frontier)
        for child in expand(problem, node):
            if problem.goal_test(child.state):
                return child
            if child.state not in reached or evaluator(child) < evaluator(reached[child.state]):
                reached[child.state] = child
                heapq.heappush(frontier, (evaluator(child), child))
    return None