word1 = 'shinchan'
word2 = "Tom"
word3 = '''Jerry'''
print(type(word1))
print(type(word2))
print(type(word3))

print(len(word1))
print(len(word2))
print(len(word3))

# Slicing with skip value
print(word1[1:7]) # hincha
print(word1[1:7:2]) # hnh

# some advance techniques
print(word1[:8]) # same as print(word1[0:8])
print(word1[0:]) # same as print(word1[0:8])