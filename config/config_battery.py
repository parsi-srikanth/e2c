"""
TODO: Add description

"""
from rich.prompt import FloatPrompt


def set_battery(args, config):
    
    if args.set_battery:
        capacity = FloatPrompt.ask('[bold green]capacity[/bold green]')        
        config['system parameters'
               ]['tiers'
                 ][args.tier
                   ]['battery'
                     ]['capacity'] = capacity
    return config