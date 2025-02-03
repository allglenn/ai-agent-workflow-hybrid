import openai

# Set up OpenAI API key
openai.api_key = "your-openai-api-key"

class SimpleAutonomousAgent:
    def __init__(self, system_prompt):
        """
        Initialize the agent with a system prompt that defines its behavior.
        """
        self.system_prompt = system_prompt

    def generate_response(self, user_input):
        """
        Generate a response based on the user input and the agent's system prompt.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,  # Controls randomness; lower values make responses more deterministic
        )
        return response['choices'][0]['message']['content']

    def decide_action(self, user_input):
        """
        Decide the best action based on the user input.
        This is where the agent's autonomy comes into play.
        """
        # Example: The agent decides whether to answer a question or ask for clarification
        if "?" in user_input:
            return self.generate_response(user_input)
        else:
            return "I need more information. Can you please ask a question or provide more details?"

# Define the agent's system prompt
system_prompt = """
You are a helpful and autonomous AI assistant. Your goal is to assist users by answering their questions, 
providing recommendations, or solving problems. If the user input is unclear, ask for clarification. 
Be concise and helpful in your responses.
"""

# Initialize the agent
agent = SimpleAutonomousAgent(system_prompt)

# Simulate a conversation with the agent
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye!")
        break
    response = agent.decide_action(user_input)
    print(f"Agent: {response}")