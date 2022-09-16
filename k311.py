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
    self.move()
    self.put2()
    self.move()
    self.put()

  def move4(self):
    self.m()
    self.m()
    self.m()
    self.m()
    
  def move3(self):
    self.m()
    self.m()
    self.m()
    
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.move4()
    kt.tl()
    kt.move4()
    kt.put()
    kt.tl()
    kt.move3()
    kt.tr()
    kt.m()
    kt.tr()
    kt.move3()
    kt.put()
    kt.tl()
    kt.move3()
    kt.tr()
    kt.m()
    kt.tr()
    kt.move3()
    kt.put()
    kt.tl()
    kt.move3()
    kt.tr()
    kt.m()
    kt.tr()
    kt.move3()
    kt.put()
    kt.tl()
    kt.move4()
    kt.tr()
    kt.move4()
    kt.m()
    kt.tr()
    kt.tr()
    pass


if __name__ == "__main__":
    run_karel_program()

  