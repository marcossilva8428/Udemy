import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine('mysql://dsuser1:Passw0rd@localhost/bancoprodutos')
                                  #mysql://scott:tiger@localhost/test
Base = sqlalchemy.ext.declarative.declarative_base()

# Declaração da classe base
class Produto(Base):
    #nome da tabela
    __tablename__='produtos'
    id = Column(Integer,primary_key=True,autoincrement=True)
    titulo = Column(String(300))
    preco = Column(String(300))
    avaliacao = Column(String(300))

Base.metadata.create_all(engine)

#Vamos criar uma Session, que é uma classe responsável por transformar objetos em linhas do banco e vice versa
TheSession = sessionmaker(bind=engine)
session = TheSession()
