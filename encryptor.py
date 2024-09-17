from base64 import b64encode
from Crypto.Cipher import AES
import json

KEY = bytes(
    [
        57, 114, 107, 120, 67, 80, 108, 106, 83,
        77, 49, 71, 86, 81, 104, 87, 119, 49, 114,
        49, 114, 75, 79, 72, 71, 99, 99, 98, 50, 105, 74, 53
    ]
)
IV = bytes(16)  # 16 zero bytes for CBC mode

def encrypt(data: str) -> str:
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    # Pad the data to be multiple of block size (16 bytes)
    pad_length = AES.block_size - (len(data) % AES.block_size)
    padded_data = data + chr(pad_length) * pad_length
    encrypted_data = cipher.encrypt(padded_data.encode())
    return b64encode(encrypted_data).decode()

# Define the data to encrypt
data = {
    "lastSaved": "2024-09-17T00:14:35.885244Z",
    "currencies": {"1": {"value": 515231434, "expirationType": 0}},
    "lootboxQueue": {"unopenedLootboxes": []},
    "currencyAllowedInRun": {},
    "lootBoxesOpened": {},
    "LootTableInjectedEntryOverrides": {},
    "ownedOnlyBuyOnceProducts": [],
    "productPurchaseTimeData": {}
}

# Convert the data to JSON and encrypt it
json_data = json.dumps(data)
encrypted_json_data = encrypt(json_data)

print("Encrypted data:", encrypted_json_data)
