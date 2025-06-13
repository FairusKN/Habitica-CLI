from collections import defaultdict

from cache import get_data_with_cache

data = get_data_with_cache(
    endpoint_name="task_data", url="https://habitica.com/api/v3/tasks/user"
)

task = defaultdict(list)

for i in data:
    key = i["type"]
    task[key].append(i)

task = dict(task)


def get_task():
    for i in task:
        print("Type : ", i.title())
        for a, j in enumerate(task[i], start=1):
            if i.lower() != "habit":
                print(
                    f"{a}. {j['text']} {'✅' if j.get('completed') else '❌'} {f'  -  {j.get("streak")}' if i.lower() == 'daily' else ''}"
                )
            else:
                print(f"{a}. {j['text']}  -  {j['counterUp']}")

            checklist = j.get("checklist", [])

            if checklist:
                print("  Checklist:")
                for item in checklist:
                    print(
                        f"    - {item['text']} (✅)"
                        if item.get("completed")
                        else f"    - {item['text']} (❌)"
                    )

            print("")

        print("")


def check_task(type: str = "daily"):
    print(type.title())
    for j, i in enumerate(task[type.lower()], start=1):
        checklist = i.get("checklist")

        print(f"{j}.", i["text"])
        if checklist:
            for j in checklist:
                print(
                    f"    [{'✅' if j.get('completed') else '❌'}]  {j['text'].title()}"
                )

        print("")

    try:
        choice = int(input("Choice (e.g. 1, 2): "))
    except ValueError as e:
        print("Invalid Input ", e)
        return

    import requests

    from header import headers

    selected_task = (
        task[type.lower()][choice - 1]
        if 0 < choice <= len(task[type.lower()])
        else None
    )
    if not selected_task:
        print("Invalid task choice.")
        return

    checklist = selected_task.get("checklist", [])

    if not checklist:
        url = f"https://habitica.com/api/v3/tasks/{selected_task['_id']}/score/up"
        response = requests.post(url, headers=headers)
    else:
        checklist_ids = []

        for index, item in enumerate(checklist, start=1):
            print(
                f"    {index}. [{'✅' if item.get('completed') else '❌'}]  {item['text'].title()}"
            )
            checklist_ids.append(item["id"])

        try:
            print("")
            choice_input = input("Checklist choice (default=1): ").strip()
            checklist_choice = int(choice_input) if choice_input.isdigit() else 1
        except ValueError as e:
            print("Invalid Input ", e)
            return

        if 0 < checklist_choice <= len(checklist_ids):
            selected_checklist = checklist_ids[checklist_choice - 1]
            url = f"https://habitica.com/api/v3/tasks/{selected_task['_id']}/checklist/{selected_checklist}/score"
            response = requests.post(url, headers=headers)
        else:
            print("Invalid checklist choice.")
            return

    code = response.status_code
    if code == 200:
        print("✅ Updated successfully.")
    else:
        print(f"❌ Error {code}.")


def getStreak():
    daily_high = ["", 0]
    daily_low = ["", 100]

    for i in task["daily"]:
        current_streak = [i.get("text"), i.get("streak")]

        if current_streak[-1] > daily_high[-1]:
            daily_high = current_streak
        elif current_streak[-1] < daily_low[-1]:
            daily_low = current_streak

    print("")
    print(f"The Highest Streak : {daily_high[0]} = {daily_high[-1]}")
    print(f"The Lowest Streak : {daily_low[0]} = {daily_low[-1]}")
