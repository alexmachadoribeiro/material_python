# importa as bibliotecas
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

try:
    # cria a engine
    engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/banco_python_app")
    Base = declarative_base()

    # cria a classe Usuario
    class Usuario(Base):
        __tablename__ = "usuario"

        id_usuario = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(255), nullable=False)
        email = Column(String(255), nullable=False, unique=True)

    # cria a tabela
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Erro ao criar a tabela: {e}")

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    os.system("cls")

    while True:
        cadastrar = input("Deseja cadastrar um novo usuário? (s/n): ").strip().lower()
        match cadastrar:
            case "s":
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")

                novo_usuario = Usuario(nome=nome, email=email)

                session.add(novo_usuario)
                session.commit()

                os.system("cls")

                print("Registro inserido com sucesso!")

                continue
            case "n":
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue

    usuarios = session.query(Usuario).all()

    os.system("cls")

    print("\nUsuários cadastrados:\n")
    for usuario in usuarios:
        print(f"ID: {usuario.id_usuario}")
        print(f"Nome: {usuario.nome}")
        print(f"Email: {usuario.email}")
    session.close()
except Exception as e:
    print(f"Erro ao inserir registro. {e}")