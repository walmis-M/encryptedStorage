# EncryptedStorage
It's a library for easy create encrypted storage on any platform.
It's using XChaCha20-Poly1305 and scrypt as KDF.

## Quick start
Clone repo
```bash
git clone https://github.com/walmis-m/encryptedStorage && cd encryptedStorage
```
Create virtual environment
```bash
python -m venv venv
```
Activate venv in Linux/macOS
```bash
source venv/bin/activate
```
Activate venv in Windows CMD
```cmd
venv\Scripts\activate
```
Install requirements
```bash
pip install -r requirements.txt
```
Run example
```bash
python examples/encrypted_file.py
```

## Project structure
```text
encryptedStorage/
├── examples/
│   └── encrypted_file.py
├── encrypted_storage.py
├── requirements.txt
└── README.md
```
