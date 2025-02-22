# Stock Analysis Dashboard & Financial Analyst Agent

An advanced, AI-powered financial analysis tool that combines market data retrieval, technical charting, and natural language insights. This project leverages cutting-edge technologies and frameworks to deliver sophisticated analyses, actionable recommendations, and comprehensive market insights—all within an interactive dashboard.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technologies & Frameworks](#technologies--frameworks)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [File Structure](#file-structure)
- [Author](#author)
- [License](#license)

---

## Overview

This project provides a complete solution for stock analysis by integrating historical market data, interactive visualizations, and AI-driven insights. At its core is the **Financial Analyst Agent**, which leverages the power of **Google Gemini 2.0 Flash** to process user queries, assess market trends, and generate clear, actionable recommendations. The accompanying **Streamlit** dashboard offers an intuitive user interface to explore stock data, visualize candlestick charts, and interact with the AI agent.

---

## Key Features

- **Real-Time Stock Data:** Integrates with **Yahoo Finance** to fetch up-to-date market data.
- **Interactive Visualizations:** Utilizes **Plotly** to generate dynamic candlestick charts and data tables.
- **AI-Driven Analysis:** Powered by **Google Gemini 2.0 Flash**, offering detailed insights, risk assessments, and investment strategies.
- **Configurable Parameters:** Customizable parameters through a YAML configuration file for ease of updates and modifications.
- **Analyst Recommendations:** Combines historical data with AI analytics to provide sophisticated market analysis and actionable recommendations.
- **Company News & Historical Context:** While primarily focused on data trends and market analysis, the agent framework can be extended to include company news and previous data analysis for a more rounded view.
- **User-Friendly Dashboard:** Built with **Streamlit** for rapid deployment and a responsive, intuitive UI.
- **Modular and Extensible:** Clean architecture and modular code design facilitate easy integration of additional data sources and analytical tools.

---

## Architecture

### Data Flow & Components

1. **Data Acquisition:**  
   - **Yahoo Finance (yfinance):** Downloads historical stock data.
   - **CSV Ticker List:** Retrieves valid stock tickers via a YAML-configured URL.
2. **Data Visualization:**  
   - **Plotly:** Generates interactive candlestick charts.
3. **AI-Powered Analysis:**  
   - **Financial Analyst Agent:** Uses **Google Gemini 2.0 Flash** for processing queries.
   - **Phidata Integration:** Facilitates data handling and tool management, ensuring robust analytics.
4. **User Interaction:**  
   - **Streamlit Dashboard:** Provides an interface for ticker selection, query submission, and data display.
5. **Configuration & Parameters:**  
   - **YAML File (`params.yaml`):** Stores essential parameters like the model ID, agent description, instructions, and ticker list URL.


## Technologies & Frameworks

- **Python:** Core programming language.
- **Google Gemini 2.0 Flash:** State-of-the-art language model used for deep financial analysis and generating recommendations.
- **Phidata:** Tool for integrating multiple data sources and analytical frameworks, enabling a seamless connection between market data and AI insights.
- **Yahoo Finance (yfinance):** API wrapper for accessing historical and real-time stock data.
- **Plotly:** Library for creating high-quality, interactive financial charts.
- **Streamlit:** Framework for rapidly building and deploying interactive dashboards.
- **YAML:** Configuration management for easy updates to parameters and settings.
- **Dataclasses:** Simplifies configuration management with Python data classes.
- **dotenv:** Manages environment variables for secure configuration.
- **Additional Libraries:**  
  - **PyYAML:** For parsing YAML files.
  - **python-dotenv:** For handling environment variables.

---

## Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/stock-analysis-dashboard.git
   cd stock-analysis-dashboard
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**

   - Create a `.env` file in the project root and add any necessary environment variables.

5. **Run the Dashboard:**

   ```bash
   streamlit run main.py
   ```

---

## Usage

- **Dashboard Interaction:**  
  Use the sidebar to select a stock ticker or search for a specific ticker. The main panel displays historical data and an interactive candlestick chart.
- **AI Agent Query:**  
  Enter your questions regarding market trends, risk analysis, or investment strategies in the designated text area. Submit your query to receive detailed, AI-powered insights.
- **Custom Analysis:**  
  The Financial Analyst Agent uses the configured parameters to tailor its analysis, ensuring that the recommendations are both precise and actionable.

---

## Configuration

### `params.yaml`

This file contains crucial configuration parameters:

- **modelId:**  
  Specifies the version of the **Google Gemini 2.0 Flash** model to use (e.g., `gemini-2.0-pro-exp-02-05`).
- **description:**  
  Outlines the capabilities and focus of the AI agent, emphasizing data-driven, analytical approaches.
- **instructions:**  
  Provides guidance on leveraging all available tools and data sources for comprehensive financial analysis.
- **tickerListUrl:**  
  URL pointing to a CSV file with valid stock tickers.

### Environment Variables

- Managed via a `.env` file using **python-dotenv**.
- Ensure sensitive data and API keys (if any) are stored securely.

---

## File Structure

```
├── LICENSE
├── main.py                   # Entry point for the Streamlit dashboard
├── financeAnalystAgent.py    # Defines the Financial Analyst Agent
├── params.yaml               # YAML configuration file for agent parameters
├── requirements.txt          # List of Python dependencies
└── utils.py                  # Utility functions for fetching data and generating charts
```

---

## Author

🔗 **Portfolio & Contact Information**:  
- 🌍 Website: [rauhanahmed.org](https://rauhanahmed.org)  
- 🏢 GitHub: [github.com/rauhanAhmed](https://github.com/rauhanAhmed)  
- 💼 LinkedIn: [linkedin.com/in/rauhan-ahmed](https://www.linkedin.com/in/rauhan-ahmed)  
- 🐦 Twitter (X): [x.com/ahmed_rauh46040](https://x.com/ahmed_rauh46040)  
- 📧 Email: [rauhaan.siddiqui@gmail.com](mailto:rauhaan.siddiqui@gmail.com)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Explore, analyze, and gain insights from the financial markets with a blend of powerful data, state-of-the-art AI, and interactive visualizations. This project is designed to support investors, analysts, and enthusiasts in making informed decisions backed by rigorous analysis and actionable recommendations.

Happy Analyzing!