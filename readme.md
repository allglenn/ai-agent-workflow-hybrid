
# LLM-Based Intelligent Agents

This project implements three different approaches to building LLM-powered applications using OpenAI's GPT models: a simple autonomous agent, a workflow-based system, and a hybrid agent-workflow system.

## Features

### 1. Simple Autonomous Agent (`simple-autonomous-agent.py`)
- Basic question-answering capabilities
- Autonomous decision-making for handling user inputs
- Configurable system prompt for defining agent behavior

### 2. Workflow-Based System (`workflow-based.py`)
- Structured, step-by-step content generation
- Topic-based learning assistance
- Automatic content summarization

### 3. Hybrid Agent-Workflow System (`hybrid-agent-workflow.py`)
- Combines autonomous decision-making with structured workflows
- Dynamic action selection based on user input
- Four different response modes:
  - Detailed explanations
  - Step-by-step guides
  - Direct question answering
  - Clarification requests

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd llm-based-agents
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to `.env`:
```bash
OPENAI_API_KEY=your-api-key-here
```

## Usage

### Simple Autonomous Agent
```bash
python simple-autonomous-agent.py
```
- Ask questions or provide statements
- Type 'exit' or 'quit' to end the session

### Workflow-Based System
```bash
python workflow-based.py
```
- Enter a topic to learn about
- Receive detailed content and a summary

### Hybrid Agent-Workflow System
```bash
python hybrid-agent-workflow.py
```
- Enter any topic or task
- The system will automatically choose the best approach to help you
- Receive detailed results and a summary

## Project Structure

```
llm-based-agents/
├── simple-autonomous-agent.py
├── workflow-based.py
├── hybrid-agent-workflow.py
├── requirements.txt
├── .env.example
├── .env
└── README.md
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Dependencies

- openai>=1.0.0
- python-dotenv>=1.0.0

## Security Notes

- Never commit your `.env` file containing your API key
- Always use environment variables for sensitive information
- The `.env` file is included in `.gitignore`

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT models
- Python community for the excellent libraries

## Support

For support, please open an issue in the repository or contact the maintainers.
