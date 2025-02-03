import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class WorkflowBasedApp:
    def __init__(self):
        """
        Initialize the workflow-based application with predefined steps.
        """
        self.workflow_steps = [
            self.step_1_ask_for_topic,
            self.step_2_generate_content,
            self.step_3_summarize_content,
        ]

    def step_1_ask_for_topic(self):
        """
        Step 1: Ask the user for a topic.
        """
        return input("Please enter a topic you'd like to learn about: ")

    def step_2_generate_content(self, topic):
        """
        Step 2: Generate content about the topic using the LLM.
        """
        prompt = f"Write a detailed explanation about {topic}."
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']

    def step_3_summarize_content(self, content):
        """
        Step 3: Summarize the generated content using the LLM.
        """
        prompt = f"Summarize the following text in one paragraph:\n\n{content}"
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']

    def run_workflow(self):
        """
        Execute the workflow step by step.
        """
        print("Welcome to the Workflow-Based LLM Application!")
        topic = self.step_1_ask_for_topic()
        print("\nGenerating content...")
        content = self.step_2_generate_content(topic)
        print("\nContent Generated:\n", content)
        print("\nSummarizing content...")
        summary = self.step_3_summarize_content(content)
        print("\nSummary:\n", summary)
        print("\nWorkflow complete. Thank you for using the app!")

# Initialize and run the workflow-based app
if __name__ == "__main__":
    app = WorkflowBasedApp()
    app.run_workflow() 