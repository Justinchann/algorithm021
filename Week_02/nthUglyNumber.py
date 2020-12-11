import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hp = [1]
        heapq.heapify(hp)
        count = 0
        while hp:
            a = heapq.heappop(hp)
            count+=1
            if a*2 not in hp:
                heapq.heappush(hp,a*2)
            if a*3 not in hp:
                heapq.heappush(hp,a*3)
            if a*5 not in hp:
                heapq.heappush(hp,a*5)
            if count==n:
                return a

        # dp = [0]*n
        # dp[0] = 1
        # a, b, c = 0, 0, 0
        # for i in range(1,n):
        #     dp[i] = min(dp[a]*2,dp[b]*3,dp[c]*5)
        #     if dp[i]==dp[a]*2:
        #         a+=1
        #     if dp[i]==dp[b]*3:
        #         b+=1
        #     if dp[i]==dp[c]*5:
        #         c+=1
        # return dp[-1]