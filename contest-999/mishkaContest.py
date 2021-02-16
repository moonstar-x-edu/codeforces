import sys
input = sys.stdin.readline

def read():
  return map(int, input().split())

(n, k) = tuple(read())
l = list(read())

first = 0
last = len(l) - 1

for i in range(0, len(l)):
  if l[i] > k:
    break

  first = i + 1

for i in range(1, len(l) + 1):
  if l[-i] > k:
    break

  last = len(l) - i - 1

print(len(l) if last < first else first + (len(l) - last - 1))