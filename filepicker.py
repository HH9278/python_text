import os
import shutil
import sys

def create_folder_and_copy_files(root_path, keyword):
    # 新しいフォルダのパスを作成
    new_folder_path = os.path.join(root_path, keyword)
    
    # 新しいフォルダが存在しない場合は作成
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"フォルダ '{new_folder_path}' を作成しました。")
    else:
        print(f"フォルダ '{new_folder_path}' は既に存在します。")

    # サブフォルダを再帰的に検索し、キーワードに一致するファイルをコピー
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if keyword in filename:
                source_file = os.path.join(dirpath, filename)
                destination_file = os.path.join(new_folder_path, filename)
                
                # ファイルをコピー
                shutil.copy2(source_file, destination_file)
                print(f"'{source_file}' を '{destination_file}' にコピーしました。")

if __name__ == "__main__":
    # コマンドライン引数の数をチェック
    if len(sys.argv) < 3:
        print("使用方法: python script_name.py <root_path> <keyword>")
        sys.exit(1)
    
    # コマンドライン引数からroot_pathとkeywordを取得
    root_path = sys.argv[1]
    keyword = sys.argv[2]
    
    create_folder_and_copy_files(root_path, keyword)
