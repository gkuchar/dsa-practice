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
        people = self.followers[userId] | {userId}

        heap = []
        for personId in people:
            tweets = self.tweets[personId]
            if tweets:
                index = len(tweets) - 1
                clock, tweetId = tweets[index]
                heapq.heappush(heap, (-clock, tweetId, personId, index))

        news_feed = []
        while heap and len(news_feed) < 10:
            neg_clock, tweetId, personId, index = heapq.heappop(heap)
            news_feed.append(tweetId)
            if index > 0:
                index -= 1
                clock, next_tweetId = self.tweets[personId][index]
                heapq.heappush(heap, (-clock, next_tweetId, personId, index))
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
