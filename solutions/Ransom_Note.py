class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)
        
        for k, v in note_count.items():
            if k not in mag_count or mag_count[k] < v:
                return False
        return True