import openai
import asyncio
import os
import yfinance as yf
from dotenv import load_dotenv

# Load OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define companies and their stock symbols (Yahoo Finance tickers)
company_tickers = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT"
}

# Fetch real-time market data
def get_stock_data():
    stock_data = {}
    for company, ticker in company_tickers.items():
        stock = yf.Ticker(ticker)
        stock_info = stock.history(period="1d")  # Fetch latest stock data

        stock_data[company] = {
            "Stock Price": round(stock_info["Close"].iloc[-1], 2),
            "Revenue": stock.info.get("totalRevenue", "N/A"),
            "Market Sentiment": "Neutral",  # Placeholder for now
            "Risk Score": round(stock.info.get("beta", 1.0), 2)  # Beta as risk proxy
        }
    return stock_data

# Async AI functions for parallel execution
async def analyze_stock_price(company, data):
    prompt = f"""
    Analyze the real-time stock price for {company}:
    - Current Price: ${data['Stock Price']}
    
    Please provide a brief analysis of the stock price, considering:
    1. Current price movement and trading patterns
    2. What this price suggests about market confidence
    3. Key price levels and potential support/resistance points
    4. Notable implications for day traders and investors
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    return f"Stock Analysis for {company}: {response['choices'][0]['message']['content']}"

async def analyze_financials(company, data):
    prompt = f"""
    Analyze the financial metrics for {company}:
    - Total Revenue: ${data['Revenue']:,.2f}
    
    Please provide insights on:
    1. The company's revenue performance compared to industry peers
    2. Key financial strengths and potential concerns
    3. Revenue growth trajectory and sustainability
    4. Impact on company's market position
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "system", "content": prompt}]
    )
    return f"Financial Analysis for {company}: {response['choices'][0]['message']['content']}"

async def analyze_sentiment(company, data):
    prompt = f"""
    Evaluate the current market sentiment for {company}:
    - Market Sentiment: {data['Market Sentiment']}
    
    Please analyze:
    1. Current market perception and investor confidence
    2. Recent news and events affecting sentiment
    3. Social media and institutional investor sentiment
    4. Potential short-term sentiment shifts and catalysts
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return f"Sentiment Analysis for {company}: {response['choices'][0]['message']['content']}"

async def assess_risk(company, data):
    prompt = f"""
    Assess the real-time risk profile for {company}:
    - Beta (Risk Score): {data['Risk Score']}
    
    Please provide:
    1. Interpretation of the current beta value
    2. Volatility analysis compared to market average
    3. Risk factors specific to {company}'s sector
    4. Recommendations for risk management
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    return f"Risk Assessment for {company}: {response['choices'][0]['message']['content']}"

async def parallel_market_analysis():
    stock_data = get_stock_data()  # Fetch real-time data
    tasks = []
    
    for company, data in stock_data.items():
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
