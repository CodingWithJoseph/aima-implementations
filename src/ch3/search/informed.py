from src.ch3.search.search import best_first_search


def greedy_best_first_search(problem, heuristic):
    return best_first_search(problem, heuristic)

def astar_search(problem, heuristic):
    return best_first_search(problem, lambda node: node.cost + heuristic(node))

def iterative_deepening_astar_search():
    pass

def recursive_best_first_search():
    pass

def beam_search():
    pass

def weighted_astar_search():
    pass