"""
TODO: Add description
"""
import ruamel.yaml
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Confirm
from rich.markdown import Markdown


from config.config_machine import print_machines
from config.config_task import print_tasks


def read_config(console):
    """
    Description:
    TODO: Add description
    """
    with open("config.yaml", 'r') as config_file:
        try:
            yaml = ruamel.yaml.YAML()
            config = yaml.load(config_file)
            return config
        except ruamel.yaml.YAMLError as yaml_err:
            console.print_exception(show_locals=True)
            if hasattr(yaml_err, 'problem_mark'):
                if yaml_err.context is not None:
                    err_msg = (f"{yaml_err.problem_mark}\n{yaml_err.problem}"
                               f" {yaml_err.context}")
                else:
                    err_msg = (f" {yaml_err.problem_mark}\n"
                               f" {yaml_err.problem}")
            else:
                err_msg = "Something went wrong while parsing yaml file"
            print(err_msg)


def write_config(config):
    """
    Description:
    TODO: Add description
    """
    yaml = ruamel.yaml.YAML()
    with open('config.yaml', 'w') as config_file:
        yaml.dump(config, config_file)


def print_other_parameters(tier, config):
    table = Table(show_header=True,
                  header_style="bold bright_yellow",
                  expand=False)
    table.add_column("parameter", justify="left", style="cyan",
                     no_wrap=True)
    table.add_column("value", justify="left", style="cyan",
                     no_wrap=True)
    loadbalancer = config['system parameters']['tiers'].get(
                            tier, {}).get('loadbalancer', {}).get('method')
    scheduler = config['system parameters']['tiers'].get(
        tier, {}).get('scheduler', {}).get('method')
    battery_capacity = config['system parameters']['tiers'].get(
        tier, {}).get('battery', {}).get('capacity')
    table.add_row('loadbalancer', loadbalancer)
    table.add_row('scheduler', scheduler)
    table.add_row('battery capacity', str(battery_capacity))
    return table


def print_config(config, console):
    tiers = config['system parameters']['tiers']

    for tier in tiers:
        machine_table = print_machines(tier, config)
        task_table = print_tasks(tier, config)
        other_table = print_other_parameters(tier, config)
        machine_title = '[bold]:::[/bold]  ' \
            '[bold green]Machines[/bold green]  [bold]:::[/bold]'
        task_title = '[bold]:::[/bold]  ' \
            '[bold green]Tasks[/bold green]  [bold]:::[/bold]'
        other_title = '[bold]:::[/bold]  ' \
            '[bold green]Other Parameters[/bold green]  [bold]:::[/bold]'
        machine_panel = Panel.fit(machine_table, title=machine_title,
                                  padding=1)
        task_panel = Panel.fit(task_table, title=task_title,
                               padding=1)
        other_panel = Panel.fit(other_table, title=other_title, padding=1)
        console.print(machine_panel)
        console.print(task_panel)
        console.print(other_panel)
        is_confirmed_settings = Confirm.ask(
            '[bold green]Do you confirm the settings[/bold green]',
            default=True)

        if not is_confirmed_settings:
            MARKDOWN = """ Follow ```python config.py --help``` to modify
              the simulation environment."""
            md = Markdown(MARKDOWN)
            console.print(md)
