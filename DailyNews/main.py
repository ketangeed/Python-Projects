import requests



# Take the news topic from the user
query = input("What type of news are you interested in today: ")



# Add your NewsAPI key
api = "1f15035e6f5944e6b59f6e51c73601ef"



# Create the API request URL
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-07-27&sortBy=publishedAt&apiKey={api}"



# Send the request to NewsAPI
k = requests.get(url)



# Convert the response into Python data
data = k.json()



# Get the list of news articles
articles = data["articles"]



# Display each article with its index number
for index, article in enumerate(articles):  # Index number will appear
    print(index + 1, ".", article["title"], article["url"])
    print("\n****************************************************\n")


    