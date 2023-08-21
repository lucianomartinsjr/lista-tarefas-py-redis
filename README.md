# Gerenciador de Tarefas usando Redis e Tkinter

Este é um programa Python que implementa um simples gerenciador de tarefas utilizando a biblioteca Redis para armazenamento e a biblioteca Tkinter para a interface gráfica. O programa permite adicionar, listar e remover tarefas, utilizando um banco de dados Redis como backend.

![image](https://github.com/lucianomartinsjr/lista-tarefas-py-redis/assets/78613684/e59f5d63-d695-4205-b0f3-4689fcbb498d)
![image](https://github.com/lucianomartinsjr/lista-tarefas-py-redis/assets/78613684/fa0385ce-c783-43f7-bc08-84b52a5514f2)
![image](https://github.com/lucianomartinsjr/lista-tarefas-py-redis/assets/78613684/011e4c61-fe09-4c4e-815f-8dc5aaaaedff)
![image](https://github.com/lucianomartinsjr/lista-tarefas-py-redis/assets/78613684/af7ebd15-7cac-49f1-847b-05c850b3f9c5)





## Pré-requisitos

Antes de executar o programa, você deve ter o Redis instalado e em execução em seu sistema. Certifique-se de que a biblioteca `redis` também esteja instalada. Você pode instalá-la usando o seguinte comando:

```bash
pip install redis
```

## Como executar o programa

1. Certifique-se de que o Redis esteja em execução.

2. Execute o arquivo `gerenciador_tarefas.py` em um ambiente Python.

```bash
python gerenciador_tarefas.py
```

3. A interface do gerenciador de tarefas será exibida.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

- **Adicionar Tarefa:** Permite adicionar uma nova tarefa. Insira a descrição da tarefa e clique no botão "Confirmar".

- **Listar Tarefas:** Exibe uma lista de todas as tarefas cadastradas. As tarefas são exibidas com seus IDs e descrições.

- **Remover Tarefa:** Permite remover uma tarefa específica. Insira o ID da tarefa a ser removida e clique no botão "Confirmar".

- **Sair:** Fecha o programa.

## Estrutura do Código

- `GerenciadorTarefasRedis`: Classe responsável por interagir com o banco de dados Redis. Ela possui métodos para adicionar, listar e remover tarefas.

- `Interface`: Classe que cria a interface gráfica usando a biblioteca Tkinter. Ela possui métodos para exibir diferentes telas (adicionar, listar, remover) e interagir com o `GerenciadorTarefasRedis`.

- `__main__`: A parte do código que é executada quando o arquivo é iniciado diretamente. Ele cria uma instância da classe `Interface` e inicia o loop principal da interface gráfica.
