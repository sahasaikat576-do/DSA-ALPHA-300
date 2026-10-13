class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        window_size = len(s1)
        for i in range(len(s2)-window_size+1):
            if sorted(s1)== sorted(s2[i:window_size+i]):
             return True
        return False


