# Teste manual
import pytest
from infraestrutura.seguranca.criptografia import hash_senha, verificar_senha


senha = "minha_senha_secreta"
senha_criptografada = hash_senha(senha)
print(f"Senha criptografada: {senha_criptografada}")

# Verificação
assert verificar_senha(senha, senha_criptografada) == True
print("Verificação de senha bem-sucedida")