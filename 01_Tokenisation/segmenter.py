import re
import sys
line = sys.stdin.readline()
sent = re.split(r'[.!?]', line)  
lis = []   
for sentence in sent:
    seg = sentence.strip().split()
    lis.append(seg)
print(lis)

