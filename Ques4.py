counter = 1
def dolots(count):
  global counter
  for i in (1, 2, 3):
    counter = count + i

dolots(4)
print counter
