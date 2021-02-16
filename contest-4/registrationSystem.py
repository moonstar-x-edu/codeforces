def req(db, name):
  value = db.get(name)

  if value != None:
    db[name] += 1
    return "{0}{1}".format(name, value + 1)
  
  db[name] = 0
  return 'OK'

n = int(input())
db = {}

res = [req(db, input()) for _ in range(0, n)]

for x in res:
  print(x)