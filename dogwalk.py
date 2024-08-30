import random

# ゲームの初期設定
distance_to_walk = 10  # 目標の距離
current_distance = 0   # 現在の距離
points = 0             # プレイヤーのポイント

# イベントリストとその結果
events = [
    {"description": "他の犬と出会った！どうする？", "choices": {"1": ("近づいて挨拶", 1), "2": ("無視する", 0), "3": ("吠える", -1)}},
    {"description": "犬が道端の何かを嗅いでいる！どうする？", "choices": {"1": ("一緒に嗅ぐ", 0), "2": ("引っ張って先に進む", 1), "3": ("待ってあげる", 1)}},
    {"description": "公園でボールを見つけた！どうする？", "choices": {"1": ("ボールを投げて遊ぶ", 1), "2": ("無視して歩き続ける", 0), "3": ("持ち帰る", 2)}},
    {"description": "雨が降り始めた！どうする？", "choices": {"1": ("近くの木の下で雨宿り", 0), "2": ("雨の中を走る", 2), "3": ("散歩をやめて帰る", -1)}}
]

# ゲームのメインループ
while current_distance < distance_to_walk:
    print(f"\n現在の距離: {current_distance} km, ポイント: {points}")
    event = random.choice(events)
    print(event["description"])
    for key, (choice, _) in event["choices"].items():
        print(f"{key}: {choice}")
    
    # プレイヤーの選択を取得
    player_choice = input("選択肢を入力してください (1, 2, 3): ")
    
    # 正しい選択肢が入力されるまで繰り返す
    while player_choice not in event["choices"]:
        print("無効な選択です。もう一度選んでください。")
        player_choice = input("選択肢を入力してください (1, 2, 3): ")

    # 選択に基づいてポイントを更新
    points += event["choices"][player_choice][1]
    current_distance += 1  # 距離を進める

print(f"\n散歩が終了しました！総ポイント: {points}")
if points > 5:
    print("素晴らしい散歩でしたね！")
elif points > 0:
    print("まあまあの散歩でした！")
else:
    print("次回はもっといい散歩になるといいですね！")