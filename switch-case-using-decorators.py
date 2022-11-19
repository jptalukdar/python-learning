class Switch():
    def __init__(self):
        self.mapping_dict= {}
        self.defaultCase = None

    def default(self):
        def wrapper(func):
            if self.defaultCase == None:
                self.defaultCase = func
                return func
            else:
                raise Exception('Duplicate default')
        return wrapper

    def case(self,name):
        print(f"adding case, {name}")
        def wrapper(func):
            print(f"adding method, {name}, {func}")
            if name not in self.mapping_dict:
                self.mapping_dict[name] = func
            else:
                raise Exception('Duplicate case detected')
            return func
        return wrapper
    
    def match(self,name):
        method = self.mapping_dict.get(name,None)
        if method != None:
            return method()
        else:
            if self.defaultCase == None:
                raise Exception('Unknown Case received')
            else:
                return self.defaultCase()
    

switch = Switch()

@switch.case(1)
def processFirstPrize():
  print('processFirstPrize')

@switch.case(2)
def processSecondPrize():
  print('processSecondPrize')

@switch.case(3)
def processThirdPrize():
  print('processThirdPrize')

@switch.case(4)	
def processFourthPrize():
  print('processFourthPrize')

@switch.case(5)
def processFifthPrize():
  print('processFifthPrize')

@switch.default()
def processDefaultChoice():
  print('processDefaultChoice')

switch.match(1)