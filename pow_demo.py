import hashlib
import time

def mine_block(data: str, difficulty: int):
    prefix = "0" * difficulty
    nonce = 0

    start = time.time()

    while True:
        candidate = f"{data}{nonce}"
        h = hashlib.sha256(candidate.encode()).hexdigest()

        if h.startswith(prefix):
            elapsed = time.time() - start
            return {
                "nonce": nonce,
                "hash": h,
                "time": elapsed
            }

        nonce += 1

result = mine_block("SSBlock#1", difficulty=4)

print("Nonce:", result["nonce"])
print("Hash:", result["hash"])
print("Time:", round(result["time"], 3), "seconds")