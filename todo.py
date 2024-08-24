tasks = []

def show_tasks():
    if not tasks:
        print("タスクはありません。")
    else:
        print("現在のタスク:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("追加するタスクを入力してください: ")
    tasks.append(task)
    print(f"タスク '{task}' を追加しました。")

def delete_task():
    show_tasks()
    task_num = int(input("削除するタスク番号を入力してください: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"タスク '{removed_task}' を削除しました。")
    else:
        print("無効な番号です。")

def main():
    while True:
        print("\n--- To-Do リスト ---")
        print("1. タスクを表示")
        print("2. タスクを追加")
        print("3. タスクを削除")
        print("4. 終了")
        choice = input("選択肢を入力してください: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("終了します。")
            break
        else:
            print("無効な選択です。")

if __name__ == "__main__":
    main()