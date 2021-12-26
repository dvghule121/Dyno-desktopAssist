import os
import random
import json

with open('projects.json', 'r') as f:
    projects = json.load(f)

completed_task = []
remaining_task = []


class Personal_func:
    def __init__(self):
        pass

    @staticmethod
    def project_progress(project_name=''):
        completed_task.clear()
        remaining_task.clear()


        for project in projects['projects']:
            if project_name != '' and project['name'] in project_name:
                completed_task.extend(project['completed'])
                remaining_task.extend(project['todo'])

        print(Personal_func.show_completed(completed_task))
        print(Personal_func.show_remaining(remaining_task))

    @staticmethod
    def show_completed(list_completed):
        completed_task_task = str()
        for task in list_completed:
            completed_task_task = completed_task_task + task + '\n'
        return f'Sir you have completed \n{completed_task_task} '
        completed_task_task = ''

    @staticmethod
    def show_remaining(list_remaining):
        remaining_task_task = str()
        for task in list_remaining:
            remaining_task_task = remaining_task_task + task + '\n'
        return f'Sir\n{remaining_task_task}\nthese task are remaining'
        remaining_task_task = ""

    @staticmethod
    def add_progress(project_name, todo):
        try:
            for project in projects['projects']:
                if project_name != project['name']:
                    projects['projects'].append({
                        "name": project_name,
                        "completed": [],
                        "todo": [todo]
                    })
                    break
                else:
                    project['todo'].append(todo)

        finally:

            with open('projects.json', 'w') as f:
                json.dump(projects, f)

    @staticmethod
    def add_competed(project_name, task):
        try:
            for project in projects['projects']:
                if project_name == project['name']:
                    project['completed'].append(task)
                    break
        finally:
            with open('projects.json', 'w') as f:
                json.dump(projects, f)






Personal_func.add_competed('pbl assignment', 'create note')
print(projects)
