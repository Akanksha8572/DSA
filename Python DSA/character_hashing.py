s = "a z,a,q,w,e,r,e,w,e,r,t,y,u,i,o"
q = ["d", "a", "d", "e"]
hash_list = [0] * 26  # Only 26 letters: a to z

for ch in s:
    if 'a' <= ch <= 'z':
        ascii_val = ord(ch)
        index = ascii_val - 97
        hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])