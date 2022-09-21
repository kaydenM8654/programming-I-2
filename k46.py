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

  

def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.tl()
    kt.m()
    kt.mazemove()
    kt.m()
    kt.ta()
    kt.mazemove()
    kt.tl()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.mazemove()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.tl()
    kt.m()
    kt.mazemove()
    kt.m()
    kt.tl()
    kt.m()
    kt.tl()
    kt.m()
    kt.mazemove()
    kt.m()
    kt.tl()
    pass


if __name__ == "__main__":
    run_karel_program()