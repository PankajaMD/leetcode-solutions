class Twitter:
    def __init__(self):
        self.timeStamp = 0
        self.userMap = {}

    class Tweet:
        def __init__(self, id: int, time: int):
            self.id = id
            self.time = time
            self.next = None

        def __lt__(self, other):
            # Max-heap behavior: higher timestamp has higher priority
            return self.time > other.time

    class User:
        def __init__(self, id: int):
            self.id = id
            self.followed = set()
            self.follow(id)  # User should follow themselves[cite: 3]
            self.tweetHead = None

        def follow(self, id: int):
            self.followed.add(id)

        def unfollow(self, id: int):
            if id != self.id:
                self.followed.remove(id)

        def post(self, id: int, time: int):
            newTweet = Twitter.Tweet(id, time)
            newTweet.next = self.tweetHead
            self.tweetHead = newTweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userMap:
            self.userMap[userId] = self.User(userId)
        self.userMap[userId].post(tweetId, self.timeStamp)
        self.timeStamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        newsFeed = []
        if userId not in self.userMap:
            return newsFeed

        followedUsers = self.userMap[userId].followed
        tweetHeap = []

        for user in followedUsers:
            tweet = self.userMap[user].tweetHead
            if tweet:
                heapq.heappush(tweetHeap, tweet)

        count = 0
        while tweetHeap and count < 10:
            tweet = heapq.heappop(tweetHeap)
            newsFeed.append(tweet.id)
            count += 1
            if tweet.next:
                heapq.heappush(tweetHeap, tweet.next)

        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userMap:
            self.userMap[followerId] = self.User(followerId)
        if followeeId not in self.userMap:
            self.userMap[followeeId] = self.User(followeeId)
        self.userMap[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userMap and followerId != followeeId:
            self.userMap[followerId].unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
