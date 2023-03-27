"""
TODO: Add description

"""

from task.task_status import TaskStatus
from loadbalancer.base_loadbalancer import BaseLoadBalancer
import config.config as config
from event import Event, EventTypes
import time
import numpy as np

class MEET(BaseScheduler):
    

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self._name: str = 'MEET'
        self._sleep_time: float = 0.1
        if total_no_of_tasks > 0:
            self._total_no_of_tasks = total_no_of_tasks
        else:
            raise ValueError('total no of tasks cannot be'
                             'a negative value') 
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def total_no_of_tasks(self):
        return self._total_no_of_tasks
    
    @total_no_of_tasks.setter
    def total_no_of_tasks(self, total_no_of_tasks):
        if not isinstance(total_no_of_tasks, int):
            raise TypeError('total no of tasks must be a' 
                            'integer value')
        elif total_no_of_tasks < 0:
            raise ValueError('total no of tasks cannot be'
                             'a negative value')
        self._total_no_of_tasks = total_no_of_tasks

    @property
    def sleep_time(self):
        return self._sleep_time

    @sleep_time.setter
    def sleep_time(self, sleep_time):
        if not isinstance(sleep_time, float):
            raise TypeError('sleep time must be a float value')
        elif sleep_time < 0:
            raise ValueError('sleep time cannot be a negative value')
        self._sleep_time = sleep_time
        

    def decide(self):
        self.gui_machine_log = []
        
        if config.settings['verbosity'].equals(Verbosity.INFO):
            s = f'\n Current State @{config.time.gct()}'
            s = '\nBQ = '
            bq = [t.id for t in self.queue.list]
            s += f'{bq}'
            s += '\n\nMACHINES ==>>>'
            for m in config.machines:
                s += f'\n\tMachine {m.type.name} :'
                if m.running_task:
                    r = [m.running_task[0].id]
                else:
                    r = []
                mq = [t.id for t in m.queue.list]
                r.append(mq)
                s +=f'\t{r}'
            config.log.write(s)

        
        if not self.queue.empty():
            task = self.choose()
            ties = []
            eets = [[task.estimated_time[m.type.name],m.id] for m in config.machines]
            min_eet = min(eets, key=lambda x:x[0])[0]
            eets = np.array(eets)            
            ties = eets[eets[:,0] == min_eet]
            np.random.seed(task.id)
            assigned_machine_idx = int(np.random.choice(ties[:,1]))            
            assigned_machine = config.machines[assigned_machine_idx]
            
            self.map(assigned_machine)
            s = f"\ntask:{task.id}  assigned to:{assigned_machine.type.name}  delta:{task.deadline}"
            config.log.write(s)                  
            return assigned_machine