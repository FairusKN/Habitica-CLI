import sys

from status import get_UserStats

# from streaks import asd
from task import check_task, get_task


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

  streak

        """)
        return

    match args[0]:
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

        case _:
            print("Unknown command. Use help for usage info.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
