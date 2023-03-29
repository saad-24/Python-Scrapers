import csv
import snscrape.modules.twitter as sns

class Initializer:
    def __init__(self,query, limit):
        self.query = query
        self.limit = limit
        self.tweets = []

class Scraper(Initializer):
    def twiiter_scraper(self):
        for i in sns.TwitterUserScraper(self.query).get_items():
            if len(self.tweets) == self.limit:
                break
            else:
                self.tweets.append([i.user.username, i.content, i.url, i.date])

class CSV(Scraper):
    def make_csv(self, filename):
        with open(filename, "a", newline="", encoding="utf8") as f:
            csv_write = csv.writer(f)
            columns = ['User','Tweet','Link', 'Date']
            csv_write.writerow(columns)

    def populate_csv(self, filename):
        with open(filename, "a", newline="", encoding="utf8") as f:
            csv_write = csv.writer(f)
            for i in self.tweets:
                csv_write.writerow(i)

class Scraper_Implementor(CSV):
    def get_tweets(self,filename):
        super().twiiter_scraper()
        super().populate_csv(filename)


filename = 'twitter.csv'
obj1 = Scraper_Implementor('elonmusk', 100)
obj1.make_csv(filename)
obj1.get_tweets(filename)







