import bcrypt

# Função para criptografar a senha
def hash_senha(senha: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode('utf-8'), salt)

# Função para verificar a senha
def verificar_senha(senha: str, hash_senha: bytes) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha)