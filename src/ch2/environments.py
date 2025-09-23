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
        self.agent_location = 0

    def percept(self):
        return {'location': self.agent_location, 'status': self.squares.copy()}

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


class PartiallyObservableVacuumEnvironment(Environment):

    def __init__(self, squares):
        self.squares = squares
        self.agent_location = 0

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

