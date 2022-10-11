# Gerenciador_tarefas_Django_Python

# Passo 1: Criar e ativar o ambiente virtual do projeto
--> python -m venv venv

# Passo 2: Instalar o Django no ambiente virtual criado (com o ambiente virtual ativado, podemos baixar o Django através do pip):
--> pip install django

# Passo 3: Criar o projeto:
--> django-admin startproject dia_organizado

# Passo 4: Criar o app do projeto:
--> python manage.py startapp tarefas  

# Passo 5: Adicionar na lista de apps instalados presente no arquivo settings.py

INSTALLED_APPS = [
     ....... 
    'tarefas.apps.TarefasConfig', ou 'tarefas' <--------
]

====================================================================================
# Para criar ou montar o gerenciador de tarefas:

# Models: 
- Descrição
- Categoria
- Data da criação
- Opções de status (concluído, pendente e adiado)
- Opções de categoria (concluído, importante e precisa ser feito)

# Views:
- Lista de tarefas
- Concluir
- Excluir
- Adiar
- Editar
- Tarefas concluídas
- Tarefas adiadas
- Mover as tarefas

# Forms:
- Adicionar as tarefas
- Editar as tarefas

# Templates:
- base.html 
- editar_tarefas.html
- tarefas_adiadas.html
- tarefas_concluidas.html
- tarefas_list.html
