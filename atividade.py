import redis
import tkinter as tk
from tkinter import simpledialog, messagebox

class GerenciadorTarefasRedis:
    def __init__(self):
        self.redis_db = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def adicionar_tarefa(self, descricao):
        tarefa_ids = [int(key) for key in self.redis_db.keys()]
        if tarefa_ids:
            id_tarefa = str(max(tarefa_ids) + 1)
        else:
            id_tarefa = '1'
        
        self.redis_db.set(id_tarefa, descricao)
        return id_tarefa


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

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        
        self.label = tk.Label(root)
        self.gerenciador = GerenciadorTarefasRedis()
        self.menu()

        self.centralizar_janela()
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
    def menu(self):
        self.limpar_frame()

        self.label = tk.Label(self.root, text="Gerenciador de Tarefas", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)


        self.botao_adicionar = tk.Button(self.root, text="Adicionar Tarefa", command=self.show_adicionar_tarefa)
        self.botao_adicionar.pack(pady=10, padx=50, fill=tk.X)

        self.botao_listar = tk.Button(self.root, text="Listar Tarefas", command=self.show_listar_tarefas)
        self.botao_listar.pack(pady=10, padx=50, fill=tk.X)

        self.botao_remover = tk.Button(self.root, text="Remover Tarefa", command=self.show_remover_tarefa)
        self.botao_remover.pack(pady=10, padx=50, fill=tk.X)

        self.sair = tk.Button(self.root, text="Sair", command=self.root.quit, fg="red", bg="lightgray")
        self.sair.pack(pady=20, padx=50, fill=tk.X )


    def show_adicionar_tarefa(self):
        self.limpar_frame()

        self.label = tk.Label(self.root, text="Adicionar Tarefa", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)

        self.descricao_label = tk.Label(self.root, text="Descrição da Tarefa:")
        self.descricao_label.pack()

        self.descricao_entry = tk.Entry(self.root)
        self.descricao_entry.pack(pady=10, padx=50, fill=tk.X)

        self.botao_confirmar = tk.Button(self.root, text="Confirmar", command=self.adicionar_tarefa)
        self.botao_confirmar.pack(pady=10, padx=50, fill=tk.X)

        self.botao_cancelar = tk.Button(self.root, text="Cancelar", command=self.menu, bg="lightgray")
        self.botao_cancelar.pack(pady=5, padx=50, fill=tk.X)
        
    def show_listar_tarefas(self):
        self.limpar_frame()

        self.label = tk.Label(self.root, text="Lista de Tarefas", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)

        self.tarefas_listbox = tk.Listbox(self.root, font=("Helvetica", 12), selectbackground="lightblue")
        self.tarefas_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        tarefas = self.gerenciador.listar_tarefas()

        if tarefas:
            for tarefa in tarefas:
                tarefa_str = f"ID: {tarefa['ID']}, Descrição: {tarefa['Descrição']}"
                self.tarefas_listbox.insert(tk.END, tarefa_str)
        else:
            self.tarefas_listbox.insert(tk.END, "Não há tarefas cadastradas.")

        self.botao_voltar = tk.Button(self.root, text="Voltar ao Menu", command=self.menu, font=("Helvetica", 12), bg="lightgray")
        self.botao_voltar.pack(pady=20, fill=tk.X)
  
    def show_remover_tarefa(self):
      self.limpar_frame()

      self.label = tk.Label(self.root, text="Remover Tarefa", font=("Helvetica", 16, "bold"))
      self.label.pack(pady=20)

      self.remover_label = tk.Label(self.root, text="ID da Tarefa a Remover:")
      self.remover_label.pack()

      self.remover_entry = tk.Entry(self.root)
      self.remover_entry.pack()

      self.botao_confirmar = tk.Button(self.root, text="Confirmar", command=self.remover_tarefa)
      self.botao_confirmar.pack(pady=10, padx=50, fill=tk.X)

      self.botao_cancelar = tk.Button(self.root, text="Cancelar", command=self.menu )
      self.botao_cancelar.pack(pady=5, padx=50, fill=tk.X)

    def adicionar_tarefa(self):
        descricao = self.descricao_entry.get()
        if descricao:
            task_id = self.gerenciador.adicionar_tarefa(descricao)
            messagebox.showinfo("Tarefa Adicionada", f"Tarefa adicionada com ID: {task_id}")
        self.menu()

    def listar_tarefas(self):
        tarefas = self.gerenciador.listar_tarefas()

        if isinstance(tarefas, str): 
            messagebox.showinfo("Lista de Tarefas", tarefas)
        else:
            tarefas_str = "\n".join([f"ID: {tarefa['ID']}, Descrição: {tarefa['Descrição']}" for tarefa in tarefas])
            if tarefas_str:
                messagebox.showinfo("Lista de Tarefas", tarefas_str)
            else:
                messagebox.showinfo("Lista de Tarefas", "Não há tarefas cadastradas.")

    def remover_tarefa(self):
        task_id = self.remover_entry.get()
        if task_id and self.gerenciador.remover_tarefa(task_id):
            messagebox.showinfo("Tarefa Removida", "Tarefa removida com sucesso.")
        else:
            messagebox.showerror("Tarefa não encontrada", "A tarefa com o ID fornecido não foi encontrada.")
        self.menu()
    
    def exibir_tarefas(self):
        tarefas = self.gerenciador.listar_tarefas()
        if tarefas:
            tarefas_window = tk.Toplevel(self.root)
            tarefas_window.title("Lista de Tarefas")

            tarefas_str = "\n".join([f"ID: {tarefa['ID']}, Descrição: {tarefa['Descrição']}" for tarefa in tarefas])
            tarefas_label = tk.Label(tarefas_window, text=tarefas_str)
            tarefas_label.pack()
        else:
            messagebox.showinfo("Lista de Tarefas", "Não há tarefas cadastradas.")
            
    def limpar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def centralizar_janela(self):
        width = 400  # Largura da janela
        height = 300  # Altura da janela

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")                    

if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)
    root.mainloop()
