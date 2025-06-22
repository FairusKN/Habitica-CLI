import argparse
import logging as log

from .cache import get_data_with_cache
from .constant import TASKS_URL, USER_URL
from .status import get_UserStats
from .task import check_task, get_task, getStreak
from .utils import change_env, get_API_status


def core() -> None:
    """
    Get command from terminal and do a command based on the args.
    """

    # Parser for CLI
    parser = argparse.ArgumentParser(description="Habitica CLI")
    parser.add_argument(
        "command",
        help="Command to run",
        choices=["status", "task", "config", "streak"],
        nargs="?",
    )
    parser.add_argument(
        "-t",
        "--type",
        help="Task type to inspect (only for 'task' command): habit, daily, or todo",
    )
    parser.add_argument("--refresh", action="store_true", help="Force refresh API")
    parser.add_argument("--api", action="store_true", help="Check API availability")
    parser.add_argument("--version", action="version", version="Habitica CLI 0.1.0")

    args = parser.parse_args()

    # Check if API is OK
    if args.api:
        get_API_status()
        return

    # If refresh = True Data will force to fetch a new data from API
    if args.refresh:
        endpoint = "task_data" if args.command == "task" else "user_data"
        url = f"{TASKS_URL}/user" if args.command == "task" else USER_URL

        get_data_with_cache(endpoint_name=endpoint, url=url, force_refresh=True)

    # Mathing command from Parse
    match args.command:
        case "config":
            change_env()

        case "status":
            get_UserStats()

        case "task":
            # If command task has "-type" will check if it one of those three
            if args.type:
                if args.type in ["habit", "daily", "todo"]:
                    check_task(type=args.type)
                    return
            else:
                get_task()
        case "streak":
            getStreak()
        case _:
            log.error("Unknown command. Use -h for usage info.")

    return
