class Counter:
  def __init__(self, value):
      self.value = value
      self.step = 1

  def increment(self):
    self.value = self.value + self.step

  def decrement(self):
    self.value = self.value - self.step
  
  def set_value(self, new_value):
    self.value = new_value
  
  def set_step(self, new_step):
    self.step = new_step
  
  def get_value(self):
    print(self.value)
    return self.value

if __name__ == "__main__":
  myCounter = Counter(10)
  myCounter.increment()
  myCounter.increment()
  myCounter.get_value()
  myCounter.set_step(5)
  myCounter.decrement()
  myCounter.get_value()
  myCounter.set_value(100)
  myCounter.increment()
  myCounter.get_value()