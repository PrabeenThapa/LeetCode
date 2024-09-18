class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            first, first_score, second, second_score = 'ab', x, 'ba', y
        else:
            first, first_score, second, second_score = 'ba', y, 'ab', x

        score = 0
        i = 0
        while i < len(s):
            if s[i:i+2] == first:
                score += first_score
                s = s[:i] + s[i+2:]
                i -= 1
            else:
                i += 1

        i = 0
        while i < len(s):
            if s[i:i+2] == second:
                score += second_score
                s = s[:i] + s[i+2:]
                i -= 1
            else:
                i += 1

        return score
