#space: O(1)
#Time: O(log(n))
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low=0
        n= len(citations)
        high= n -1
        while(low <= high):
        
            mid = low + int((high-low)/2)
            if citations[mid] < n - mid:
                low = mid +1
            else:
                high = mid -1

        return n - low
        
