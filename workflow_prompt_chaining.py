import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define FAQs database
FAQS = {
    "password": {
        "question": "How do I reset my password?",
        "answer": "You can reset your password by following these steps:\n1. Go to the login page\n2. Click 'Forgot Password'\n3. Enter your email address\n4. Follow the instructions in the reset email"
    },
    "business_hours": {
        "question": "What are your business hours?",
        "answer": "Our business hours are from 9 AM to 5 PM, Monday to Friday (EST). We're closed on major holidays."
    },
    "contact": {
        "question": "How do I contact support?",
        "answer": "You can contact support through multiple channels:\n- Email: support@example.com\n- Phone: +1-800-123-4567\n- Live Chat: Available during business hours"
    },
    "order_history": {
        "question": "Where can I find my order history?",
        "answer": "To view your order history:\n1. Log into your account\n2. Click on 'My Account'\n3. Select 'Order History'\n4. You'll see all past orders with details"
    }
}

def identify_issue(user_input):
    """
    Identify the type of issue from user input and match with FAQs.
    """
    # Create a context string from FAQs
    faq_context = "\n".join([f"Q: {faq['question']}\nA: {faq['answer']}" for faq in FAQS.values()])
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are a customer support assistant. Use these FAQs as reference:\n\n{faq_context}\n\nIdentify the main issue from the user's input and match it with the most relevant FAQ if applicable."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']

def generate_solution(issue):
    """
    Generate a solution based on the identified issue and FAQs.
    """
    # Create a context string from FAQs
    faq_context = "\n".join([f"Q: {faq['question']}\nA: {faq['answer']}" for faq in FAQS.values()])
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are a customer support assistant. Use these FAQs as reference:\n\n{faq_context}\n\nProvide a detailed solution for the following issue, incorporating relevant FAQ information if applicable."
            },
            {
                "role": "user",
                "content": f"Issue: {issue}"
            }
        ],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']

def check_satisfaction(solution):
    """
    Generate a follow-up question to check if the solution was helpful.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a customer support assistant. Generate a follow-up question to check if the solution was helpful and if the user needs any clarification."
            },
            {
                "role": "user",
                "content": f"Solution provided: {solution}"
            }
        ],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']

def customer_support_chatbot():
    """
    Main function to run the customer support chatbot.
    """
    print("Welcome to Customer Support! How can I assist you today?")
    print("(Type 'exit', 'quit', or 'bye' to end the conversation)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nThank you for using our customer support. Goodbye!")
            break

        # Step 1: Identify the issue
        issue = identify_issue(user_input)
        
        # Step 2: Generate a solution
        solution = generate_solution(issue)
        print(f"\nAgent: {solution}")
        
        # Step 3: Check satisfaction
        follow_up = check_satisfaction(solution)
        print(f"\nAgent: {follow_up}")

if __name__ == "__main__":
    customer_support_chatbot()