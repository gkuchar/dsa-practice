from collections import defaultdict
import heapq
from datetime import datetime
class Twitter:

    def __init__(self):
        # maps userId to all followers userIds: int -> Set[int]
        self.followers = defaultdict(set)

        # maps userId to its tweets: time posted + tweetIds: int -> List[(datetime, int)]
        self.tweets = defaultdict(list)
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.clock, tweetId))
        self.clock += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        for follower in self.followers[userId]:
            follower_tweets = self.tweets[follower]
            for follower_tweet in follower_tweets:
                follower_tweet_time = follower_tweet[0]
                if len(news_feed) < 10:
                    heapq.heappush(news_feed, follower_tweet)
                elif follower_tweet_time > news_feed[0][0]:
                    heapq.heappop(news_feed)
                    heapq.heappush(news_feed, follower_tweet)
        
        user_tweets = self.tweets[userId]
        for user_tweet in user_tweets:
            user_tweet_time = user_tweet[0]
            if len(news_feed) < 10:
                heapq.heappush(news_feed, user_tweet)
            elif user_tweet_time > news_feed[0][0]:
                heapq.heappop(news_feed)
                heapq.heappush(news_feed, user_tweet)

        return [tweet[1] for tweet in sorted(news_feed, key=lambda tweet: tweet[0], reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
