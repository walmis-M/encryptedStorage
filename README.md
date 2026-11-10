![GitHub License](https://img.shields.io/github/license/walmis-m/encryptedStorage)
![GitHub Stars](https://img.shields.io/github/stars/walmis-m/encryptedStorage)

# EncryptedStorage
A library for easily creating encrypted storage for small objects on any platform.
Uses XChaCha20-Poly1305 and scrypt as the KDF.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

