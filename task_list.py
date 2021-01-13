tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

uncompleted_list = []
completed_list = []
task_descriptions = []
time_tasks = []

def uncompleted_tasks(task_list):
    for task in task_list:
        if task["completed"] == False:
            uncompleted_list.append(task)

uncompleted_tasks(tasks)

print(uncompleted_list)

def completed_tasks(task_list):
    for task in task_list:
        if task["completed"] == True:
            completed_list.append(task)

completed_tasks(tasks)

print(completed_list)

def task_description(task_list):
    for task in task_list:
        task_descriptions.append(task["description"])

task_description(tasks)

print(task_descriptions)

def given_time(task_list, time):
    for task in task_list:
        if time <= task["time_taken"]:
            time_tasks.append(task)

given_time(tasks, 10)

print(time_tasks)

def given_description(task_list, provided_description):
    for task in task_list:
        if provided_description == task["description"]:
            print(task)
    return "Not Found"

given_description(tasks, "Make Dinner")

def update_completion(task_list, completed_task):
    for task in task_list:
        if completed_task == task["description"]:
            task["completed"] = True
      

update_completion(tasks, "Feed Cat")
print(tasks[3])

def add_task(description_given, completed_given, time_taken_given):
    tasks.append({
        "description": description_given,
        "completed": completed_given,
        "time_taken": time_taken_given
    })
add_task("Shower", True, 20)
print(tasks)