"""Unit tests for the models module."""

import pytest
from datetime import datetime
from src.models import TodoItem, Priority, Status


class TestPriority:
    """Test cases for the Priority enum."""

    def test_priority_high_value(self):
        """Test that HIGH priority has correct value."""
        assert Priority.HIGH.value == "HIGH"

    def test_priority_mid_value(self):
        """Test that MID priority has correct value."""
        assert Priority.MID.value == "MID"

    def test_priority_low_value(self):
        """Test that LOW priority has correct value."""
        assert Priority.LOW.value == "LOW"

    def test_priority_from_string(self):
        """Test creating Priority from string value."""
        assert Priority("HIGH") == Priority.HIGH
        assert Priority("MID") == Priority.MID
        assert Priority("LOW") == Priority.LOW

    def test_priority_invalid_value(self):
        """Test that invalid priority raises ValueError."""
        with pytest.raises(ValueError):
            Priority("INVALID")


class TestStatus:
    """Test cases for the Status enum."""

    def test_status_pending_value(self):
        """Test that PENDING status has correct value."""
        assert Status.PENDING.value == "PENDING"

    def test_status_completed_value(self):
        """Test that COMPLETED status has correct value."""
        assert Status.COMPLETED.value == "COMPLETED"

    def test_status_from_string(self):
        """Test creating Status from string value."""
        assert Status("PENDING") == Status.PENDING
        assert Status("COMPLETED") == Status.COMPLETED

    def test_status_invalid_value(self):
        """Test that invalid status raises ValueError."""
        with pytest.raises(ValueError):
            Status("INVALID")


class TestTodoItem:
    """Test cases for the TodoItem class."""

    def test_todo_item_creation(self):
        """Test creating a TodoItem with all required fields."""
        todo = TodoItem(
            title="Test Todo",
            details="Test details",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner="testuser"
        )
        assert todo.title == "Test Todo"
        assert todo.details == "Test details"
        assert todo.priority == Priority.HIGH
        assert todo.status == Status.PENDING
        assert todo.owner == "testuser"

    def test_todo_item_default_id(self):
        """Test that TodoItem generates a unique ID by default."""
        todo1 = TodoItem(
            title="Todo 1",
            details="Details 1",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner="user1"
        )
        todo2 = TodoItem(
            title="Todo 2",
            details="Details 2",
            priority=Priority.LOW,
            status=Status.COMPLETED,
            owner="user2"
        )
        assert todo1.id != todo2.id
        assert len(todo1.id) > 0
        assert len(todo2.id) > 0

    def test_todo_item_custom_id(self):
        """Test creating a TodoItem with a custom ID."""
        custom_id = "custom-uuid-123"
        todo = TodoItem(
            id=custom_id,
            title="Test Todo",
            details="Test details",
            priority=Priority.MID,
            status=Status.PENDING,
            owner="testuser"
        )
        assert todo.id == custom_id

    def test_todo_item_timestamps(self):
        """Test that TodoItem has creation and update timestamps."""
        before = datetime.now()
        todo = TodoItem(
            title="Test Todo",
            details="Test details",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner="testuser"
        )
        after = datetime.now()
        
        # Parse ISO format timestamps
        created = datetime.fromisoformat(todo.created_at)
        updated = datetime.fromisoformat(todo.updated_at)
        
        assert before <= created <= after
        assert before <= updated <= after
        # created_at and updated_at should be very close (within microseconds)
        time_diff = abs((created - updated).total_seconds())
        assert time_diff < 0.001

    def test_todo_item_to_dict(self):
        """Test converting TodoItem to dictionary."""
        todo = TodoItem(
            id="test-123",
            title="Test Todo",
            details="Test details",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner="testuser",
            created_at="2026-01-15T10:00:00",
            updated_at="2026-01-15T11:00:00"
        )
        todo_dict = todo.to_dict()
        
        assert todo_dict["id"] == "test-123"
        assert todo_dict["title"] == "Test Todo"
        assert todo_dict["details"] == "Test details"
        assert todo_dict["priority"] == "HIGH"
        assert todo_dict["status"] == "PENDING"
        assert todo_dict["owner"] == "testuser"
        assert todo_dict["created_at"] == "2026-01-15T10:00:00"
        assert todo_dict["updated_at"] == "2026-01-15T11:00:00"

    def test_todo_item_from_dict(self):
        """Test creating TodoItem from dictionary."""
        data = {
            "id": "test-456",
            "title": "Dict Todo",
            "details": "From dictionary",
            "priority": "MID",
            "status": "COMPLETED",
            "owner": "dictuser",
            "created_at": "2026-01-10T10:00:00",
            "updated_at": "2026-01-15T12:00:00"
        }
        todo = TodoItem.from_dict(data)
        
        assert todo.id == "test-456"
        assert todo.title == "Dict Todo"
        assert todo.details == "From dictionary"
        assert todo.priority == Priority.MID
        assert todo.status == Status.COMPLETED
        assert todo.owner == "dictuser"
        assert todo.created_at == "2026-01-10T10:00:00"
        assert todo.updated_at == "2026-01-15T12:00:00"

    def test_todo_item_roundtrip_serialization(self):
        """Test that TodoItem can be converted to dict and back."""
        original = TodoItem(
            id="test-789",
            title="Roundtrip Todo",
            details="Testing serialization",
            priority=Priority.LOW,
            status=Status.PENDING,
            owner="roundtripuser",
            created_at="2026-01-12T08:00:00",
            updated_at="2026-01-12T09:00:00"
        )
        
        # Convert to dict and back
        todo_dict = original.to_dict()
        restored = TodoItem.from_dict(todo_dict)
        
        assert restored.id == original.id
        assert restored.title == original.title
        assert restored.details == original.details
        assert restored.priority == original.priority
        assert restored.status == original.status
        assert restored.owner == original.owner
        assert restored.created_at == original.created_at
        assert restored.updated_at == original.updated_at

    def test_todo_item_all_priorities(self):
        """Test TodoItem with each priority level."""
        for priority in [Priority.HIGH, Priority.MID, Priority.LOW]:
            todo = TodoItem(
                title=f"Todo with {priority.value} priority",
                details="Test details",
                priority=priority,
                status=Status.PENDING,
                owner="testuser"
            )
            assert todo.priority == priority

    def test_todo_item_all_statuses(self):
        """Test TodoItem with each status."""
        for status in [Status.PENDING, Status.COMPLETED]:
            todo = TodoItem(
                title="Test Todo",
                details="Test details",
                priority=Priority.HIGH,
                status=status,
                owner="testuser"
            )
            assert todo.status == status

    def test_todo_item_empty_title(self):
        """Test creating TodoItem with empty title (should work, validation is elsewhere)."""
        todo = TodoItem(
            title="",
            details="Test details",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner="testuser"
        )
        assert todo.title == ""

    def test_todo_item_empty_owner(self):
        """Test creating TodoItem with empty owner (should work, validation is elsewhere)."""
        todo = TodoItem(
            title="Test Todo",
            details="Test details",
            priority=Priority.HIGH,
            status=Status.PENDING,
            owner=""
        )
        assert todo.owner == ""
