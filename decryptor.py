from base64 import b64decode
from Crypto.Cipher import AES

KEY = bytes(
    [
        57, 114, 107, 120, 67, 80, 108, 106, 83,
        77, 49, 71, 86, 81, 104, 87, 119, 49, 114,
        49, 114, 75, 79, 72, 71, 99, 99, 98, 50, 105, 74, 53
    ]
)
IV = bytes(16)  # 16 zero bytes for CBC mode

ciphertext = "IegY21/091yYehMIQUAncLMHj63J9ZNv5mKgx7wUIHYw3+fWqz+WXQCbyDBGWavWPaaSayRdrXAytwVDcDppzHBapcfC4RCiw4srDMCY9X0ejcgn5588S6RN+RdKAECXu7FLoDdicpYYUVaj0eCKHpoA1bMhuKmKLYB8ArfydKZ5RedOJrNeRZSe/Qj359K33rd7QJwkY3CNTtGh5XUzV2ue1q+rZxKX95ikmWW0lxuuvVzqypyLUb+DrzYFCCaoJUxYj2TvAeLQngClFjIi4vH3D8Okp1Yykp8WKvG3729wx+ypuTcGsvByeo7ZATIWrX5od0fQneZZOSPUVfHJzonLn16Ey6+0vy6wajwVaI1d8qUWGFPcBNtKb89W930c"

def decrypt(ciphertext: str) -> str:
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    buffer = b64decode(ciphertext)
    decrypted_data = aes.decrypt(buffer)
    return decrypted_data.decode()

print(decrypt(ciphertext))
