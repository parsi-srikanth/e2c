"""
TODO: Add description

"""
from rich.prompt import Prompt


def set_loadbalancer(args, config):
    methods = config['system parameters']['loadbalancer']['methods']
    if args.set_loadbalancer:
        lb_method = Prompt.ask('[bold green]loadbalancer method[/bold green]',
                               choices=methods)
        
        config['system parameters']['loadbalancer']['used'] = lb_method
    return config