class tweets:
    def __init__(self, tweets):
        self.tweets = tweets

    def tweet_id( self ):
        return( self.tweets.select( "strong.fullname" )[0].get_text() )
    
    def tweet_image( self ):
        return( [ image[ "src" ] for image in self.tweets.select( "img" ) ] )

    def tweet_text( self ):
        return( self.tweets.select( "p.tweet-text" )[0].get_text() )

    def tweet_time( self ):
        return( self.tweets.select( "a.tweet-timestamp" )[0][ "title" ] )
