def division(a, b):
  try: 
    if a < b:
      temp = a
      a = b
      b = temp
      return a / b
    else:
      return a / b
  except ZeroDivisionError as e:
    print(str(e))
  finally:
    if a == 0:
       a = 1
    elif b == 0:
       b = 1
  return a / b

print(division(5, 2))
print(division(2, 5))
print(division(0, 5))
print(division(2, 0))


