"""
nexus.config
~~~~~~~~~~~~

Global configuration for the NEXUS system.
"""

from dataclasses import dataclass


@dataclass
class NexusConfig:
    """Configuration for a NEXUS instance."""

    # Memory
    memory_capacity: int = 10_000
    memory_decay_rate: float = 0.01

    # Reasoning
    max_reasoning_depth: int = 50
    min_confidence_threshold: float = 0.3

    # Learning
    learning_rate: float = 0.01
    enable_continuous_learning: bool = True

    # System
    device: str = "cpu"
    verbose: bool = False


# Default configuration
DEFAULT_CONFIG = NexusConfig()
