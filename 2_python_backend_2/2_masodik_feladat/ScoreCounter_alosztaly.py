from typing import Sequence
from Counter_osztaly import Counter

class Score_counter(Counter):
  def __init__(self, value, name, age):
      super().__init__(value)
      self.name = name
      self.age = age
      self.iswinner = False

  def increment(self):
      self.value = self.value + self.step
      if self.value >= 12:
          self.iswinner = True


myScoreCounter = Score_counter(10, 'Zsolt', 34)
myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
myScoreCounter.get_value()
print(myScoreCounter.iswinner)