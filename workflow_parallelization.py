import openai
import asyncio
import random
import os
from dotenv import load_dotenv

# Load OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Mock financial market data with natural language descriptions
companies = [
    "Apple Inc.", 
    "Tesla Motors", 
    "Microsoft Corporation",
    "Amazon.com Inc."
]

market_data = {
    company: {
        "Current Stock Price": round(random.uniform(50, 500), 2),
        "Quarterly Revenue (Billions)": round(random.uniform(10, 100), 2),
        "Market Sentiment": random.choice([
            "Strongly Bullish",
            "Moderately Bullish",
            "Neutral",
            "Moderately Bearish",
            "Strongly Bearish"
        ]),
        "Investment Risk Level": {
            "score": round(random.uniform(1, 10), 1),
            "category": random.choice([
                "Very Low Risk",
                "Low Risk",
                "Moderate Risk",
                "High Risk",
                "Very High Risk"
            ])
        }
    }
    for company in companies
}

# Async functions for parallel execution
async def analyze_stock_price(company, data):
    """ Uses GPT-4-Turbo to analyze stock trends """
    prompt = f"""
    Analyze the current stock price for {company}:
    - Current Price: ${data['Current Stock Price']}
    
    Please provide a brief analysis of the stock price, considering:
    1. Whether this price point represents good value
    2. What this price suggests about the company's market position
    3. Any notable implications for investors
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": prompt}],
    )
    return f"Stock Analysis for {company}: {response['choices'][0]['message']['content']}"

async def analyze_financials(company, data):
    """ Uses GPT-3.5-Turbo-16k for financial report analysis """
    prompt = f"""
    Analyze the quarterly financial performance of {company}:
    - Quarterly Revenue: ${data['Quarterly Revenue (Billions)']} billion
    
    Please provide insights on:
    1. The revenue scale relative to industry standards
    2. What this revenue suggests about company growth
    3. Potential financial outlook based on this revenue
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "system", "content": prompt}],
    )
    return f"Financial Analysis for {company}: {response['choices'][0]['message']['content']}"

async def analyze_sentiment(company, data):
    """ Uses GPT-4 for sentiment analysis """
    prompt = f"""
    Evaluate the market sentiment for {company}:
    - Current Sentiment: {data['Market Sentiment']}
    
    Please analyze:
    1. What this sentiment level typically indicates
    2. Potential factors contributing to this sentiment
    3. How this sentiment might affect short-term trading
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
    )
    return f"Sentiment Analysis for {company}: {response['choices'][0]['message']['content']}"

async def assess_risk(company, data):
    """ Uses GPT-3.5-Turbo for risk assessment """
    prompt = f"""
    Assess the investment risk profile for {company}:
    - Risk Score: {data['Investment Risk Level']['score']}/10
    - Risk Category: {data['Investment Risk Level']['category']}
    
    Please provide:
    1. An interpretation of the risk score and category
    2. What this risk level means for different types of investors
    3. How this risk profile compares to typical market standards
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
    )
    return f"Risk Assessment for {company}: {response['choices'][0]['message']['content']}"

async def parallel_market_analysis():
    """ Runs all AI models in parallel """
    tasks = []
    for company, data in market_data.items():
        tasks.append(analyze_stock_price(company, data))
        tasks.append(analyze_financials(company, data))
        tasks.append(analyze_sentiment(company, data))
        tasks.append(assess_risk(company, data))

    results = await asyncio.gather(*tasks)
    return results

# Run the AI analysis
if __name__ == "__main__":
    analysis_results = asyncio.run(parallel_market_analysis())
    print("\n".join(analysis_results))
