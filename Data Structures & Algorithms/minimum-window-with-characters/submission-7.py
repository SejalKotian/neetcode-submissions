class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # shortest one
        # we need a contiguous one
        # we need it to satisfy the condition

        # brute force
        # generate every possible substring of s
        # check whether it contains every character in t
        # keep track of the shortest valid substring
        
        # expand the window util it becomes valid and then shrink it find the shortest valid
        #how to know if a window is valid - use freq hashmaps

        #create a frequency map of t
        need ={}
        for c in t:
            need[c]=need.get(c,0)+1

        #we need freq map of charcaters in teh current window
        window={}
        left=0
        formed=0 #number of distinct character reqs currently satisfied
        required=len(need) #distinct characters in t
        min_len = float("inf") #(length of the shortest valid window formed)
        min_start =0 #starting index of the window

        for right in range(len(s)):
            c=s[right]
            window[c]=window.get(c,0)+1
            if c in need and window[c]==need[c]:
                formed+=1
            while formed==required:
                if right-left +1 <min_len:
                    min_len = right - left + 1
                    min_start =left
                #start removing the leftmost charcter
                removed = s[left]
                window[removed]-=1

                #check all reqs still meet
                if removed in need and window[removed]<need[removed]:
                    formed -=1
                left +=1
        if min_len == float("inf"):
            return ""
        return s[min_start:min_start+min_len]

