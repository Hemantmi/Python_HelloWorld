class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        arr = [0] * 26
        arr2 = [0] * 26

        for char in s:
            if(arr[ord(char)-ord('a')])>=0:
                arr[ord(char)-ord('a')]+=1
        
        for char in t:
            if(arr2[ord(char)-ord('a')])>=0:
                arr2[ord(char)-ord('a')]+=1

        if(arr==arr2):
            return True
        else:
            return False  
        