"""
Twitter user -> user id, list of followers, list of people user followee.

dict of users -> {users id: {'followers':list[ids],'followees':list[id]}} -> ex: dict_of_users[1] -> {1:{'followers':[],'followers':[2,3,4,5]}

global feed -> list[(user id, tweet)] -> everytime a new tweet is created we append.
"""
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_of_users = {}
        self.global_feed = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        
        """ Do we allow repeated tweets to be stored ? """
        res = (userId,tweetId)
        self.global_feed.append(res)
        self.dict_of_users[userId] = self.dict_of_users.get(userId,
            {'followers':[],'followees':[]})
        #print "posting tweet",res

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        
        """ We must return either"
                1. the previous 10 tweets with the id of one of the followees or the user itself
                2. untill the length of the list
        """
        
        length = len(self.global_feed)
        count = 0
        res = []
        
        if userId not in self.dict_of_users:
            return res
        
        while (length > 0) and (count < 10):
            curr = self.global_feed[length-1]
            if (curr[0] in self.dict_of_users[userId]['followees']) or (curr[0]==userId):
                #print "true", curr
                res.append(curr[1])
                count += 1
            #else:
                #print "false",curr
            length -= 1
        #print "feed of id",userId,res
        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            #print "user can not follow him/her-self"
            return False
            
        self.dict_of_users[followerId] = self.dict_of_users.get(followerId,
            {'followers':[],'followees':[]})
            
        if followeeId in self.dict_of_users[followerId]['followees']:
            #print "user already followed"
            return False
        
        else:
            self.dict_of_users[followerId]['followees'].append(followeeId)
        
        #print "added",self.dict_of_users[followerId]['followees']

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            #print "user can not unfollow him/her-self"
            return False
        
        self.dict_of_users[followerId] = self.dict_of_users.get(followerId,
            {'followers':[],'followees':[]})
        
        if followeeId not in self.dict_of_users[followerId]['followees']:
            #print "user is not followed"
            return False
        
        else:
            self.dict_of_users[followerId]['followees'].remove(followeeId)
        
        #print "removed",self.dict_of_users[followerId]['followees']

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)