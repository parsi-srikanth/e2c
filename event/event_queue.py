"""
TODO: Add description
"""
from event.event import Event
from utils.descriptors import EventList

import heapq


class EventQueue:
    """
    TODO: Add description
    """

    event_list = EventList()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(EventQueue, cls).__new__(cls)
        return cls.instance

    def add(self, event):
        if isinstance(event, Event):
            heapq.heappush(self.event_list, event)

    def pop(self):
        if self.event_list:
            return heapq.heappop(self.event_list)
        else:
            return Event(None, None, None)

    def remove(self, event):
        self.event_list.remove(event)
        heapq.heapify(self.event_list)

    def reset(self):
        self.event_list = EventList()
