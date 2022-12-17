import sys
import string
text = sys.stdin.readline()
tk = text.split()
tk = [i.lower().strip(string.punctuation) for i in tk]
tk = [i for i in tk if i]
print(tk)
