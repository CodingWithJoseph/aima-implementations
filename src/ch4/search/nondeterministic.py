from typing import List, Optional


class AndNode:
    pass

class OrNode:
    pass


def and_or_search() -> Optional[List]:
    """AND-OR graph search (Figure 4.11)."""
    raise NotImplementedError


def or_search() -> Optional[List]:
    """OR part of AND-OR search (Figure 4.11)."""
    raise NotImplementedError


def and_search() -> Optional[List]:
    """AND part of AND-OR search (Figure 4.11)."""
    raise NotImplementedError


def is_cycle() -> bool:
    """Check if state is in path."""
    raise NotImplementedError