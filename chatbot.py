from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# チャットボットのインスタンスを作成
chatbot = ChatBot('SimpleBot')

# トレーナーの設定
trainer = ChatterBotCorpusTrainer(chatbot)

# トレーナーに標準的な英語の対話データを学習させる
trainer.train('chatterbot.corpus.english')

print("チャットボットが準備できました。終了するには 'exit' と入力してください。")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("チャットを終了します。")
            break

        # ユーザー入力に対する応答を生成
        response = chatbot.get_response(user_input)
        print("Bot:", response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
