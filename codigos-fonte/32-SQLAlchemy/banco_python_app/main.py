from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from datetime import datetime

# Configuração do banco e modelo
engine = create_engine("sqlite:///database/banco_python_app.db")
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    data_nasc = Column(Date, nullable=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def cadastrar_usuario(session):
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    while True:
        data_nasc_str = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
        try:
            data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")
    novo_usuario = Usuario(nome=nome, email=email, data_nasc=data_nasc)
    session.add(novo_usuario)
    session.commit()
    print("Registro inserido com sucesso!")

def listar_usuarios(session):
    usuarios = session.query(Usuario).all()
    print("\nUsuários cadastrados:\n")
    for usuario in usuarios:
        print(f"ID: {usuario.id_usuario}")
        print(f"Nome: {usuario.nome}")
        print(f"Email: {usuario.email}")
        if usuario.data_nasc:
            print(f"Data de Nascimento: {usuario.data_nasc.strftime('%d/%m/%Y')}")
        else:
            print("Data de Nascimento: Não informada")
        print("-" * 30)

def atualizar_usuario(session):
    id_usuario = input("Digite o ID do usuário que deseja atualizar: ").strip()
    usuario = session.query(Usuario).filter_by(id_usuario=id_usuario).first()
    if usuario:
        novo_nome = input(f"Novo nome ({usuario.nome}): ").strip() or usuario.nome
        novo_email = input(f"Novo email ({usuario.email}): ").strip() or usuario.email
        nova_data_nasc_str = input(f"Nova data de nascimento ({usuario.data_nasc.strftime('%d/%m/%Y') if usuario.data_nasc else 'Não informada'}): ").strip()
        if nova_data_nasc_str:
            try:
                nova_data_nasc = datetime.strptime(nova_data_nasc_str, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Mantendo a anterior.")
                nova_data_nasc = usuario.data_nasc
        else:
            nova_data_nasc = usuario.data_nasc
        usuario.nome = novo_nome
        usuario.email = novo_email
        usuario.data_nasc = nova_data_nasc
        session.commit()
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def excluir_usuario(session):
    id_usuario = input("Digite o ID do usuário que deseja excluir: ").strip()
    usuario = session.query(Usuario).filter_by(id_usuario=id_usuario).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

def main():
    session = Session()
    while True:
        os.system("cls")
        print("Escolha uma opção:")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Excluir usuário")
        print("5 - Sair")
        opcao = input("Opção: ").strip()
        match opcao:
            case "1":
                cadastrar_usuario(session)
                input("Pressione Enter para continuar...")
            case "2":
                listar_usuarios(session)
                input("Pressione Enter para continuar...")
            case "3":
                atualizar_usuario(session)
                input("Pressione Enter para continuar...")
            case "4":
                excluir_usuario(session)
                input("Pressione Enter para continuar...")
            case "5":
                break
            case _:
                print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")
    session.close()

if __name__ == "__main__":
    main()

# NOTE: código-fonte antigo
# from sqlalchemy import create_engine, Column, Integer, String, Date
# from sqlalchemy.orm import declarative_base, sessionmaker
# import os
# from datetime import datetime

# try:
#     engine = create_engine("sqlite:///database/banco_python_app.db")
#     Base = declarative_base()

#     class Usuario(Base):
#         __tablename__ = "usuario"

#         id_usuario = Column(Integer, primary_key=True, autoincrement=True)
#         nome = Column(String(255), nullable=False)
#         email = Column(String(255), nullable=False, unique=True)
#         data_nasc = Column(Date, nullable=True)  # Agora como tipo DATE

#     Base.metadata.create_all(engine)
# except Exception as e:
#     print(f"Erro ao criar a tabela: {e}")

# try:
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     os.system("cls")

#     while True:
#         cadastrar = input("Deseja cadastrar um novo usuário? (s/n): ").strip().lower()
#         match cadastrar:
#             case "s":
#                 nome = input("Digite o nome do usuário: ")
#                 email = input("Digite o email do usuário: ")
#                 while True:
#                     data_nasc_str = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
#                     try:
#                         data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
#                         break
#                     except ValueError:
#                         print("Data inválida. Use o formato dd/mm/aaaa.")

#                 novo_usuario = Usuario(nome=nome, email=email, data_nasc=data_nasc)

#                 session.add(novo_usuario)
#                 session.commit()

#                 os.system("cls")

#                 print("Registro inserido com sucesso!")

#                 continue
#             case "n":
#                 break
#             case _:
#                 print("Opção inválida. Tente novamente.")
#                 continue

#     usuarios = session.query(Usuario).all()

#     os.system("cls")

#     print("\nUsuários cadastrados:\n")
#     for usuario in usuarios:
#         print(f"ID: {usuario.id_usuario}")
#         print(f"Nome: {usuario.nome}")
#         print(f"Email: {usuario.email}")
#         if usuario.data_nasc:
#             print(f"Data de Nascimento: {usuario.data_nasc.strftime('%d/%m/%Y')}")
#         else:
#             print("Data de Nascimento: Não informada")
#     session.close()
# except Exception as e:
#     print(f"Erro ao inserir registro. {e}")