import random
from abc import abstractmethod, ABC

clean = 'clean'
dirty = 'dirty'

class Environment(ABC):

    @abstractmethod
    def percept(self):
        pass

    @abstractmethod
    def apply_action(self, action):
        pass

    @abstractmethod
    def step(self, agent):
        pass

class FullyObservableVacuumEnvironment(Environment):

    def __init__(self, squares):
        self.squares = squares
        height = len(squares)
        width = len(squares[0])
        self.agent_location = (random.randint(0, width - 1), random.randint(0, height - 1))

    def percept(self):
        return {'location': self.agent_location, 'status': self.squares.copy()}

    def apply_action(self, action):
        x, y = self.agent_location
        if action == 'suck':
            self.squares[x][y] = clean
        else:
            if action == 'up' and y > 0:
                self.agent_location = (x, y - 1)
            elif action == 'down' and y < len(self.squares) - 1:
                self.agent_location = (x, y + 1)
            elif action == 'right' and x < len(self.squares[0]) - 1:
                self.agent_location = (x + 1, y)
            elif action == 'left' and x > 0:
                self.agent_location = (x - 1, y)

    def step(self, agent):
        percept = self.percept()
        action = agent.step(percept)
        self.apply_action(action)
        return action, percept


class PartiallyObservableVacuumEnvironment(Environment):

    def __init__(self, squares):
        self.squares = squares
        height = len(squares)
        width = len(squares[0])
        self.agent_location = (random.randint(0, width - 1), random.randint(0, height - 1))

    def percept(self):
        return {'location': self.agent_location, 'status': self.squares[self.agent_location]}

    def apply_action(self, action):
        if action == 'suck':
            self.squares[self.agent_location] = clean
        elif action == 'right' and self.agent_location < len(self.squares) - 1:
            self.agent_location += 1
        elif action == 'left' and self.agent_location > 0:
            self.agent_location -= 1

    def step(self, agent):
        percept = self.percept()
        action = agent.step(percept)
        self.apply_action(action)
        return action, percept

