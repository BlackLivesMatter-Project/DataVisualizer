"""used to play with DataParser class"""
from .data_parser import DataParser

def run_app():
    """Main function for running app from command line."""
    tweets = DataParser('data/1000-blm-tweets.csv')
    print(tweets.collect_users_by_followers(min_followers=10000))
    #print(tweets.collect_retweets(10))
    #print(retweets.head(15))

if __name__ == '__main__':
    run_app()
