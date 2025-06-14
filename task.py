from collections import defaultdict

from cache import get_data_with_cache
from logger import log
from constant import TASKS_URL, HABITICA_API_BASE

data = get_data_with_cache(
    endpoint_name="task_data", url=f"{TASKS_URL}/user"
)

task = defaultdict(list)

for i in data:
    key = i["type"]
    task[key].append(i)

task = dict(task)


def get_task():
    for i in task:
        log.info(f"Type : {i.title()}")
        for a, j in enumerate(task[i], start=1):
            if i.lower() != "habit":
                log.info(
                    f"{a}. {j['text']} {'✅' if j.get('completed') else '❌'} {f'  -  {j.get("streak")}' if i.lower() == 'daily' else ''}"
                )
            else:
                log.info(f"{a}. {j['text']}  -  {j['counterUp']}")

            checklist = j.get("checklist", [])

            if checklist:
                log.info("  Checklist:")
                for item in checklist:
                    log.info(
                        f"    - {item['text']} (✅)"
                        if item.get("completed")
                        else f"    - {item['text']} (❌)"
                    )
            print("")
        print("")


def check_task(type: str = "daily"):
    """
    Checked a task based on Type
    """

    log.info(type.title())

    #Loop trough the data to get the task
    for j, i in enumerate(task[type.lower()], start=1):
        checklist = i.get("checklist")

        log.info(f"{j}. {i["text"]}" )

        #Loop a checklist then print it if there is any checklist
        if checklist:
            for j in checklist:
                log.info(
                    f"    [{'✅' if j.get('completed') else '❌'}]  {j['text'].title()}"
                )

        print("")

    try:
        choice = int(input("Choice (e.g. 1, 2): "))
    except ValueError:
        log.error("Invalid Input ")
        return

    import requests

    from header import headers

    selected_task = (
        task[type.lower()][choice - 1]
        if 0 < choice <= len(task[type.lower()])
        else None
    )
    if not selected_task:
        log.error("Invalid task choice.")
        return

    checklist = selected_task.get("checklist", [])

    #If there is no checklist in task will outomatically post
    if not checklist:
        url = f"{TASKS_URL}/{selected_task['_id']}/score/up"
        response = requests.post(url, headers=headers)
    else:
        checklist_ids = []

        #Loop trough checklist then append the id
        for index, item in enumerate(checklist, start=1):
            log.info(
                f"    {index}. [{'✅' if item.get('completed') else '❌'}]  {item['text'].title()}"
            )
            checklist_ids.append(item["id"])

        #Input for checklist
        try:
            print("")
            choice_input = input("Checklist choice (default=1): ").strip()
            checklist_choice = int(choice_input) if choice_input.isdigit() else 1
        except ValueError:
            log.error("Invalid Input ")
            return

        # Check if the input for checklist is valid then request POST
        if 0 < checklist_choice <= len(checklist_ids):
            selected_checklist = checklist_ids[checklist_choice - 1]
            url = f"{TASKS_URL}/{selected_task['_id']}/checklist/{selected_checklist}/score"
            response = requests.post(url, headers=headers)
        else:
            log.error("Invalid checklist choice.")
            return

    code = response.status_code
    if code == 200:
        log.info("✅ Updated successfully.")
    else:
        log.error(f"❌ Error {code}.")


def getStreak():
    daily_high = ["", 0]
    daily_low = ["", 100]

    #Loop trough streak in daily type to append the score and the task
    for i in task["daily"]:
        current_streak = [i.get("text"), i.get("streak")]

        if current_streak[-1] > daily_high[-1]:
            daily_high = current_streak
        elif current_streak[-1] < daily_low[-1]:
            daily_low = current_streak

    print("")
    log.info(f"The Highest Streak : {daily_high[0]} = {daily_high[-1]}")
    log.info(f"The Lowest Streak : {daily_low[0]} = {daily_low[-1]}")
