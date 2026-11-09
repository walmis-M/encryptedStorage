import sys
from pathlib import Path
import logging

# importing EncryptedStorage
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
from encrypted_storage import EncryptedStorage

# creating subclass
class EncryptedFile(EncryptedStorage):
    def __init__(self, password: str | bytes, file_path: Path):
        super().__init__(password)
        self.file_path = file_path

    def send(self, data: bytes) -> bool:
        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            if self.file_path.exists() and not self.file_path.is_file():
                logging.error("Path is not a file.")
                return False
            with open(self.file_path, "wb") as f:
                f.write(data)
            return True
        except PermissionError:
            logging.error("Permission denied.")
            return False
        except OSError as e:
            logging.error(f"OSError: {e}")
            return False

    def get(self) -> bytes | None:
        try:
            with open(self.file_path, "rb") as f:
                return f.read()
        except (PermissionError, IsADirectoryError):
            logging.error("Permission denied or path is a directory.")
            return None
        except OSError as e:
            logging.error(f"OSError: {e}")
            return None

if __name__ == "__main__":
    encrypted_file = EncryptedFile("password", Path("example.enc"))
    # writing
    print("Writing to file...")
    write_success = encrypted_file.encrypt_and_send("TOP SECRET DATA")
    if write_success:
        print("Success!")
    else:
        print("Failed!")

    # reading
    dec = encrypted_file.get_and_decrypt()
    print(dec) # TOP SECRET DATA
