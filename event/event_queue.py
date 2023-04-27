from collections import deque
from .event import Event


class EventQueue:
    """A priority queue for storing and managing events"""

    def __init__(self):
        self.events = deque()

    def add(self, event):
        """Insert an event into the event queue"""
        if isinstance(event, Event):
            self.events.append(event)

    def pop(self):
        """Remove and return the event with the smallest time"""
        if self.events:
            return self.events.popleft()
        else:
            return None

    def remove(self, event: Event):
        """Remove an event from the event queue"""
        try:
            self.events.remove(event)
        except ValueError:
            pass

    def clear(self):
        """Clear the event queue"""
        self.events.clear()
