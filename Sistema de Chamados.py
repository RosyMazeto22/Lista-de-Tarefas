import sqlite3

# Conectar ao banco
conn = sqlite3.connect("chamados.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    descricao TEXT,
    status TEXT
)
""")
conn.commit()


def criar_chamado():
    titulo = input("Título: ")
    descricao = input("Descrição: ")

    cursor.execute("INSERT INTO chamados (titulo, descricao, status) VALUES (?, ?, ?)",
                   (titulo, descricao, "Aberto"))
    conn.commit()
    print("Chamado criado com sucesso!")


def listar_chamados():
    cursor.execute("SELECT * FROM chamados")
    chamados = cursor.fetchall()

    print("\n📋 Lista de Chamados:")
    for c in chamados:
        print(f"ID: {c[0]} | {c[1]} | {c[2]} | Status: {c[3]}")


def atualizar_status():
    id_chamado = input("ID do chamado: ")
    novo_status = input("Novo status (Aberto/Em andamento/Fechado): ")

    cursor.execute("UPDATE chamados SET status=? WHERE id=?", (novo_status, id_chamado))
    conn.commit()
    print("Status atualizado!")


def deletar_chamado():
    id_chamado = input("ID do chamado: ")

    cursor.execute("DELETE FROM chamados WHERE id=?", (id_chamado,))
    conn.commit()
    print("Chamado removido!")


def menu():
    while True:
        print("\n--- SISTEMA DE CHAMADOS ---")
        print("1 - Criar chamado")
        print("2 - Listar chamados")
        print("3 - Atualizar status")
        print("4 - Deletar chamado")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_chamado()
        elif opcao == "2":
            listar_chamados()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            deletar_chamado()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")


menu()

conn.close()