"""
TODO: Add description

"""

from task.task_status import TaskStatus
from loadbalancer.base_loadbalancer import BaseLoadBalancer
import config.config as config
from event import Event, EventTypes
import time

class MM(BaseScheduler):
    

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self._name: str = 'MM'
        self._sleep_time: float = 0.1
        if total_no_of_tasks > 0:
            self._total_no_of_tasks = total_no_of_tasks
        else:
            raise ValueError('total no of tasks cannot be'
                             'a negative value') 
        self.gui_machine_log = []

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
    
    
    def phase1(self):
       
        provisional_map = []
        index = 0     
        self.prune()       
        for task in self.queue.list:
            min_ct = float('inf')
            min_ct_machine = None            
            for machine in config.machines:
                pct = machine.provisional_map(task)              
                if pct < min_ct:
                    min_ct = pct
                    min_ct_machine = machine 
           
        
            provisional_map.append([task, min_ct, min_ct_machine, index])
            index += 1 
        
        return provisional_map
    

    def phase2(self, provisional_map):
        provisional_map_machines = []        
        for machine in config.machines:
            if not machine.queue.full():
                min_ct =float('inf')
                task = None
                index = None
                for pair in provisional_map:                    
                    if pair[2] != None and pair[2].id == machine.id and pair[1] < min_ct:
                        task = pair[0]
                        min_ct = pair[1]
                        index = pair[3]   
                provisional_map_machines.append([task,machine,index])

        return provisional_map_machines



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
        
        provisional_map = self.phase1()
        provisional_map_machines = self.phase2(provisional_map)

        for pair in provisional_map_machines:
            task = pair[0]
            assigned_machine = pair[1]  

            if task != None :
                index = self.queue.list.index(task)                                               
                task = self.choose(index)
                self.map(assigned_machine)
                s = f"\ntask:{task.id}  assigned to:{assigned_machine.type.name}  ec:{pair[2]}   delta:{task.deadline}"
                config.log.write(s)
                return assigned_machine
        return None
