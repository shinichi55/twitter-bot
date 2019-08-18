#!/usr/bin/python3

import tweets

import requests
from bs4 import BeautifulSoup

def main_url( search ):
    url = "https://twitter.com/search"

    results = requests.get( url,
        params={ "f": "tweets", "q": "{}".format( search ), "src": "typd" },
        headers={ "User-Agent": "Mozilla/5.0 ( Macintosh; Intel Mac OS X 10_13_6 ) AppleWebKit/537.36 ( KHTML, like Gecko ) Chrome/76.0.3809.100 Safari/537.36" }
    )

    html = BeautifulSoup( results.text, "html.parser" )
    timeline = html.select( "#timeline li.stream-item" )

    return timeline

if __name__ == "__main__":
    search = input( "What are you searching for?: " )
    
    for tweet in main_url( search ):
        twitter = tweets.tweets( tweet )
        print( "\n{}\n{}\n{}\n{}".format( twitter.tweet_id(), twitter.tweet_text(), twitter.tweet_image(), twitter.tweet_time() ) )

