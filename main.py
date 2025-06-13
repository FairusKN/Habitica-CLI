import sys

from cache import get_data_with_cache
from config import change_env
from status import get_UserStats
from task import check_task, get_task, getStreak


def main() -> None:
    args = sys.argv[1:]

    if not args or "help" in args or "h" in args:
        print("""
Usage:
  h, help
        Show this help menu

  s, stats, status
        Show player stats

  t, task
        Show player task.
        Use -habit, -daily, -todo To check Task.
        Use

  config
        Change Habitica API-key & UserID

  streak
        See highest and lowest daily streak

  --refresh
        Use this if you want to force fetch from the API.
        Note: This app use 45s/fetch, if you do command in less than 45s it will use cache instead of refetching
        """)
        return

    refresh = "--refresh" in args

    get_data_with_cache(force_refresh=refresh) if refresh else None

    match args[0]:
        case "config":
            change_env()

        case "s" | "stats" | "status":
            get_UserStats()

        case "t" | "task":
            try:
                if args[1] in ["-habit", "-daily", "-todo"]:
                    check_task(type=args[1].split("-")[-1].lower())
                    return

            except IndexError as e:
                print("Error ", e)

            get_task()

        case "streak":
            getStreak()
        case _:
            print("Unknown command. Use help for usage info.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
        exit()
