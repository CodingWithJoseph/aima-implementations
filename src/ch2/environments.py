import copy
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

class GridEnvironment(Environment):

    def __init__(self, squares, agent_location):
        self.squares = squares
        self.agent_location = agent_location

    def percept(self):
        raise NotImplementedError

    def apply_action(self, action):
        raise NotImplementedError

    def step(self, agent):
        percept = self.percept()
        action = agent.step(percept)
        self.apply_action(action)
        return action, percept

class GridEnvironment1D(GridEnvironment):
    def __init__(self, squares, agent_location):
        super().__init__(
            squares=squares,
            agent_location=agent_location
        )
        if len(squares) > 0 and isinstance(squares[0], list):
            raise ValueError('Squares must be 1D')

    def percept(self):
        raise NotImplementedError

    def apply_action(self, action):
        if action == 'suck':
            self.squares[self.agent_location] = clean
        elif action == 'left':
            self._move(-1)
        elif action == 'right':
            self._move(1)

    def _move(self, dx):
        self.agent_location = max(0, min(self.agent_location + dx, len(self.squares) - 1))


class FullyObservableGridEnvironment1D(GridEnvironment1D):
    def __init__(self, squares):
        super().__init__(
            squares=squares,
            agent_location=random.randint(0, len(squares) - 1)
        )

    def percept(self):
        return {'location': self.agent_location, 'status': self.squares.copy()}

class PartiallyObservableGridEnvironment1D(GridEnvironment1D):
    def __init__(self, squares):
        super().__init__(
            squares=squares,
            agent_location=random.randint(0, len(squares) - 1)
        )

    def percept(self):
        return {'location': self.agent_location, 'status': self.squares[self.agent_location]}

class GridEnvironment2D(GridEnvironment):
    def __init__(self, squares, agent_location):
        super().__init__(
            squares=squares,
            agent_location=agent_location
        )

    def percept(self):
        raise NotImplementedError

    def apply_action(self, action):
        x, y = self.agent_location
        if action == 'suck':
            self.squares[x][y] = clean
        elif action == 'up':
            self._move(0, -1)
        elif action == 'down':
            self._move(0, 1)
        elif action == 'left':
            self._move(-1, 0)
        elif action == 'right':
            self._move(1, 0)

    def _move(self, dx, dy):
        x, y = self.agent_location
        new_x = max(0, min(x + dx, len(self.squares[0]) - 1))
        new_y = max(0, min(y + dy, len(self.squares) - 1))
        self.agent_location = (new_x, new_y)

class FullyObservableGridEnvironment2D(GridEnvironment2D):
    def __init__(self, squares):
        super().__init__(
            squares,
            (
                random.randint(0, len(squares[0]) - 1),
                random.randint(0, len(squares) - 1)
            )
        )

    def percept(self):
        return {'location': self.agent_location, 'status': copy.deepcopy(self.squares)}

class PartiallyObservableGridEnvironment2D(GridEnvironment2D):
    def __init__(self, squares):
        super().__init__(
            squares,
            (
                random.randint(0, len(squares[0]) - 1),
                random.randint(0, len(squares) - 1)
            )
        )

    def percept(self):
        x, y = self.agent_location
        return {'status': self.squares[x][y]}