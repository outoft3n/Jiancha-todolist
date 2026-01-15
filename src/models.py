"""Data models for the To-Do List application."""

from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import Optional
import uuid


class Priority(Enum):
    """Enum for to-do item priority levels."""

    HIGH = "HIGH"
    MID = "MID"
    LOW = "LOW"


class Status(Enum):
    """Enum for to-do item status."""

    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


@dataclass
class TodoItem:
    """Represents a to-do item in the application.

    Attributes:
        id: Unique identifier for the to-do item (UUID).
        title: The title of the to-do item.
        details: Additional details about the to-do item.
        priority: Priority level (HIGH, MID, or LOW).
        status: Current status (PENDING or COMPLETED).
        owner: Username of the to-do item owner.
        created_at: ISO-8601 timestamp of creation.
        updated_at: ISO-8601 timestamp of last update.
    """

    title: str
    details: str
    priority: Priority
    status: Status
    owner: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        """Convert TodoItem to a dictionary for JSON serialization.

        Returns:
            Dictionary representation of the TodoItem.
        """
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details,
            "priority": self.priority.value,
            "status": self.status.value,
            "owner": self.owner,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TodoItem":
        """Create a TodoItem instance from a dictionary.

        Args:
            data: Dictionary containing to-do item data.

        Returns:
            TodoItem instance.
        """
        return cls(
            id=data["id"],
            title=data["title"],
            details=data["details"],
            priority=Priority(data["priority"]),
            status=Status(data["status"]),
            owner=data["owner"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
        )
