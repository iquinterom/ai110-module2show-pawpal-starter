"""PawPal+ system model.

Class skeletons generated from diagrams/uml.mmd.
Attributes and method signatures only -- no scheduling logic yet.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Category(Enum):
    """Type of care task."""

    WALK = "walk"
    FEEDING = "feeding"
    MEDS = "meds"
    ENRICHMENT = "enrichment"
    GROOMING = "grooming"
    OTHER = "other"


class Priority(Enum):
    """How important a task is when time is limited."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Recurrence(Enum):
    """How often a task repeats."""

    DAILY = "daily"
    WEEKLY = "weekly"


@dataclass
class Task:
    """A single care activity for a pet."""

    name: str
    category: Category
    duration_minutes: int
    priority: Priority
    recurrence: Recurrence = Recurrence.DAILY
    preferred_time: str = ""


@dataclass
class Pet:
    """Information about a single pet and its care tasks."""

    name: str
    species: str
    breed: str = ""
    age: int = 0
    needs: list[str] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a care task to this pet."""
        ...


@dataclass
class Owner:
    """The user, their global constraints, and their pets."""

    name: str
    available_minutes: int
    preferences: list[str] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Register a pet under this owner."""
        ...


@dataclass
class PlanEntry:
    """A task placed in a specific time slot within a plan."""

    task: Task
    start_time: str
    end_time: str


@dataclass
class DailyPlan:
    """The generated schedule: what was scheduled, what was skipped, and why."""

    entries: list[PlanEntry] = field(default_factory=list)
    skipped_tasks: list[Task] = field(default_factory=list)
    total_minutes: int = 0
    reasoning: str = ""

    def add_entry(self, entry: PlanEntry) -> None:
        """Add a scheduled task to the plan."""
        ...

    def summary(self) -> str:
        """Return a human-readable summary of the plan."""
        ...


@dataclass
class Planner:
    """Core scheduling engine: turns constraints + tasks into a DailyPlan."""

    def generate_plan(self, owner: Owner, pet: Pet, tasks: list[Task]) -> DailyPlan:
        """Build a daily plan from the owner's constraints and the task list."""
        ...

    def sort_tasks(self, tasks: list[Task]) -> list[Task]:
        """Order tasks (e.g. by priority, then duration) before scheduling."""
        ...

    def explain_reasoning(self, plan: DailyPlan) -> str:
        """Produce a justification for why the plan looks the way it does."""
        ...
