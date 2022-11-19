"""
Goal:
To create event based execution
"""

class EventManager():
  def __init__(self) -> None:
     self.action_list = {}

  """
  Takes an event name as parameter.
  """
  def action(self,name,func=None):
    if func is not None:
      self.__add_action(name,func)
    else:
      def wrapper(func):
        self.__add_action(name,func)
        return func
      return wrapper
  
  def __add_action(self, name, func):
    print(f"adding event {name} to action")
    if name not in self.action_list:
        self.action_list[name] = func
    else:
        raise Warning("You are replacing an existing action")

  def catch(self,name):
    if name not in self.action_list:
      print("Event not found")
      print(self.action_list)
    else:
      self.action_list[name]()
    

em = EventManager()

"""
em.action(event_name)
def action_name():
  ...
"""


@em.action("start_show")
def raise_curtains():
  print("Raising curtains")

@em.action("stop_show")
def drop_curtains():
  print("Show stopped")

em.catch("start_show")


