from hashlib import sha256

def generate_idempotency_key(request_id: str, payload: dict) -> str:
    raw = f"{request_id}:{sorted(payload.items())}"
    return sha256(raw.encode()).hexdigest()
