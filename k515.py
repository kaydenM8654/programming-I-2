from stanfordkarel import *


class ktools: 
  def m(self):
    """shorthand for move"""
    move()

  def tl(self):
    """turn left"""
    turn_left()

  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """pick beeper"""
    pick_beeper()

  def put(self):
    """put beeper"""
    put_beeper()

  def put2(self):
    """2 beepers on a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """put 5 beepers in a row"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """print h using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def move4(self):
    self.m()
    self.m()
    self.m()
    self.m()

  def fic(self):
    """front is cleared"""
    return front_is_clear()


  def fib(self):
    """front is blocked"""
    return not self.fic()

  def ric(self):
    """right is cleared"""
    self.tr()
    if self.fic():
      self.tl()
      return True
    self.tl()
    return False

  def rib(self):
    """right is blocked"""
    return not self.ric()

  def mazemove(self):
    """maze move"""
    if self.fib():
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass

  def mm(self, num):
    """move multiple"""
    for number in range(num):
      self.m()

  def pickm(self, num):
    """pick multiple"""
    for i in range(num-1):
      self.pick()
      self.m()
    self.pick()

  def putm(self, num):
    """put multiple"""
    for _ in range(0, num-1):
      self.put()
      self.m()
    self.put()

  def SOB(self):
    """standing on beeper"""
    return beepers_present()

  def jump(self):
    """jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
    """find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.SOB():
        self.m()
        self.tl()
        self.m()
    pass

def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.m()
    kt.tl()
    kt.m()
    kt.tr()
    kt.m()
    while kt.SOB():
      kt.pick()
      kt.find()
    pass


if __name__ == "__main__":
    run_karel_program()