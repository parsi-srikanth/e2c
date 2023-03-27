"""
TODO: Add description
"""
from abs import ABC, abstractmethod



class baseAbsLoadBalancer(ABC):
    """
    TODO: Class description
    """

    taskToBeActioned = None

    def __init__(self) -> None:
        super().__init__()
        self.queue = Queue()
        self.name = 'base'
        self.stats = {'drop':[], 'deferred':[], 'cancelled':[], 'mapped':[]}

    def get_stats(self):
        return self.stats
    
    def get_name(self):
        return self.name

    def get_queue(self):
        return self.queue
    
    def isempty(self):
        return self.queue.isempty()
    
    def choose(self, index=0):
        taskToBeActioned = self.queue.get(index)     
        if config.gui.equals('on'):
            self.decision.emit({'type':'choose',
                                'time':config.time.gct(),
                                'where':'simulator: choose',
                                'data': {'task':taskToBeActioned,
                                        'bq_indx': index,
                                        },                                
                                        })
            time.sleep(self.sleep_time)
        if config.settings['verbosity'].equals(Verbosity.INFO):
            s =f'\n{taskToBeActioned.id} selected --> BQ = '
            bq = [t.id for t in self.queue.list]
            s += f'{bq}'
            s += f'\nexecutime: {taskToBeActioned.execution_time}'
            s += f'\testimeated_time{taskToBeActioned.estimated_time}'

            config.log.write(s)
        
        return taskToBeActioned

    def defer(self, task):
        if config.time.gct() > task.deadline:
            self.drop(task)
            return 1
        if config.gui.equals('on'):
            self.decision.emit({'type':'defer',
                            'time':config.time.gct(),
                            'where':'simulator: defer',
                            'data': {'task':task,                                    
                                    },                            
                                    })
            time.sleep(self.sleep_time)
        taskToBeActioned = None
        task.status =  TaskStatus.DEFERRED
        task.no_of_deferring += 1
        self.queue.put(task)
         
        self.stats['deferred'].append(task)

        event_time = config.event_queue.event_list[0].time
        event_type = EventTypes.DEFERRED
        event = Event(event_time, event_type, task)
        config.event_queue.add_event(event)

        if config.settings['verbosity'].equals(Verbosity.INFO):
            s = '\n[ Task({:}),  _________ ]: Deferred       @time({:3.3f})'.format(
            task.id, config.time.gct())
            config.log.write(s)
        self.gui_machine_log.append({"Task id":task.id,"Event Type":"DEFERRED","Time":config.time.gct(), "Type":'task'})

    def drop(self, task):
        taskToBeActioned = None
        task.status = TaskStatus.CANCELLED
        task.drop_time = config.time.gct()
        self.stats['dropped'].append(task) 
        if config.gui.equals('on'):
            self.decision.emit({'type':'cancelled',
                                'time':config.time.gct(),
                                'where':'simulator: drop',
                                'data': {'task':task,                                    
                                        },                               
                                        })
            time.sleep(self.sleep_time)
        if config.settings['verbosity'].equals(Verbosity.INFO):       
            s = '\n[ Task({:}),  _________ ]: Cancelled      @time({:3.3f})'.format(
                task.id, config.time.gct()       )
            config.log.write(s)
        self.gui_machine_log.append({"Task id":task.id,"Event Type":"CANCELLED","Time":config.time.gct(), "Type":'task'})

    def map(self, machine):
        task = taskToBeActioned
        assignment = machine.admit(task)
        if assignment != 'notEmpty':
            task.assigned_machine = machine
            self.stats['mapped'].append(task)
            if config.gui.equals('on'):
                self.decision.emit({'type':'map',
                                'time':config.time.gct(),
                                'where':'scheduler: map',
                                'data': {'task':task,
                                         'assigned_machine':machine,                                    
                                        },
                                        })
                time.sleep(self.sleep_time)
        else:
            self.defer(task)
    
    def prune(self):

        for task in self.queue.list:
            if config.time.gct() > task.deadline:                
                task.status = TaskStatus.CANCELLED
                task.drop_time = config.time.gct()
                self.stats['dropped'].append(task) 
                self.queue.remove(task)
                if config.gui.equals('on'):
                        self.decision.emit({'type':'cancelled',
                                        'time':config.time.gct(),
                                        'where':'scheduler: prune',
                                        'data': {'task':task,                                                                                  
                                                },                                        
                                                })
                        time.sleep(self.sleep_time)
    
    def decide():
        raise NotImplementedError("Please Implement this method")


