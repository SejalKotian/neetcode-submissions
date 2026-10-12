class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we need to use sliding window to find
        #keep expanding as long as <=k replacements for the window to be valid
        #when invalid keep shrinking from left and expanding from right
        # When looking for the longest substring:
        # - Expand while valid — because a bigger valid window could improve our answer.
        # - Shrink when invalid — because an invalid window cannot be our answer, and shrinking makes room to explore different valid windows.
        # - Record the longest valid length seen throughout the process.
        # When looking for the shortest substring (like Minimum Window Substring):
        # - Expand until valid.
        # - Shrink while valid to find the smallest possible window.
        left=0
        right =0
        max_valid =0
        check={} # to avoid recalculating frequecny everytime in each window
        while (right<len(s)):
            c=s[right]
            check[c]=check.get(c,0)+1
            while (right-left+1) - max(check.values()) >k:
                check[s[left]]-=1
                left+=1
            max_valid=max(max_valid, right-left+1)
            right+=1

        return max_valid

        
                