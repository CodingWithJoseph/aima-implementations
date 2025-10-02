from typing import Any, Set, List, Optional


class BeliefStateAgent:
    pass

def sensorless_search() -> Optional[List[Any]]:
    """Search in belief-state space for sensorless problems."""
    raise NotImplementedError


def belief_state_and_or_search() -> Optional[Any]:
    """AND-OR search in belief-state space."""
    raise NotImplementedError


def predict() -> Set[Any]:
    """Prediction stage of belief state update (Equation 4.4/4.5)."""
    raise NotImplementedError


def possible_percepts() -> Set[Any]:
    """Compute possible percepts from belief state."""
    raise NotImplementedError


def update() -> Set[Any]:
    """Update belief state given percept (Equation 4.5)."""
    raise NotImplementedError