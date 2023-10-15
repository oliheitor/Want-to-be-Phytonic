import json

# Nomes dos arquivos para persistência
estudantes_file = "estudantes.json"
disciplinas_file = "disciplinas.json"
professores_file = "professores.json"
turmas_file = "turmas.json"
matriculas_file = "matriculas.json"

# Inicializar dados padrão
default_estudantes = []
default_disciplinas = []
default_professores = []
default_turmas = []
default_matriculas = []

# Função para carregar dados de um arquivo ou criar se não existir
def carregar_dados(arquivo, default_data):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Se o arquivo não existe, cria com os dados padrão
        with open(arquivo, 'w') as file:
            json.dump(default_data, file)
        return default_data

# Função para salvar dados em um arquivo
def salvar_dados():
    # Salvar estudantes
    with open(estudantes_file, 'w') as file:
        json.dump(estudantes, file)

    # Salvar disciplinas
    with open(disciplinas_file, 'w') as file:
        json.dump(disciplinas, file)

    # Salvar professores
    with open(professores_file, 'w') as file:
        json.dump(professores, file)

    # Salvar turmas
    with open(turmas_file, 'w') as file:
        json.dump(turmas, file)

    # Salvar matrículas
    with open(matriculas_file, 'w') as file:
        json.dump(matriculas, file)



# Carregar ou criar os arquivos JSON
estudantes = carregar_dados(estudantes_file, default_estudantes)
disciplinas = carregar_dados(disciplinas_file, default_disciplinas)
professores = carregar_dados(professores_file, default_professores)
turmas = carregar_dados(turmas_file, default_turmas)
matriculas = carregar_dados(matriculas_file, default_matriculas)

# Listas
estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

# MENUS
# Função Menu Principal
def menu_principal():
    print("\n--- MENU PRINCIPAL ---\n")
    print("Escolha uma opção:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("\n6. Sair\n")

# Função Menu Operações
def menu_operacoes():
    print("\n--- MENU DE OPERAÇÕES ---\n")
    print("Escolha uma operação:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("\n5. Voltar ao Menu Principal\n")

# FUNÇÕES DE OPERAÇÃO
# Incluir
def incluir(opcao):
    if opcao == estudantes:
        codigo_est = int(input("Digite o código do estudante: "))
        # Verificar se o código do estudante já existe
        for estudante in estudantes:
            if estudante.get("codigo_est") == codigo_est:
                print("O código do estudante já existe. Não é possível adicionar outro estudante com o mesmo código.")
                return  # Retorna da função sem adicionar o estudante
        nome_est = input("Digite o nome do estudante: ")
        cpf_est = input("Digite o CPF do estudante: ")
        estudante = {"codigo_est": codigo_est, "nome_est": nome_est, "cpf_est": cpf_est}
        estudantes.append(estudante)
        print("Estudante incluído com sucesso.")
    elif opcao == disciplinas:
        codigo_dis = int(input("Digite o código da disciplina: "))
        nome_dis = input("Digite o nome da disciplina: ")
        disciplina = {"codigo_dis": codigo_dis, "nome_dis": nome_dis}
        disciplinas.append(disciplina)
        print("Disciplina incluída com sucesso.")
    elif opcao == professores:
        codigo_pro = int(input("Digite o código do professor: "))
        nome_pro = input("Digite o nome do professor: ")
        cpf_pro = input("Digite o CPF do professor: ")
        professor = {"codigo_pro": codigo_pro, "nome_pro": nome_pro, "cpf_pro": cpf_pro}
        professores.append(professor)
        print("Professor incluído com sucesso.")
    elif opcao == turmas:
        codigo_tur = int(input("Digite o código da turma: "))
        # Verificar se o código da turma já existe
        for turma in turmas:
            if turma.get("codigo_tur") == codigo_tur:
                print("O código da turma já existe. Não é possível adicionar turma com o mesmo código.")
                return  # Retorna da função sem adicionar a turma
        codigo_pro = int(input("Digite o código do professor: "))
        codigo_dis = int(input("Digite o código da disciplina: "))
        turma = {"codigo": codigo_tur, "codigo_professor": codigo_pro, "codigo_disciplina": codigo_dis}
        turmas.append(turma)
        print("Turma incluída com sucesso.")
    elif opcao == matriculas:
        codigo_tur = int(input("Digite o código da turma: "))
        codigo_est = int(input("Digite o código do estudante: "))
        # Verificar se a matrícula já existe
        for matricula in matriculas:
            if matricula.get("codigo_tur") == codigo_tur and matricula.get("codigo_est") == codigo_est:
                print("A matrícula já existe. Não é possível adicionar uma matrícula com os mesmos códigos de turma e estudante.")
                return  # Retorna da função sem adicionar a matrícula           
        matricula = {"codigo_turma": codigo_tur, "codigo_estudante": codigo_est}
        matriculas.append(matricula)
        print("Matrícula incluída com sucesso.")

# Listar
def listar(opcao):
    if opcao == estudantes:
        if not estudantes:
                    print("Não há estudantes cadastrados.")
        else:
            print("Lista de estudantes cadastrados:")
            for estudante in estudantes:
                print(f"Código: {estudante['codigo_est']}, Nome: {estudante['nome_est']}, CPF: {estudante['cpf_est']}")
    elif opcao == disciplinas:
        if not disciplinas:
                    print("Não há disciplinas cadastradas.")
        else:
            print("Lista de disciplinas cadastradas:")
            for disciplina in disciplinas:
                print(f"Código: {disciplina['codigo_dis']}, Nome: {disciplina['nome_dis']},")
    elif opcao == professores:
        if not professores:
                    print("Não há professores cadastrados.")
        else:
            print("Lista de professores cadastrados:")
            for professor in professores:
                print(f"Código: {professor['codigo_pro']}, Nome: {professor['nome_pro']}, CPF: {professor['cpf_pro']}")
    elif opcao == turmas:
        if not turmas:
                    print("Não há turmas cadastradas.")
        else:
            print("Lista de turmas cadastradas:")
            for turma in turmas:
                print(f"Código-tur: {turma['codigo_tur']}, Código_pro: {turma['codigo_pro']}, Código_dis: {turma['codigo_dis']}")
    elif opcao == matriculas:
        if not matriculas:
                    print("Não há matrículas cadastradas.")
        else:
            print("Lista de matrículas cadastradas:")
            for matricula in matriculas:
                print(f"Código-tur: {matricula['codigo_tur']}, Código_est: {matricula['codigo_est']},")

# Atualizar
def atualizar(opcao):
    if opcao == estudantes:
        codigo = int(input("Digite o código do estudante que deseja editar: "))
        for estudante in estudantes:
            if estudante["codigo_est"] == codigo:
                nome = input("Digite o novo nome do estudante: ")
                cpf = input("Digite o novo CPF do estudante: ")
                estudante["nome_est"] = nome
                estudante["cpf_est"] = cpf
                print("Estudante atualizado com sucesso.")
                break
            else:
                print("Estudante não encontrado.")
    elif opcao == disciplinas:
        codigo = int(input("Digite o código da disciplina que deseja editar: "))
        for disciplina in disciplinas:
            if disciplina["codigo_dis"] == codigo:
                codigo = input("Digite o novo código da disciplina: ")
                nome = input("Digite o novo nome da disciplina: ")
                disciplina["cod_dis"] = codigo
                disciplina["nome_dis"] = nome
                
                print("Disciplina atualizada com sucesso.")
                break
            else:
                print("Disciplina não encontrada.")
    elif opcao == professores:
        codigo = int(input("Digite o código do professor que deseja editar: "))
        for professor in professores:
            if professor["codigo_pro"] == codigo:
                nome = input("Digite o novo nome do professor: ")
                cpf = input("Digite o novo CPF do professor: ")
                professor["nome_pro"] = nome
                professor["cpf_pro"] = cpf
                print("Professor atualizado com sucesso.")
                break
            else:
                print("Professor não encontrado.")
    elif opcao == turmas:
        codigo = int(input("Digite o código da turma que deseja editar: "))
        for turma in turmas:
            if turma["codigo_tur"] == codigo:
                codigo_tur = input("Digite o novo código da turma: ")
                codigo_pro = input("Digite o novo código do professor: ")
                codigo_dis = input("Digite o novo código da disciplina: ")
                turma["codigo_tur"] = codigo_tur
                turma["codigo_pro"] = codigo_pro
                turma["codigo_dis"] = codigo_dis
                print("Turma atualizada com sucesso.")
                break
            else:
                print("Turma não encontrada.")
    elif opcao == matriculas:
        codigo_tur = int(input("Digite o código da turma para a matrícula que deseja alterar: "))
        codigo_est = int(input("Digite o código do estudante para a matrícula que deseja alterar: "))
        for matricula in matriculas:
            if matricula["codigo_tur"] == codigo_tur and matricula["codigo_est"] == codigo_est:
                codigo_tur = input("Digite o novo código da turma: ")
                codigo_est = input("Digite o novo código do estudante: ")
                matricula["codigo_tur"] = codigo_tur
                matricula["codigo_pro"] = codigo_est
                print("Turma atualizada com sucesso.")
                break
            else:
                print("Turma não encontrada.")

# Excluir  
def excluir(opcao):
    if opcao == estudantes:
        codigo = int(input("Digite o código do estudante que deseja excluir: "))
        for estudante in estudantes:
            if estudante["codigo_est"] == codigo:
                estudantes.remove(estudante)
                print("Estudante excluído com sucesso.")
                break
            else:
                print("Estudante não encontrado.")
    elif opcao == disciplinas:
        codigo = int(input("Digite o código da disciplina que deseja excluir: "))
        for disciplina in disciplinas:
            if disciplina["codigo_dis"] == codigo:
                disciplinas.remove(disciplina)
                print("Disciplina excluída com sucesso.")
                break
            else:
                print("Disciplina não encontrada.")
    elif opcao == professores:
        codigo = int(input("Digite o código do professor que deseja excluir: "))
        for professor in professores:
            if professor["codigo_pro"] == codigo:
                professores.remove(professor)
                print("Professor excluído com sucesso.")
                break
            else:
                print("Professor não encontrado.")
    elif opcao == turmas:
        codigo = int(input("Digite o código da turma que deseja excluir: "))
        for turma in turmas:
            if turma["codigo_tur"] == codigo:
                turmas.remove(turma)
                print("Turma excluída com sucesso.")
                break
            else:
                print("Turma não encontrada.")

    elif opcao == matriculas:
        codigo_tur = int(input("Digite o código da turma referene a matrícula que deseja excluir: "))
        codigo_est = int(input("Digite o código do estudante referente a matrícula que deseja excluir: "))
        for matricula in matriculas:
            if matricula["codigo_tur"] == codigo_tur and matricula["codigo_est"] == codigo_est:
                matriculas.remove(matricula)
                print("Matrícula excluída com sucesso.")
                break
            else:
                print("Matrícula não encontrada.")

# Loop principal
while True:
    menu_principal()
    opcao_principal = input("Informe a opção desejada: ")

    if opcao_principal == "1":
        print("--- ESTUDANTES ---")

        while True:
            menu_operacoes()
            operacao = input("Informe a operação desejada: ")
            if operacao == "1":
                print("--- Incluir ---")
                incluir(estudantes)
            elif operacao == "2":
                print("--- Listar ---")
                listar(estudantes)
            elif operacao == "3":
                print("--- Atualizar ---")
                atualizar(estudantes)
            elif operacao == "4":
                print("--- Excluir ---")
                excluir(estudantes)
            elif operacao == "5":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida, tente novamente!")
                input("Pressione ENTER para continuar")
                continue

    elif opcao_principal == "2":
        print("--- DISCIPLINAS ---")

        while True:
            menu_operacoes()
            operacao = input("Informe a operação desejada: ")
            if operacao == "1":
                print("--- Incluir ---")
                incluir(disciplinas)
            elif operacao == "2":
                print("--- Listar ---")
                listar(disciplinas)
            elif operacao == "3":
                print("--- Atualizar ---")
                atualizar(disciplinas)
            elif operacao == "4":
                print("--- Excluir ---")
                excluir(disciplinas)
            elif operacao == "5":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida, tente novamente!")
                input("Pressione ENTER para continuar")
                continue

    elif opcao_principal == "3":
        print("--- PROFESSORES ---")

        while True:
            menu_operacoes()
            operacao = input("Informe a operação desejada: ")
            if operacao == "1":
                print("--- Incluir ---")
                incluir(professores)
            elif operacao == "2":
                print("--- Listar ---")
                listar(professores)
            elif operacao == "3":
                print("--- Atualizar ---")
                atualizar(professores)
            elif operacao == "4":
                print("--- Excluir ---")
                excluir(professores)
            elif operacao == "5":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida, tente novamente!")
                input("Pressione ENTER para continuar")
                continue

    elif opcao_principal == "4":
        print("--- TURMAS ---")

        while True:
            menu_operacoes()
            operacao = input("Informe a operação desejada: ")

            if operacao == "1":
                print("--- Incluir ---")
                incluir(turmas)
            elif operacao == "2":
                print("--- Listar ---")
                listar(turmas)
            elif operacao == "3":
                print("--- Atualizar ---")
                atualizar(turmas)
            elif operacao == "4":
                print("--- Excluir ---")
                excluir(turmas)
            elif operacao == "5":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida, tente novamente!")
                input("Pressione ENTER para continuar")
                continue

    elif opcao_principal == "5":
        print("--- MATRÍCULAS ---")

        while True:
            menu_operacoes()
            operacao = input("Informe a operação desejada: ")

            if operacao == "1":
                print("--- Incluir ---")
                incluir(matriculas)
            elif operacao == "2":
                print("--- Listar ---")
                listar(matriculas)
            elif operacao == "3":
                print("--- Atualizar ---")
                atualizar(matriculas)
            elif operacao == "4":
                print("--- Excluir ---")
                excluir(matriculas)
            elif operacao == "5":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida, tente novamente!")
                input("Pressione ENTER para continuar")
                continue

    elif opcao_principal == "6":
        print("Salvando dados e saindo do sistema...")
        salvar_dados()
        break
    else:
        print("Opção inválida, tente novamente!")
        input("Pressione ENTER para continuar")
        continue

print("Finalizando Aplicação...")