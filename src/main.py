import sys
import os
import uvicorn
from infraestrutura.api.usuario_api import app
from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from repositorios.sqlite_usuario_repositorio import SQLiteUsuarioRepositorio

# Adiciona o caminho do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Caminho do banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'data', 'villasapp_base.db')

# Cria o diretório se não existir
os.makedirs(os.path.dirname(db_path), exist_ok=True)

if __name__ == "__main__":
    connector = SQLiteConnector(db_path)
    repositorio = SQLiteUsuarioRepositorio(connector)
    uvicorn.run(app, host="0.0.0.0", port=8000)