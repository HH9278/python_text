
import os
import requests
from dotenv import load_dotenv
from random import choice

# 環境変数を読み込む
load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# ニュースAPIから最新のニュースを取得する関数
def get_top_headlines():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        headlines = [article['title'] for article in news_data['articles']]
        return headlines
    else:
        print("ニュースの取得に失敗しました。")
        return []

# ツイートを生成する関数
def create_tweet(headlines):
    tweet_templates = [
        "最新ニュース速報: {}",
        "これは見逃せない！: {}",
        "注目のニュース: {}",
        "今日の話題: {}",
    ]
    headline = choice(headlines)
    template = choice(tweet_templates)
    return template.format(headline)

if __name__ == "__main__":
    headlines = get_top_headlines()
    if headlines:
        tweet_text = create_tweet(headlines)
        print("生成されたツイート:", tweet_text)
    else:
        print("有効なニュース見出しがありませんでした。")