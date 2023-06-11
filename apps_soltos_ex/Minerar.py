from hashlib import sha256
import time

def aplicar_sha256(texto):
  print(sha256("a".encode("ascii")).hexdigest())

def minerar(num_bloco, transacoes, hash_anterior, qtd_zeros):
  nonce = 0
  while True:
    texto = str(num_bloco) + transacoes + hash_anterior + str(qtd_zeros)
    meu_hash = aplicar_sha256(texto)
    incio_zero = str(meu_hash)[0:qtd_zeros]
    if incio_zero == "0"*qtd_zeros:
        return nonce, meu_hash
    # if meu_hash.startswith("0" * qtd_zeros):
    #   return nonce, meu_hash
  nonce += 1




def aplicar_sha256(texto):
  print(sha256("a".encode("ascii")).hexdigest())

# def minerar(num_bloco, transacoes, hash_anterior, qtd_zeros):
#   nonce = 0
#   while True:
#     texto = str(num_bloco) + transacoes + hash_anterior + str(qtd_zeros)
#     meu_hash = aplicar_sha256(texto)
#     nonce += 1
    
num_bloco = 15
transacoes = """Lira -> Alon -> 10; Alon -> joão -> 15; João -> Amanda -> 5"""
hash_anterior = "abc"
qtd_zeros = 2
inicio = time.time()
resultado = minerar(num_bloco, transacoes, hash_anterior, qtd_zeros)
print(resultado)
print(time.time() - inicio)


texto = str(num_bloco) + transacoes + hash_anterior + str(qtd_zeros)
meu_hash = aplicar_sha256(texto)
a = str(meu_hash)

# print(meu_hash)
print(a)
