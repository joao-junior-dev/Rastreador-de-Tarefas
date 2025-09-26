import sys

def add_task(task):
    pass


def update_task(id_task, name_task, description_task):
    pass

def delete_task(task):
    pass

def list_tasks():
    pass

def list_tasks_done():
    pass

def list_tasks_failed():
    pass

def set_task_in_progress(id_task):
    pass

def task_done(id_task):
    pass

def list_task_in_progress():
    pass

if __name__ == '__main__':
    if sys.argv[1] == 'add':
        add_task(sys.argv[2])
    elif sys.argv[1] == 'update':
        update_task(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'delete':
        delete_task(sys.argv[2])
    elif sys.argv[1] == 'mark-in-progress':
        set_task_in_progress(sys.argv[2])
    elif sys.argv[1] == 'mark-in-done':
        task_done(sys.argv[2])
    elif sys.argv[1] == 'list':
        list_tasks()
    elif sys.argv[1] == 'list' and sys.argv[2] == 'done':
        list_tasks_done()
    elif sys.argv[1] == 'list' and sys.argv[2] == 'failed':
        list_tasks_failed()
    elif sys.argv[1] == 'list' and sys.argv[2] == 'in_progress':
        list_task_in_progress()