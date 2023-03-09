"""
TODO: Add Description
"""
import heapq
from .event import Event

class EventQueue:
    """A priority queue for storing and managing events"""

    def __init__(self):
        self.events:Event = []

    def add(self, event):
        """Insert an event into the event queue"""
        if isinstance(event, Event):
            heapq.heappush(self.events, event)

    def pop(self):
        """Remove and return the event with the smallest time"""
        return heapq.heappop(self.events) if self.events else None

    def remove(self, event:Event):
        """Remove an event from the event queue"""
        try:
            self.events.remove(event)
            heapq.heapify(self.events)
        except ValueError:
            pass

    def clear(self):
        """Clear the event queue"""
        self.events = []