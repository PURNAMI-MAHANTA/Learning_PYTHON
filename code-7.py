name = "purnami"
print(len(name))

print(name[0:7]) # purnami
print(name[:]) # It takes [0:length-1], same as print(name[0:7])
print(name[0:]) # Also same as print(name[0:7])
print(name[:7]) # Also same as print(name[0:7])

print(name[3:]) # nami, same as print(name[3:7])
print(name[3:6]) # nam, print(name[3:6]) starting value(3) is included but ending value(6) is not included.

print(name[-5:-1]) # rnam
print(name[2:6]) # rnam