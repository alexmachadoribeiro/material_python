import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# cria a engine
try:
    engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/crud_python")
    Base = declarative_base()
except Exception as e:
    print(f"Erro ao criar conexão: {e}.")

# classes
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

class Ddd(Base):
    __tablename__ = "ddd"

    id_ddd = Column(Integer, primary_key=True, autoincrement=True)
    ddd = Column(String(2), nullable=False, unique=True)


class Telefone(Base):
    __tablename__ = "telefone"

    id_telefone = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_ddd = Column(Integer, ForeignKey("ddd.id_ddd"), nullable=False)
    numero = Column(String(10), nullable=False)


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

# cria as tabelas
try:
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")
except Exception as e:
    print(f"Erro ao criar tabelas: {e}.")
