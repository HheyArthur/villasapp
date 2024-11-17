import bcrypt

# Função para criptografar a senha
def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Função para verificar a senha
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha.encode('utf-8'))