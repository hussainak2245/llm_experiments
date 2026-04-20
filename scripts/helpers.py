"""Helper utilities for experiment execution and aggregation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class RunResult:
    experiment: int
    dataset: str
    model: str
    language: str
    batch_size: int
    replicate: int
    accuracy: float


def mean_accuracy(results: Iterable[RunResult]) -> float:
    """Return mean accuracy for a collection of run results."""
    values = [r.accuracy for r in results]
    if not values:
        raise ValueError("results cannot be empty")
    return sum(values) / len(values)
