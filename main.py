from keygen import generate_keypair
from rsa import encrypt, decrypt
from chunking import bytes_to_chunks, chunks_to_bytes

def send_message(text, public_key):
    n, e = public_key
    text_bytes = text.encode()
    k = (n.bit_length() - 1) // 8
    chunks = bytes_to_chunks(text_bytes, k)
    encrypted_chunks = [encrypt(chunk, public_key) for chunk in chunks]
    return encrypted_chunks

def receive_message(ciphertexts, private_key):
    n, d = private_key
    k = (n.bit_length() - 1) // 8
    decrypted_chunks = [decrypt(chunk, private_key) for chunk in ciphertexts]
    decrypted_bytes = chunks_to_bytes(decrypted_chunks, k)
    text = decrypted_bytes.decode()
    return text
