from abc import ABC


class Problem(ABC):
    def __init__(self, state_space, initial_state, goal=None):
        self.state_space = state_space
        self.initial_state = initial_state
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        raise NotImplementedError

    def action_cost(self, state1, action, state2):
        raise NotImplementedError


class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def path(self):
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))

    def solution(self):
        return [node.action for node in self.path()[1:]]
