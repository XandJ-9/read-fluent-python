def averager():
  total = 0
  count = 0
  while True:
    term = yield avg  # yield avg 将avg值返回给调用者，然后暂停当前线程
    total += term
    count += 1
    avg = total / count