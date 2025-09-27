import json
import sys
import os
from datetime import datetime


def ler_dados():
    ARQUIVO = 'tarefas.json'
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as arq:
            return json.load(arq)
    return {"contador_id": 0, "tarefas": []}


def carrega_dados(tarefas):
    ARQUIVO = 'tarefas.json'

    with open(ARQUIVO, 'w') as arq:
        json.dump(tarefas, arq)


def adiciona_tarefa(tarefa):
    tarefas = ler_dados()
    tarefas["contador_id"] += 1
    tarefas["tarefas"].append({"id": tarefas["contador_id"],
                               "tarefa": tarefa,
                               "status": "ToDo",
                               "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                               "updatedAt": None})
    carrega_dados(tarefas)


def atualizar_tarefa(id, nova_tarefa):
    tarefas = ler_dados()
    for tarefa in tarefas["tarefas"]:
        if tarefa["id"] == id:
            tarefa["tarefa"] = nova_tarefa
            tarefa["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    carrega_dados(tarefas)

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


