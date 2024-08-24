from cryptography.fernet import Fernet
import os
import json

# パスワードを暗号化・復号化するためのキーを生成するか、読み込む
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
cipher_suite = Fernet(key)

# パスワードデータを保存するファイル
password_file = "passwords.json"

# パスワードをファイルに保存する
def save_passwords(passwords):
    with open(password_file, "w") as f:
        encrypted_data = cipher_suite.encrypt(json.dumps(passwords).encode())
        f.write(encrypted_data.decode())

# パスワードをファイルから読み込む
def load_passwords():
    if not os.path.exists(password_file):
        return {}
    with open(password_file, "r") as f:
        encrypted_data = f.read().encode()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

# パスワードを追加する
def add_password():
    service = input("サービス名: ")
    username = input("ユーザー名: ")
    password = input("パスワード: ")
    passwords = load_passwords()
    passwords[service] = {"username": username, "password": password}
    save_passwords(passwords)
    print(f"{service} のパスワードを保存しました。")

# パスワードを取得する
def get_password():
    service = input("パスワードを取得するサービス名: ")
    passwords = load_passwords()
    if service in passwords:
        print(f"ユーザー名: {passwords[service]['username']}")
        print(f"パスワード: {passwords[service]['password']}")
    else:
        print(f"{service} のパスワードが見つかりません。")

# パスワードを削除する
def delete_password():
    service = input("パスワードを削除するサービス名: ")
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"{service} のパスワードを削除しました。")
    else:
        print(f"{service} のパスワードが見つかりません。")

# メインメニュー
def main():
    while True:
        print("\n--- パスワードマネージャー ---")
        print("1. パスワードを追加")
        print("2. パスワードを取得")
        print("3. パスワードを削除")
        print("4. 終了")
        choice = input("選択肢: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            break
        else:
            print("無効な選択肢です。")

if __name__ == "__main__":
    main()