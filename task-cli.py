import json
import os
from datetime import datetime
import argparse


def ler_dados():
    """devolve um objeto {} com um contador int e uma lista de tarefas []"""

    ARQUIVO = 'tarefas.json'
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as arq:
            return json.load(arq)
    return {"contador_id": 0, "tarefas": []}


def carrega_dados(tarefas):
    """Serializa um objeto python em um arquivo .json no diretório local"""

    ARQUIVO = 'tarefas.json'

    with open(ARQUIVO, 'w') as arq:
        json.dump(tarefas, arq)


def adicionar_tarefa(tarefa):
    """Adiciona uma tarefa na nossa lista de tarefas dentro di nosso arquivo .json local"""

    tarefas = ler_dados()
    tarefas["contador_id"] += 1
    tarefas["tarefas"].append({"id": tarefas["contador_id"],
                               "tarefa": tarefa,
                               "status": "ToDo",
                               "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                               "updatedAt": None})
    carrega_dados(tarefas)
    return tarefas["contador_id"]


def atualizar_tarefa(id, nova_tarefa):
    """Altera o nome de uma tarefa passando o id e o novo nome da tarefa"""

    tarefas = ler_dados()
    for tarefa in tarefas["tarefas"]:
        if tarefa["id"] == id:
            tarefa["tarefa"] = nova_tarefa
            tarefa["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    carrega_dados(tarefas)




def deletar_tarefa(id_tarefa):
    """Exclui uma tarefa do nosso arquivo .json local passando o id como para função"""

    tarefas = ler_dados()
    for indice, tarefa in enumerate(tarefas["tarefas"]):

        if tarefa["id"] == id_tarefa:
            del tarefas["tarefas"][indice]

    carrega_dados(tarefas)

def set_tarefa_concluida_ou_andamento(id, concluida_ou_andamento):
    """Altera o status de uma tarefa para concluída"""

    tarefas = ler_dados()
    for indice, tarefa in enumerate(tarefas["tarefas"]):
        if tarefa["id"] == id:
            tarefas["tarefas"][indice]["status"] = concluida_ou_andamento
    carrega_dados(tarefas)

def listar_tarefas(status):
    """Lista todos os tarefas"""

    tarefas = ler_dados()
    if status == 'all':
        for tarefa in tarefas["tarefas"]:
            print(tarefa)
    elif status == 'concluida':
        for tarefa in tarefas["tarefas"]:
            if tarefa["status"] == "concluida":
                print(tarefa)
    elif status == "ToDo":
        for tarefa in tarefas["tarefas"]:
            if tarefa["status"] == "ToDo":
                print(tarefa)
    elif status == "andamento":
        for tarefa in tarefas["tarefas"]:
            if tarefa["status"] == "andamento":
                print(tarefa)


def main():
    parser = argparse.ArgumentParser(prog="task-cli", description="Task manager cli")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Adicionar
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("task", help="Nome da tarefa")

    # Atualizar
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int, help="Id da tarefa")
    update_parser.add_argument("nova_tarefa", help="Nova tarefa")

    # Deletar
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id_tarefa", help="Id da tarefa")

    # Setar em andamento
    mark_done_parser = subparsers.add_parser("mark_done")
    mark_done_parser.add_argument("id_tarefa", help="Id da tarefa")
    mark_done_parser.add_argument("done-or-progress", help="Marque como 'andamento' ou 'concluida'")

    # Listar tarefas
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("status", nargs="?", choices=["all", "done", "todo", "in-progress"])

    args = parser.parse_args()

    if args.command == "add":
        id_tarefa = adicionar_tarefa(args.task)
        print(f"Output: Task added successfully (ID: {id_tarefa})")
    elif args.command == "update":
        atualizar_tarefa(args.id, args.nova_tarefa)
        print(f"Output: Task updated successfully (ID: {args.id} - {args.nova_tarefa})")
    elif args.command == "delete":
        deletar_tarefa(args.id_tarefa)
        print(f"Output: Task deleted successfully (ID: {args.id_tarefa})")
    elif args.command == "mark-done":
        set_tarefa_concluida_ou_andamento(args.id_tarefa, args.done_or_progress)
        print(f'Output: Task mark done successfully (ID: {args.id_tarefa} - {args.done_or_progress})')
    elif args.command == "list":
        listar_tarefas(args.status)


if __name__ == "__main__":
    main()
