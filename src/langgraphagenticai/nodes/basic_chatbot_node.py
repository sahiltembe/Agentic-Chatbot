from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot login implementation
    """

    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Proccess the input state and generates a chatbot response. 
        """

        return {"messages":self.llm.invoke(state['messages'])}