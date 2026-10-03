import requests
import requests

def get_live_outbreaks_from_newsapi(api_key):
    url = f"https://newsapi.org/v2/everything?q=disease OR virus OR outbreak OR flu&language=en&pageSize=10&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])

    results = []
    for article in articles:
        results.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "publishedAt": article["publishedAt"],
            "url": article["url"]
        })
    return results


def get_real_time_data():
    # Example: Use NewsAPI or GNews
    news_api_key = "your_news_api_key"
    twitter_bearer_token = "your_twitter_bearer_token"

    news_data = []
    twitter_data = []

    try:
        news_response = requests.get(
            f"https://gnews.io/api/v4/search?q=disease+outbreak&token={news_api_key}"
        )
        news_data = [article['title'] for article in news_response.json().get('articles', [])]

        # Simulated twitter data; replace with Twitter API v2 call
        twitter_data = ["Virus outbreak in India", "New flu wave in Europe"]

    except Exception as e:
        news_data = ["Error fetching news data"]
        twitter_data = ["Error fetching tweets"]

    return {
        "tweets": twitter_data,
        "news": news_data,
    }
[
    {"disease": "Dengue", "region": "Mumbai", "cases": 2300, "lat": 19.0760, "lon": 72.8777},
    {"disease": "COVID-19", "region": "Bangalore", "cases": 3000, "lat": 12.9716, "lon": 77.5946}
]
