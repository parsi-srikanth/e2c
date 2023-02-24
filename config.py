"""
TODO: Add Description

"""
import argparse
import sys

from rich.console import Console
from rich.table import Table
from rich_argparse import RichHelpFormatter

from config.config_battery import set_battery
from config.config_loadbalancer import set_loadbalancer
from config.config_machine import config_machines, print_machines
from config.config_scheduler import set_scheduler
from config.config_task import config_tasks, print_tasks
from config.handle_config_file import read_config, write_config

console = Console()


def header() -> None:
    table = Table(show_header=False, header_style="bold magenta", expand=True)
    table.add_column(
        "E2C Simulator Configuration", justify="center", style="cyan",
        no_wrap=True
    )
    table.add_row(
        "[bold]E2C Simulator Configuration\n"
        "The E2C CLI is useful for configuring the simulation "
        "environment and E2C settings.[/bold]"
    )
    console.print(table)


def argument_parse():
    """
    TODO: Add help message to arguments
    """
    parser = argparse.ArgumentParser(
        prog="config",
        epilog="E2C Configuration Help",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("--tier", default="tier-1")
    parser.add_argument("--add-machine", default=False)
    parser.add_argument("--modify-machine", default=False)
    parser.add_argument("--attr-machine", nargs="+")
    parser.add_argument("--delete-machine", action="store_true")
    parser.add_argument("--machine-names", nargs="+")

    parser.add_argument("--add-task", default=False)
    parser.add_argument("--modify-task", default=False)
    parser.add_argument("--attr-task", nargs="+")
    parser.add_argument("--delete-task", action="store_true")
    parser.add_argument("--task-names", nargs="+")

    parser.add_argument("--set-loadbalancer", action="store_true")
    parser.add_argument("--set-scheduler", action="store_true")

    parser.add_argument("--set-battery", action="store_true")

    args = parser.parse_args()
    return args


def handle_cli(args) -> None:
    """
    Description:
    TODO: Add description
    """
    config = read_config(console)
    if any([args.add_machine, args.modify_machine, args.delete_machine]):
        new_config = config_machines(args, config, console)
        machine_table = print_machines(args.tier, new_config)
        console.print(machine_table)
        write_config(new_config)
    elif any([args.add_task, args.modify_task, args.delete_task]):
        new_config = config_tasks(args, config, console)
        task_table = print_tasks(args.tier, new_config)
        console.print(task_table)
        write_config(new_config)
    elif args.set_loadbalancer:
        new_config = set_loadbalancer(args, config)
        write_config(new_config)
    elif args.set_scheduler:
        new_config = set_scheduler(args, config)
        write_config(new_config)
    elif args.set_battery:
        new_config = set_battery(args, config)
        write_config(new_config)
    else:
        print(f"Invalid Argparse Argument: {args}")
        sys.exit(0)


def main() -> None:
    header()
    args = argument_parse()
    handle_cli(args)


if __name__ == "__main__":
    main()
