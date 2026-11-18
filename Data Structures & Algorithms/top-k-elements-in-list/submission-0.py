class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_ele = set(nums)
        fre_map = {}
        for i in nums:
            fre_map[i] = 0
        for i in nums:
            fre_map[i]+=1
        sorted_by_value_asc = dict(sorted(fre_map.items(), key=lambda item: item[1]))
        key_list = list(sorted_by_value_asc.keys())
        return key_list[-k:]
    


        