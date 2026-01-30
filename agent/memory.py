class AgentMemory:
    def __init__(self):
        self.history = []

    def save(self, entry):
        self.history.append(entry)
