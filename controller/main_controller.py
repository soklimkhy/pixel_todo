import json
import os
import sys
from util.path_utils import CONFIG_PATH



def load_tasks():
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
def add_task(task_list, task):
    if task:
        task_list.append(task)
        save_tasks(task_list)
    return task_list

def delete_task(task_list, index):
    if 0 <= index < len(task_list):
        task_list.pop(index)
        save_tasks(task_list)
    return task_list
