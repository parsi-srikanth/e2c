"""
TODO: Add Description
"""
import heapq

from .event import Event

class EventQueue:
    """  
        All events are queued in EventQueue.
        
        events: It is the list of events in the queue. It has
        Min-heap data structure. It can help sorting the queue based on the
        event.time with reasonable time complexity.
    """

    events = []

    def add(self, event):
        """Insert an event into the events."""
        if isinstance(event, Event):
            heapq.heappush(self.events, event)

    def pop(self):
        """it returns the root of events which is the event with 
        smallest time."""

        if self.events:  # it checks that events is non-empty
            return heapq.heappop(self.events)
        else:
            return Event(None, None, None)

    def remove(self, event):
        """It removes the event from the events. Then, the resulted
        events is heapified again. """
        print(self.events)
        print('\n\n\n')
        self.events.remove(event)
        heapq.heapify(self.events)
    
    def reset(self):
        self.events = []