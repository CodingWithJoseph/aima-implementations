from typing import Any, Callable

def hill_climbing() -> Any:
    """Basic hill climbing search (Figure 4.2)."""
    raise NotImplementedError


def steepest_ascent_hill_climbing() -> Any:
    """Hill climbing that always picks the best neighbor."""
    raise NotImplementedError


def stochastic_hill_climbing() -> Any:
    """Randomly selects from uphill moves."""
    raise NotImplementedError


def first_choice_hill_climbing() -> Any:
    """Generates successors randomly until finding improvement."""
    raise NotImplementedError


def random_restart_hill_climbing() -> Any:
    """Hill climbing with random restarts."""
    raise NotImplementedError


def simulated_annealing() -> Any:
    """Simulated annealing search (Figure 4.5)."""
    raise NotImplementedError


def local_beam_search() -> Any:
    """Local beam search with k states."""
    raise NotImplementedError


def stochastic_beam_search() -> Any:
    """Beam search with probabilistic selection."""
    raise NotImplementedError