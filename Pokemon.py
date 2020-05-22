
class Pokemon(object):
  def __init__(self, name):
    self.name = name
  
  def gruesse(self):
    print("%s sagt hallo ..." % self.name)