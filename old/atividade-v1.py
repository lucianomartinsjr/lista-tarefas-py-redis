import redis

class GerenciadorTarefas:
    def __init__(self):
        self.redis_db = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def adicionar_tarefa(self, descricao):
        task_id = len(self.redis_db.keys()) + 1
        self.redis_db.set(task_id, descricao)
        return task_id

    def listar_tarefas(self):
        tasks = []
        for key in self.redis_db.keys():
            task = {'ID': key, 'Descrição': self.redis_db.get(key)}
            tasks.append(task)
        return tasks

    def remover_tarefa(self, task_id):
        if self.redis_db.exists(task_id):
            self.redis_db.delete(task_id)
            return True
        return False

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            task_id = gerenciador.adicionar_tarefa(descricao)
            print(f"Tarefa adicionada com ID: {task_id}")

        elif escolha == '2':
            tarefas = gerenciador.listar_tarefas()
            for tarefa in tarefas:
                print(tarefa)

        elif escolha == '3':
            task_id = input("Digite o ID da tarefa a ser removida: ")
            if gerenciador.remover_tarefa(task_id):
                print("Tarefa removida com sucesso.")
            else:
                print("Tarefa não encontrada.")

        elif escolha == '4':
            break
