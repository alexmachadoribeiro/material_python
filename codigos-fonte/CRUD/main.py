from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from datetime import datetime

try:
    engine = create_engine("sqlite:///db_teste.db")
    Base = declarative_base()

    class Usuario(Base):
        __tablename__ = "usuario"

        id_usuario = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(255), nullable=False)
        email = Column(String(255), nullable=False, unique=True)
        data_nasc = Column(Date, nullable=True)  # Agora como tipo DATE

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
        if usuario.data_nasc:
            print(f"Data de Nascimento: {usuario.data_nasc.strftime('%d/%m/%Y')}")
        else:
            print("Data de Nascimento: Não informada")
    session.close()
except Exception as e:
    print(f"Erro ao inserir registro. {e}")