class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0


        str_nums = list(map(str, nums))
        
        str_nums.sort(key=cmp_to_key(compare))
    
        largest_num = ''.join(str_nums)
        return '0' if largest_num[0] == '0' else largest_num