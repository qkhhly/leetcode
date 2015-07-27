
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        ''' 
            use a dict
        '''
        num_dist = {}
        
        for i in range(len(nums)):
            if nums[i] in num_dist:
                num_dist[nums[i]].append(i+1)
            else:
                num_dist[nums[i]] = [i+1]
        
        for i in num_dist:
            if target - i in num_dist:
                if target - i == i:
                    res =[num_dist[i][0], num_dist[target-i][1]]
                else:
                    res = [num_dist[i][0], num_dist[target-i][0]]
                break
        
        if res[0] > res[1]:
            res[0], res[1] = res[1], res[0]
        
        return res



class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        ''' save some time by looking up while hashing the array
            use the python enumerate iterator
            put (target - e) in the dict instead of e 
        '''

        d = {}
        for i, e in enumerate(nums):
            if e in d:
                return d[e] + 1, i + 1
            else:
                d[target - e] = i


