"""
TODO: Add description

"""
from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm
from rich.table import Table
import sys


def config_tasks(args, config, console):
    if args.add_task:
        new_config = add_task(args, config, console)
    elif args.modify_task:
        new_config = modify_task(args, config, console)    
    elif args.delete_task:
        new_config = delete_task(args, config, console)               
    return new_config


def print_tasks(tier, config):
    """
    Description:
    TODO: Add description
    """
    
    tasks = config['system parameters']['tiers'][tier]['tasks']
    machines = config['system parameters']['tiers'][tier]['machines']
    attrs = config['system parameters']['task attributes']    
    table = Table(show_header=True, header_style="bold bright_yellow", 
                  expand=False)
    table.add_column("task", justify="center", style="cyan", 
                     no_wrap=True)
    for attr in attrs.keys():
        if attr == 'eet':
            for machine in machines:
                table.add_column(f'eet on {machine}', justify="center", 
                                 style="cyan", no_wrap=True)
        else:
            table.add_column(attr, justify="center", style="cyan", 
                             no_wrap=True)        
    for key, value in tasks.items():         
        row = [key] + [str(value[attr]) for attr in attrs if attr != 'eet'] 
        for machine in machines:
            row += [str(value['eet'][machine])]
        table.add_row(*row)

    return table    
    

def add_task(args, config, console):
    """
    TODO: Type checking
    """        
    tasks = config['system parameters']['tiers'][args.tier]['tasks']
    machines = list(config['system parameters']['tiers'][args.tier]
                    ['machines'].keys())
    attrs = config['system parameters']['task attributes']
    console.rule('[bold]::: Configured Tasks :::[/bold]', style='blue')
    task_table = print_tasks(args.tier, config)
    console.print(task_table)
    console.rule(f'[bold]::: Adding {args.add_task} New Task :::[/bold]', 
                 style='blue')    
    task = dict()
    for i in range(int(args.add_task)):        
        name = Prompt.ask('\n[bold green]name[/bold green]', 
                          default=f'T{len(tasks)+i+1}')
        if name in tasks.keys():
            msg = 'A task with the same name already exists'
            warning_answer = Confirm.ask(f'{msg}. Are you sure to continue?', 
                                         default=False)            
            if not warning_answer:
                sys.exit(0)
        task[name] = dict()
        for attr, val in attrs.items():
            if attr == 'eet':
                continue            
            elif val['type'] == 'float':
                task[name][attr] = FloatPrompt.ask(f'[bold green]{attr}'
                                                   f'[/bold green]', 
                                                   choices=val['choices'])
            elif val['type'] == 'int':
                task[name][attr] = IntPrompt.ask(f'[bold green]{attr}' 
                                                 f'[/bold green]', 
                                                 choices=val['choices'])
            else:
                task[name][attr] = Prompt.ask(f'[bold green]{attr}' 
                                              f'[/bold green]', 
                                              choices=val['choices'])
        eet = dict()
        for machine in machines:
            exe_time = FloatPrompt.ask(f'[bold green]EET on {machine}'
                                       f'[/bold green]')
            eet[machine] = exe_time

        task[name]['eet'] = eet
    for key, value in task.items():
        tasks[key] = value
    config['system parameters']['tiers'][args.tier]['tasks'] = tasks    
    return config


def modify_task(args, config, console):
    """
    TODO: Type checking
    """    
    tasks = config['system parameters']['tiers'][args.tier]['tasks']
    machines = config['system parameters']['tiers'][args.tier]['machines']
    attrs = config['system parameters']['task attributes']
    task_table = print_tasks(args.tier, config)
    console.print(task_table)
    task_name = args.modify_task
    try:
        task = tasks[task_name]
    except KeyError:        
        console.print_exception(extra_lines=8, show_locals=True)        
        sys.exit(0)
    
    for attr in args.attr_task:
        if attr == 'name':
            new_name = Prompt.ask(f'[bold green]{attr}[/bold green]')
            tasks[new_name] = task
            del tasks[task_name]
            task_name = new_name    
        elif attr not in attrs.keys():
            raise KeyError(f'Attribute not found: {attr}')        
        elif attr == 'eet':
            eet = dict()
            for machine in machines:
                exe_time = FloatPrompt.ask(f'[bold green]EET on {machine}' 
                                           f'[/bold green]')
                eet[machine] = exe_time
            task['eet'] = eet
        elif attrs[attr]['type'] == 'float':            
            task[attr] = FloatPrompt.ask(f'[bold green]{attr}[/bold green]',
                                         choices=attrs[attr]['choices'])
        elif attrs[attr]['type'] == 'int':
            task[attr] = IntPrompt.ask(f'[bold green]{attr}[/bold green]', 
                                       choices=attrs[attr]['choices'])
        else:
            task[attr] = Prompt.ask(f'[bold green]{attr}[/bold green]', 
                                    choices=attrs[attr]['choices'])
    tasks[task_name] = task
    config['system parameters']['tiers'][args.tier]['tasks'] = tasks   
    return config 


def delete_task(args, config, console):
    """
    TODO: Type checking
    """    
    tasks = config['system parameters']['tiers'][args.tier]['tasks']
    task_table = print_tasks(args.tier, config)
    console.print(task_table)
    for task in args.task_names:
        try:
            tasks[task]
        except KeyError as err:
            console.print_exception(show_locals=False)
            print(f"Task not found in tasks config: {err}")
            sys.exit(0)   
        del tasks[task]
    config['system parameters']['tiers'][args.tier]['tasks'] = tasks    
    return config 
