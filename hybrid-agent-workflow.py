import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class HybridLLMApp:
    def __init__(self):
        """
        Initialize the hybrid application with a combination of workflow steps and agent-like autonomy.
        """
        self.workflow_steps = [
            self.step_1_ask_for_topic,
            self.step_2_decide_action,
            self.step_3_execute_action,
            self.step_4_summarize_results,
        ]

    def step_1_ask_for_topic(self):
        """
        Step 1: Ask the user for a topic or task.
        """
        return input("What topic or task would you like assistance with? ")

    def step_2_decide_action(self, user_input):
        """
        Step 2: Use the LLM to decide the best action based on the user input.
        This is where the agent-like autonomy comes into play.
        """
        prompt = f"""
        The user has provided the following input: "{user_input}".
        Based on this input, decide the best action to take. Your options are:
        1. Generate a detailed explanation.
        2. Provide a step-by-step guide.
        3. Answer a specific question.
        4. Ask for clarification if the input is unclear.
        Return only the number of the chosen action.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,  # Low temperature for deterministic decisions
        )
        action = int(response['choices'][0]['message']['content'].strip())
        return action

    def step_3_execute_action(self, user_input, action):
        """
        Step 3: Execute the chosen action using the LLM.
        """
        if action == 1:
            prompt = f"Write a detailed explanation about {user_input}."
        elif action == 2:
            prompt = f"Provide a step-by-step guide for {user_input}."
        elif action == 3:
            prompt = f"Answer the following question: {user_input}"
        elif action == 4:
            return "I need more information. Can you please clarify your request?"
        else:
            return "Invalid action selected."

        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']

    def step_4_summarize_results(self, result):
        """
        Step 4: Summarize the results of the executed action.
        """
        if result.startswith("I need more information"):
            return result  # No summarization needed for clarification requests

        prompt = f"Summarize the following text in one paragraph:\n\n{result}"
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']

    def run_hybrid_app(self):
        """
        Execute the hybrid workflow step by step.
        """
        print("Welcome to the Hybrid LLM-Based Application!")
        user_input = self.step_1_ask_for_topic()
        print("\nDeciding the best action...")
        action = self.step_2_decide_action(user_input)
        print("\nExecuting action...")
        result = self.step_3_execute_action(user_input, action)
        print("\nResult:\n", result)
        print("\nSummarizing results...")
        summary = self.step_4_summarize_results(result)
        print("\nSummary:\n", summary)
        print("\nWorkflow complete. Thank you for using the app!")

# Initialize and run the hybrid app
if __name__ == "__main__":
    app = HybridLLMApp()
    app.run_hybrid_app() 