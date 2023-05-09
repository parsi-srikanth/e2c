"""
TODO: Add description

"""
from rich.prompt import Prompt


def set_scheduler(args, config):
    methods = config['system parameters']['scheduler']['methods']
    if args.set_scheduler:
        lb_method = Prompt.ask('[bold green]scheduler method[/bold green]',
                               choices=methods)

        config['system parameters']['scheduler']['used'] = lb_method
    return config
