import os
import sqlite3

def criar_conexao() -> sqlite3.Connection:
    os.makedirs("database", exist_ok=True)
    
    caminho_db = "database/smart_stay.db"
    
    conexao = sqlite3.connect(caminho_db)
    
    conexao.execute("PRAGMA foreign_keys = ON;")
    
    conexao.row_factory = sqlite3.Row
    
    return conexao