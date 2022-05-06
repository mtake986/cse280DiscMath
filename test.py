def xor(p, q):
  print(f'{p} ^ {q} = {p ^ q}')
  return not q if p else q

actual = [
  True ^ True,
  True ^ False,
  False ^ True,
  False ^ False,
  xor(True, True),
  xor(True, False),
  xor(False, True),
  xor(False, False)
]
expected = [
  False, True,
  True, False,
  False, True,
  True, False
]
print(actual == expected)