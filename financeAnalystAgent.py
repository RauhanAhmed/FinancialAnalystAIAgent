# Import necessary modules
from phi.tools.yfinance import YFinanceTools
from phi.model.google import Gemini
from dataclasses import dataclass
from phi.agent import Agent
import yaml
import os

# Configuration class for Financial Analyst Agent
@dataclass
class FinancialAnalystAgentConfig:
    paramsPath: str = os.path.join(os.getcwd(), "params.yaml")  # Path to the parameters file

# Main class for the Financial Analyst Agent
class FinancialAnalystAgent:
    def __init__(self):
        # Load configuration settings
        self.financialAnalystAgentConfig = FinancialAnalystAgentConfig()
        with open(self.financialAnalystAgentConfig.paramsPath, "rb") as params:
            self.params = yaml.safe_load(params)  # Load YAML parameters into a dictionary

    def chatbot(self, userQuery: str) -> str:
        # Initialize the finance agent with model and tool settings
        financeAgent = Agent(
            name="Finance Agent",
            description=self.params.get("description"),  # Set agent description from config
            model=Gemini(
                id=self.params.get("modelId")  # Load model ID from parameters
            ),
            tools=[
                YFinanceTools(enable_all=True)  # Enable all financial tools
            ],
            instructions=[
                self.params.get("instructions")  # Load instructions for the agent
            ],
            markdown=True  # Enable markdown formatting in responses
        )
        
        # Run the agent with the user query and return the response
        response = financeAgent.run(userQuery)
        return response.to_dict()["messages"][-1]["content"]  # Extract the last message content