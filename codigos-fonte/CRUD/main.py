# ANCHOR - Importa as bibliotecas
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# ANCHOR - cria a engine
try:
    engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/crud_python")
    Base = declarative_base()
except Exception as e:
    print(f"Erro ao criar conexão: {e}.")

# SECTION - classes
class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=False)

    # Método para definir a data de nascimento no formato brasileiro
    def set_data_nascimento(self, data_str):
        self.data_nascimento = datetime.strptime(data_str, "%d/%m/%Y").date()

class Estado(Base):
    __tablename__ = "estado"

    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    sigla = Column(String(2), nullable=False, unique=True)
    nome = Column(String(255), nullable=False, unique=True)

class Logradouro(Base):
    __tablename__ = "logradouro"

    id_logradouro = Column(Integer, primary_key=True, autoincrement=True)
    logradouro = Column(String(255), nullable=False, unique=True)


class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_estado = Column(Integer, ForeignKey("estado.id_estado"), nullable=False)
    id_logradouro = Column(Integer, ForeignKey("logradouro.id_logradouro"), nullable=False)
    cep = Column(String(8), nullable=False)
    numero = Column(String(10), nullable=False)
    complemento = Column(String(255), nullable=True)
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)

class Ddd(Base):
    __tablename__ = "ddd"

    id_ddd = Column(Integer, primary_key=True, autoincrement=True)
    id_estado = Column(Integer, ForeignKey("estado.id_estado"), nullable=False)
    ddd = Column(String(2), nullable=False)


class Telefone(Base):
    __tablename__ = "telefone"

    id_telefone = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_ddd = Column(Integer, ForeignKey("ddd.id_ddd"), nullable=False)
    numero = Column(String(10), nullable=False)
# !SECTION

# ANCHOR - cria as tabelas
try:
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")
except Exception as e:
    print(f"Erro ao criar tabelas: {e}.")

# SECTION - CRUD
if __name__ == "__main__":
    try:
        Session = sessionmaker(bind=engine)
        session = Session()

        while True:
            print(f"\n{'=' * 20} CRUD PYTHON {'=' * 20}\n")
            print("0 - Sair do programa")
            print("1 - Cadastrar novo usuário")
            print("2 - Listar")
            print("3 - Atualizar dados")
            print("4 - Deletar usuário")
            opcao = input("Escolha uma opção: ").strip()
            match opcao:
                case "0":
                    print("Saindo do programa...")
                    break
                case "1":
                    # SECTION - Cadastrar
                    os.system("cls")
                    print(f"{'-'*10}Cadastrar novo usuário{'-'*10}\n")

                    # ANCHOR - Dados pessoais
                    nome = input("Digite o nome do usuário: ")
                    email = input("Digite o email do usuário: ")
                    cpf = input("Digite o CPF do usuário (somente números): ")
                    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")

                    # SECTION - Endereço
                    print("Endereço do usuário:")
                    cep = input("Digite o CEP do usuário (somente números): ").strip()

                    # ANCHOR - Selecionar o estado
                    while True:
                        print("Selecione o estado:")
                        estado = session.query(Estado).all()
                        for e in estado:
                            print(f"({e.sigla}) {e.nome}")
                        estado_usuario = input("Informe a sigla do estado do usuário: ").strip().upper()
                        if estado_usuario in estado:
                            break
                        else:
                            print("Estado inválido. Tente novamente.")
                            continue

                    cidade = input("Digite a cidade do usuário: ").strip()
                    bairro = input("Digite o bairro do usuário: ").strip()

                    # ANCHOR - Selecionar o logradouro
                    while True:
                        print("Selecione o logradouro:")
                        logradouro = session.query(Logradouro).all()
                        for l in logradouro:
                            print(f"({l.logradouro})")
                        logradouro_usuario = input("Informe o logradouro do endereço: ").strip()
                        if logradouro_usuario in logradouro:
                            break
                        else:
                            print("Logradouro inválido. Tente novamente.")
                            continue

                    complemento = input("Digite o complemento do endereço (opcional): ").strip()
                    numero = input("Digite o número da residência: ").strip()
                    # !SECTION

                    # REVIEW - selecionar o DDD apenas do estado selecionado
                    while True:
                        print("Selecione o DDD:")

                        ddd = session.query(Ddd).all()
                        for d in ddd:
                            print(f"({d.ddd})")
                        ddd_usuario = input("Informe o DDD do usuário: ").strip()
                        if ddd_usuario in ddd:
                            telefone = input(f"Digite o telefone do usuário (somente números): ({ddd_usuario}) ").strip()
                            break
                        else:
                            print("DDD inválido. Tente novamente.")
                            continue

                    # ANCHOR - cadastra novo usuário
                    novo_usuario = Usuario(nome=nome, email=email, cpf=cpf)
                    novo_usuario.set_data_nascimento(data_nascimento)
                    session.add(novo_usuario)
                    session.commit()

                    usuario_id = novo_usuario.id_usuario
                    estado_id = session.query(Estado).filter_by(sigla=estado_usuario).first().id_estado # REVIEW
                    logradouro_id = session.query(Logradouro).filter_by(logradouro=logradouro_usuario).first().id_logradouro

                    # ANCHOR - cadastra novo telefone
                    novo_telefone = Telefone(id_usuario=usuario_id, id_ddd=ddd_usuario, numero=telefone)
                    session.add(novo_telefone)
                    session.commit()

                    # ANCHOR - cadastra novo endereço
                    novo_endereco = Endereco(
                        id_usuario=usuario_id,
                        id_estado=estado_id,
                        id_logradouro=logradouro_id,
                        cep=cep, numero=numero,
                        complemento=complemento,
                        bairro=bairro,
                        cidade=cidade
                    )

                    session.add(novo_endereco)
                    session.commit()

                    os.system("cls")
                    print("Usuário cadastrado com sucesso!")

                    continue
                # !SECTION
                case "2":
                    # TODO - Listar
                    pass
                case "3":
                    # TODO - Atualizar
                    pass
                case "4":
                    # TODO - Deletar
                    pass
                case _:
                    print("Opção inválida. Tente novamente.")
                    continue

        session.close()
    except Exception as e:
        print(f"Erro ao executar o CRUD: {e}.")
# !SECTION