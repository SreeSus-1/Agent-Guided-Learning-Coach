from agents.base_agent import BaseAgent

class ExplainerAgent(BaseAgent):

    def explain(self, topic):

        prompt = f"""
        You are an expert tutor.

        Explain the concept of {topic} in simple terms.

        Include examples and step-by-step explanation.
        """

        return self.call_ollama(prompt)