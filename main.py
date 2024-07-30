def canConstruct(ransomNote, magazine):
    leftoverletters = magazine
    for letter in ransomNote:
        index = leftoverletters.find(letter)
        if index < 0:
            return False
        leftoverletters = leftoverletters[-1:index-1] + leftoverletters[index+1:]

    return True


# Example 1:
# Input: 
ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))
# Output: false

# Example 2:
# Input: 
ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))
# Output: false

# Example 3:
# Input: 
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
# Output: true
 