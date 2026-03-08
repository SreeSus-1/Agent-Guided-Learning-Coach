from agents.base_agent import BaseAgent

class QuizAgent(BaseAgent):

    def generate_quiz(self, topic):

        prompt = f"""
        Create 3 quiz questions to test understanding of:

        {topic}

        Include answers.
        """

        return self.call_ollama(prompt)