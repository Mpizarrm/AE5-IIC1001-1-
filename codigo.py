import os
import time

class LCGRandomNumber :
  def __init__(self, a=16807, c=0, m=2**31-1, seed=None) :
    self.a = a
    self.c = c
    self.m = m
    
    if seed is None:
      self.x0 = int(os.getpid() + time.time())
    else :
      self.x0 = seed
    
    self.x_prev = (self.a * self.x0 + self.c) % self.m
  
  def random_number(self, num_range=None) :
    self.x_prev = (self.a * self.x_prev + self.c) % self.m
    if num_range is None :
      return self.x_prev
    else :
      return int((self.x_prev / (self.m - 1)) * (num_range[1] - num_range[0])  + num_range[0])