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
    
  def k(self):
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.tl()
    self.m()
    self.tr()
    self.m()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.m()

  def a(self):
    self.tl()
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()

  def y(self):
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def d(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()

  def e(self):
    """print e using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()

  def n(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.tl()
    self.put5()
    
    

  def move5(self):
    self.m()
    self.m()
    self.m()
    self.m()
    self.m()

  
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.k()
    kt.a()
    kt.y()
    kt.d()
    kt.e()
    kt.n()
    pass


if __name__ == "__main__":
    run_karel_program()