"""
TODO: Add description

"""
from rich.prompt import Prompt, FloatPrompt, IntPrompt, Confirm
from rich.table import Table
import sys


def config_machines(args, config, console):
    if args.add_machine:
        new_config = add_machine(args, config, console)
    elif args.modify_machine:
        new_config = modify_machine(args, config, console)
    elif args.delete_machine:
        new_config = delete_machine(args, config, console)

    return new_config


def print_machines(tier, config):
    """
    Description:
    TODO: Add description
    """

    machines = config['system parameters']['tiers'][tier]['machines']
    table = Table(show_header=True, header_style="bold bright_yellow",
                  expand=False)
    attrs = config['system parameters']['machine attributes']
    table.add_column("machine", justify="center", style="cyan",
                     no_wrap=True)
    for attr in attrs.keys():
        table.add_column(attr, justify="center", style="cyan",
                         no_wrap=True)
    for key, value in machines.items():
        row = [key] + [str(value[attr]) for attr in attrs.keys()]
        table.add_row(*row)

    return table


def add_machine(args, config, console):
    """
    TODO: Type checking
    """
    machines = config['system parameters']['tiers'][args.tier]['machines']
    attrs = config['system parameters']['machine attributes']
    console.rule('[bold]::: Configured Machines :::[/bold]', style='blue')
    machine_table = print_machines(args.tier, config)
    console.print(machine_table)
    console.rule(f'[bold]::: Adding {args.add_machine} New Machine :::[/bold]',
                 style='blue')
    machine = dict()
    for i in range(int(args.add_machine)):
        name = Prompt.ask('\n[bold green]name[/bold green]',
                          default=f'M{len(machines)+i+1}')
        if name in machines.keys():
            msg = 'A machine with the same name already exists'
            warning_answer = Confirm.ask(f'{msg}. Are you sure to continue?',
                                         default=False)
            if not warning_answer:
                sys.exit(0)
        machine[name] = dict()
        for attr, val in attrs.items():
            if val['type'] == 'float':
                print(machine)
                machine[name][attr] = FloatPrompt.ask(f'[bold green]{attr}'
                                                      f'[/bold green]',
                                                      choices=val['choices'])
            elif val['type'] == 'int':
                machine[name][attr] = IntPrompt.ask(f'[bold green]{attr}'
                                                    f'[/bold green]',
                                                    choices=val['choices'])
            else:
                machine[name][attr] = Prompt.ask(f'[bold green]{attr}'
                                                 f'[/bold green]',
                                                 choices=val['choices'])
    for key, value in machine.items():
        machines[key] = value
    config['system parameters']['tiers'][args.tier]['machines'] = machines
    return config


def modify_machine(args, config, console):
    """
    TODO: Type checking
    """
    machines = config['system parameters']['tiers'][args.tier]['machines']
    tasks = config['system parameters']['tiers'][args.tier]['tasks']
    attrs = config['system parameters']['machine attributes']
    machine_table = print_machines(args.tier, config)
    console.print(machine_table)
    machine_name = args.modify_machine
    try:
        machine = machines[machine_name]
    except KeyError:
        console.print_exception(extra_lines=8, show_locals=True)
        sys.exit(0)

    for attr in args.attr_machine:
        if attr == 'name':
            new_name = Prompt.ask(f'[bold green]{attr}[/bold green]')
            machines[new_name] = machine
            del machines[machine_name]
            for task, value in tasks.items():
                print(value['eet'])
                eet_machine_name = value['eet'].pop(machine_name)
                tasks[task]['eet'].update({new_name: eet_machine_name})
            machine_name = new_name
        elif attr not in attrs.keys():
            raise KeyError(f'Attribute not found: {attr}')
        elif attrs[attr]['type'] == 'float':
            machine[attr] = FloatPrompt.ask(f'[bold green]{attr}[/bold green]')
        elif attrs[attr]['type'] == 'int':
            machine[attr] = IntPrompt.ask(f'[bold green]{attr}[/bold green]')
        else:
            machine[attr] = Prompt.ask(f'[bold green]{attr}[/bold green]')
    machines[machine_name] = machine
    config['system parameters']['tiers'][args.tier]['machines'] = machines
    return config


def delete_machine(args, config, console):
    """
    TODO: Type checking
    """
    machines = config['system parameters']['tiers'][args.tier]['machines']
    machine_table = print_machines(args.tier, config)
    console.print(machine_table)
    for machine in args.machine_names:
        try:
            machines[machine]
        except KeyError as err:
            console.print_exception(show_locals=False)
            print(f"Machine not found in machines config: {err}")
            sys.exit(0)
        del machines[machine]
    config['system parameters']['tiers'][args.tier]['machines'] = machines
    return config
