class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_map = {}

        arr1_str = [str(x) for x in arr1]
        arr2_str = [str(x) for x in arr2]
        
        # Step 1: Build the prefix map for arr1
        for str_num in arr1_str:
            prefix = ""
            for ch in str_num:
                prefix += ch
                prefix_map[prefix] = 0
                
        max_length = 0
        
        # Step 2: Check for common prefixes in arr2
        for str_num in arr2_str:
            prefix = ""
            for ch in str_num:
                prefix += ch
                if prefix in prefix_map:
                    max_length = max(max_length, len(prefix))
        
        return max_length
