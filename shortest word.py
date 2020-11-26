def find_short(s):
    words = s.split()
    l = words[0]
    c = 0 
    for word in words:
      if len(word)<=len(l):
        l = word
        c +=1
    l = len(l)
    return l # l: shortest word length

print(find_short("turns out random test cases are easier than writing out basic ones"))
