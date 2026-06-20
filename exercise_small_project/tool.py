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
    