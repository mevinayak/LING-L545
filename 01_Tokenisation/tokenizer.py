import sys
import string
text = sys.stdin.readline()
sc = []
tokens = text.split()

  # Remove punctuation and make all tokens lowercase
tokens = [token.lower().strip(string.punctuation) for token in tokens]

  # Remove any remaining empty tokens
tokens = [token for token in tokens if token]

print(tokens)
