#1
class Tool:
    def __init__(self, name):
        self.name = name
        self.call_count = 0

    def call(self):
        self.call_count += 1

    def get_info(self):
        return {
            "name": self.name,
            "call_count": self.call_count
        }
    
#2
class Agent:
    def __init__(self, name, max_retries):
        self.name = name
        self.max_retries = max_retries
        self.retry_count = 0

    def can_retry(self):
        if self.retry_count < self.max_retries:
            return True
        else:
            return False
        
    def increase_retry(self):
        if self.can_retry() == True:
            self.retry_count += 1

    def to_dict(self):
        return {
            "name": self.name,
            "max_retries": self.max_retries,
            "retry_count": self.retry_count
        }
    

#3
class Trace:
    def __init__(self, request_id):
        self.request_id = request_id
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)

    def get_event_count(self):
        return len(self.events)
    
    def to_dict(self):
        return {
            "request_id": self.request_id,
            "events": self.events,
            "event_count": self.get_event_count()
        }


#4
search = Tool("search")
weather = Tool("weather")
calculator = Tool("calculator")

search.call()
search.call()
weather.call()
calculator.call()
calculator.call()
calculator.call()

tools = []

tools.append(search)
tools.append(weather)
tools.append(calculator)

for tool in tools:
    print(tool.get_info())