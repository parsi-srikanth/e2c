"""
TODO: Add description
"""
from abs import ABC, abstractmethod

from clock import Clock


class baseAbsScheduler(ABC):
    """
    TODO: Class description
    """

    def __init__(self, name: str) -> None: #are stats and queue parameters? is name?
        super().__init__()
        self._name = name
        # self._stats =
        # self._queue =

    @property
    def name(self) -> str:
        return self._name    
    
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        self._name = str(name)

    @property
    def stats(self) -> dict:
        return self._stats

    @stats.setter
    def stats(self, stats: dict):
        if not isinstance(stats, dict):
            raise TypeError('Stats must be a dictionary')
        self._stats = stats

    @property
    def queue(self) -> Queue:
        return self._queue
    
    @queue.setter
    def queue(self, queue: Queue):
        if not isinstance(queue, Queue):
            raise TypeError('Queue must be a Queue Type')
        self._queue = queue



    def choose(self) -> Task:
        task = first_arrived_to_mq #fcfs? #does choose func need to know the scheduling method? 
    
    def admit(self, task: Task) -> bool:
    

    def allocate(self, task: Task) -> Machine:
        machine.running = task
        

    def schedule(self, task: Task):  #where does the task come from that gets passed into schedule func?
        task = choose()
        if machine.is_empty():
            machine = allocate(task)
    
    def defer(self, task: Task):
    

    def prune(self) -> [Task]:
        #remove machine's task and all tasks from machine queue?
    
    def is_empty(self) -> bool:
        if machine.running:        #use this if the field "running: Task" on BaseAbsMachine is empty if machine isnt busy?
            return False              #i am unsure how to see if machine is empty
        return True

    def q_completion_time(self) -> float:
    
