class CatchEvents(Exception):
  def __init__(self, *args: object) -> None:
    print("I got your call to fire the event and I am doing it")
    self.action()
  def action(self):
    print("Well this is embarassing, I am a naked action")



class SomeEvent(CatchEvents):
  def action(self):
    print("I am some event and I am doing something")


def fire(event:CatchEvents):
  try:
    raise event
  except CatchEvents as ex:
    pass #Well once you are done, you don't need to keep it


fire(SomeEvent)
fire(CatchEvents)

print("Something")