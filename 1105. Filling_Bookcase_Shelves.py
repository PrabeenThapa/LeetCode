from typing import List
from functools import lru_cache
from math import inf

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        
        @lru_cache(None)
        def calculate_min_height(index: int, current_width: int, current_height: int) -> int:
            if index == len(books):
                return 0
            
            book_width, book_height = books[index]
            current_width += book_width
            min_height = inf

            if current_width <= shelf_width:
                if book_height <= current_height:
                    min_height = calculate_min_height(index + 1, current_width, current_height)
                else:
                    min_height = min(min_height, book_height - current_height + calculate_min_height(index + 1, current_width, book_height))

            return min(min_height, book_height + calculate_min_height(index + 1, book_width, book_height))

        return calculate_min_height(0, 0, 0)
