# Search-Engine
This project allows users to interact with a chatbot that can search the web, fetch information from Arxiv, Wikipedia, and perform general web searches using DuckDuckGo. The chatbot integrates with Groq's Gemma2-9b-it model for natural language processing, enabling intelligent responses based on real-time searches.

Features
Natural Language Queries: Ask questions in natural language and get answers in real-time.
Web Search: The chatbot can search the web via DuckDuckGo, providing broad search capabilities.
Arxiv Search: It can retrieve academic papers from Arxiv based on your queries, making it ideal for researchers.
Wikipedia Search: The chatbot also pulls information from Wikipedia to answer a variety of questions.
Customizable: You can configure the Groq API key and the chatbot’s behavior via the sidebar.
Technologies Used
LangChain: For building the agent-based chatbot with multiple data sources.
Groq API: To power the Gemma2-9b-it language model for generating responses.
Streamlit: For creating the user-friendly interface for chatting and interacting with the bot.
ArxivAPIWrapper: To fetch academic papers from Arxiv.
WikipediaAPIWrapper: To pull content from Wikipedia for answering queries.
DuckDuckGo: For general web search integration.
