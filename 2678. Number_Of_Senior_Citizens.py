class Solution:
    def countSeniors(self, records: List[str]) -> int:
        senior_count = 0
        for record in records:
            age_str = record[11:13]
            if age_str > '60':
                senior_count += 1
        return senior_count