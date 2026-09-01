from keygen import generate_keypair

def bytes_to_chunks(data, k):
    if(len(data) % k != 0):
        p = k - (len(data) % k)
    else:
        p = k 
    padding = bytes([p] * p)
    padded_data = data + padding
    chunks = [padded_data[i:i+k] for i in range(0, len(padded_data), k)]
    int_chunks = [int.from_bytes(chunk, byteorder="big") for chunk in chunks]
    return int_chunks

def chunks_to_bytes(chunks, k):
    chunk_bytes = [chunk.to_bytes(k, byteorder="big") for chunk in chunks]
    full_data = b"".join(chunk_bytes)
    padding = full_data[-1:]
    padding = int.from_bytes(padding, byteorder="big")
    return full_data[:-padding]
