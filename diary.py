import os
import json
from datetime import datetime

# 日記エントリを保存するファイル
DIARY_FILE = 'diary.json'

def load_entries():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_entries(entries):
    with open(DIARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(entries, file, indent=4, ensure_ascii=False)

def create_entry(entries):
    date = input("日付を入力してください (YYYY-MM-DD) またはEnterキーを押して今日の日付を使用: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    content = input("日記を入力してください: ")
    entries[date] = content
    print(f"{date} のエントリが保存されました。")
    save_entries(entries)

def view_entry(entries):
    date = input("表示する日付を入力してください (YYYY-MM-DD): ")
    if date in entries:
        print(f"{date} のエントリ:")
        print(entries[date])
    else:
        print(f"{date} のエントリは見つかりませんでした。")

def edit_entry(entries):
    date = input("編集する日付を入力してください (YYYY-MM-DD): ")
    if date in entries:
        print(f"{date} の現在のエントリ:")
        print(entries[date])
        new_content = input("新しい内容を入力してください: ")
        entries[date] = new_content
        print(f"{date} のエントリが更新されました。")
        save_entries(entries)
    else:
        print(f"{date} のエントリは見つかりませんでした。")

def delete_entry(entries):
    date = input("削除する日付を入力してください (YYYY-MM-DD): ")
    if date in entries:
        del entries[date]
        print(f"{date} のエントリが削除されました。")
        save_entries(entries)
    else:
        print(f"{date} のエントリは見つかりませんでした。")

def search_entries(entries):
    keyword = input("検索するキーワードを入力してください: ")
    found = False
    for date, content in entries.items():
        if keyword in content:
            print(f"{date} のエントリ:")
            print(content)
            found = True
    if not found:
        print("そのキーワードを含むエントリは見つかりませんでした。")

def main():
    entries = load_entries()
    while True:
        print("\n日記アプリ")
        print("1. 新しいエントリを作成")
        print("2. エントリを表示")
        print("3. エントリを編集")
        print("4. エントリを削除")
        print("5. エントリを検索")
        print("6. 終了")
        choice = input("オプションを選んでください: ")

        if choice == '1':
            create_entry(entries)
        elif choice == '2':
            view_entry(entries)
        elif choice == '3':
            edit_entry(entries)
        elif choice == '4':
            delete_entry(entries)
        elif choice == '5':
            search_entries(entries)
        elif choice == '6':
            break
        else:
            print("無効な選択です。もう一度やり直してください。")

if __name__ == "__main__":
    main()