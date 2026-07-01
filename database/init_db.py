from database.database import engine, Base

# Importa os modelos para registrar as tabelas
import database.models


def init_database():
    Base.metadata.create_all(bind=engine)