class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for j in range (len(nums2)):
            nums1.append(nums2[j])
            
        nums1.sort()   
        
        l = len(nums1)
        if l%2==0:
            return (((nums1[(l//2)-1]+ nums1[(l//2)])/2))
                   
                
        else:
            return (nums1[l//2])
        
