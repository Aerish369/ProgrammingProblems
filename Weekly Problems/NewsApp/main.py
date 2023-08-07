# Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
# Go to: https://newsapi.org/ and explore the various options to build you application

import requests

input1 = int(input("""Welcome to daily tech news. 
                Press 1 for General news.
                Press 2 for Bitcoin news.
                Press 3 for Apple company related news. 
                Press 4 for TechCrunch and The Next Web published news.\n"""))

if input1 == 1:
    def gnews():
        main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=9bf51c3e2c9e40e58922ed9b892f1a4f"
        gnews = requests.get(main_url).json()
        article = gnews["articles"]
        # print(article)

        ns_article = []
        for i in article:
            ns_article.append(i["title"])
            # print(ns_article)

        for j in range(5):
            print(j+1, ns_article[j])
    gnews()
elif input1 == 2:
    def bnews():
        bitcoin_url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=9bf51c3e2c9e40e58922ed9b892f1a4f"
        bnews = requests.get(bitcoin_url).json()
        article = bnews["articles"]
        # print(article)

        bs_article = []
        for i in article:
            bs_article.append(i["title"])
            # print(ns_article)

        for j in range(5):
            print(j+1, bs_article[j])
    bnews()
elif input1 == 3:
    def anews():
        apple_url = "https://newsapi.org/v2/everything?q=apple&from=2023-08-06&to=2023-08-06&sortBy=popularity&apiKey=9bf51c3e2c9e40e58922ed9b892f1a4f"
        anews = requests.get(apple_url).json()
        article = anews["articles"]
        # print(article)

        as_article = []
        for i in article:
            as_article.append(i["title"])
            # print(ns_article)

        for j in range(5):
            print(j+1, as_article[j])
    anews()
elif input1 == 4:
    def tenews():
        tech_url = "https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=9bf51c3e2c9e40e58922ed9b892f1a4f"
        tenews = requests.get(tech_url).json()
        article = tenews["articles"]
        # print(article)

        te_article = []
        for i in article:
            te_article.append(i["title"])
            # print(ns_article)

        for j in range(5):
            print(j+1, te_article[j])
    tenews()
else:
    print("Invalid Input")












