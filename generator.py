import markovify
import sys
if len(sys.argv) != 2:
    sys.exit("Usage: python generator.py sample.txt")
with open(sys.argv[1]) as f:
    text = f.read()
model = markovify.Text(text)
print()
for i in range(5):
    print(model.make_sentence())
    print()
