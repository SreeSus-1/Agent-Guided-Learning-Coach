from agents.base_agent import BaseAgent

class MotivationAgent(BaseAgent):

    def motivate(self, topic):

        prompt = f"""
        You are a supportive learning coach.

        Provide encouragement and study advice for someone learning:

        {topic}

        Keep the tone positive and motivating.
        """

        return self.call_ollama(prompt)