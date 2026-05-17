"""
nexus.memory
~~~~~~~~~~~~~

Persistent memory system that replaces fixed context windows
with adaptive, prioritized long-term storage.
"""

import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class MemoryEntry:
    """A single memory unit."""
    key: str
    value: Any
    timestamp: float = field(default_factory=time.time)
    access_count: int = 0
    importance: float = 0.5
    tags: List[str] = field(default_factory=list)


class PersistentMemory:
    """
    Adaptive memory store that prioritizes, forgets,
    and recalls information like a human brain.
    """

    def __init__(self, capacity: int = 10_000):
        self.store: Dict[str, MemoryEntry] = {}
        self.capacity = capacity

    def remember(self, key: str, value: Any, importance: float = 0.5, tags: Optional[List[str]] = None) -> None:
        if len(self.store) >= self.capacity:
            self._forget_least_important()
        self.store[key] = MemoryEntry(
            key=key, value=value, importance=importance, tags=tags or []
        )

    def recall(self, key: str) -> Optional[Any]:
        entry = self.store.get(key)
        if entry:
            entry.access_count += 1
            return entry.value
        return None

    def search(self, tag: str) -> List[MemoryEntry]:
        return [e for e in self.store.values() if tag in e.tags]

    def _forget_least_important(self) -> None:
        if not self.store:
            return
        weakest = min(self.store.values(), key=lambda e: e.importance)
        del self.store[weakest.key]
