class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        created_hash ={}
        created_hash2 ={}

        for char in s:
            if char not in created_hash:
                created_hash[char]=1
            else:
                created_hash[char]+=1

        for char in t:
            if char not in created_hash2:
                created_hash2[char]=1
            else:
                created_hash2[char]+=1

        if created_hash==created_hash2:
            return True
        else:
            return False