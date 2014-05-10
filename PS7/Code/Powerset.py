memo = {}
memo[0] = []
def powerset(n):
  if n in memo.keys():
    return n
  rep = []
  for i in range(n):
    if i in memo.keys():
      rep += [i]
    else:
      result = powerset(i)
      memo[i] = result
      rep += [result]
  for i, x in enumerate(rep):
    if x in memo.values():
      rep[i] = i
  return rep

final = powerset(4)

