def words_in_dict(dictionary, text):
    goodwords = set(dictionary)
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos + 1:])
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans
# O(NK + M)
