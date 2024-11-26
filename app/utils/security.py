import hashlib
import secrets

def get_password_hash(password: str) -> str:
    """生成密码哈希 (示例实现)"""
    salt = secrets.token_hex(8)
    combined = (password + salt).encode()
    return f"{salt}${hashlib.sha256(combined).hexdigest()}"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码 (示例实现)"""
    try:
        salt, stored_hash = hashed_password.split('$')
        password_hash = hashlib.sha256((plain_password + salt).encode()).hexdigest()
        return password_hash == stored_hash
    except ValueError:
        return False