"""
nexus.learning
~~~~~~~~~~~~~~~

Continuous learning system that allows the model
to evolve with every interaction without re-training.
"""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
import time


@dataclass
class LearningEvent:
    """A single learning interaction."""
    input_data: Any
    feedback: Optional[Any] = None
    timestamp: float = field(default_factory=time.time)
    reward: float = 0.0


class ContinuousLearner:
    """
    Learning engine that updates the model's knowledge base
    in real-time based on interactions and feedback.
    """

    def __init__(self):
        self.history: List[LearningEvent] = []
        self.adapters: Dict[str, Callable] = {}

    def learn(self, event: LearningEvent) -> None:
        """Process a new learning event and update internal state."""
        self.history.append(event)
        for adapter in self.adapters.values():
            adapter(event)

    def register_adapter(self, name: str, fn: Callable) -> None:
        """Register a callback that fires on every learning event."""
        self.adapters[name] = fn

    @property
    def total_interactions(self) -> int:
        return len(self.history)

    @property
    def average_reward(self) -> float:
        if not self.history:
            return 0.0
        return sum(e.reward for e in self.history) / len(self.history)
