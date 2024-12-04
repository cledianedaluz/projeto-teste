def menu():
    print("Escolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Ver tarefas")
    print("4. Sair")
    
    escolha = input("Digite sua escolha (1/2/3/4): ")
    
    if escolha == '1':
        task = input("Digite a tarefa que deseja adicionar: ")
        add_task(task)
    elif escolha == '2':
        task = input("Digite a tarefa que deseja remover: ")
        remove_task(task)
    elif escolha == '3':
        view_tasks()
    elif escolha == '4':
        print("Saindo...")
        exit()
    else:
        print("Opção inválida! Tente novamente.")

# Loop do menu
while True:
    menu()
