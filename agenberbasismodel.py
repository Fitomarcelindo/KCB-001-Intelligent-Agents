class ModelBasedReflexAgent:
    def __init__(self):
        self.current_state = None
        self.model = {}

    def update_model(self, percept):
        if(percept ==  "dirty"):
            self.model[percept] = True
        else:
            self.model[percept] = False
            

    def update_state(self, percept):
        if percept in self.model:
            self.current_state = self.model[percept]

    def select_action(self):
        if self.current_state == True:
            action = "clean"
        else:
            action = "move"

        return action

def model_based_reflex_agent(percept):
    agent = ModelBasedReflexAgent()
    agent.update_model(percept)
    agent.update_state(percept)
    action = agent.select_action()

    return action

# Contoh penggunaan:
percept = input("")
action = model_based_reflex_agent(percept.lower())
print(action) 
