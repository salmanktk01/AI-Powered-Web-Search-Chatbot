import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun #duck search things from the whole internet
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os 
from dotenv import load_dotenv

groq_api_key=os.getenv("GROQ_API_KEY")

#arxivwrapper
api_wrapper_arxic=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)
Arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxic) #you need to run this 


#wikipediawrapper
api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki) #you need to run this 


st.title("LangChain - Chat with search")

#sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")

search=DuckDuckGoSearchRun(name="search") #giving the task we are giving to him 



if "messages" not in st.session_state:   #when starting their no messages so we this ,sessionsate basically dictonary hai and yeh ap ki state koa maintain rakh they hai 
    st.session_state["messages"]=[
        {"role":"assitant","content":"Hi,I'm a chatbot who can search from the  web .how can i help you"}
    ]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt:=st.chat_input(placeholder="What is machine learning?"):  #walrus operator ,here what we are doing is ka jao mesages placeholder se aya rah hai ,yeh woe kry gy 
   st.session_state.messages.append( {"role":"user","content":prompt})
   st.chat_message("user").write(prompt) #creata a chatbubble with the user jao poucha hai 
   llm=ChatGroq(model="Gemma2-9b-it",groq_api_key="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",streaming=True)
   tools=[search,Arxiv,wiki]
   search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

   with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False) #agr kes koa chiya toh he/she needs to expands those messages by himself
        response=search_agent.run(st.session_state.messages,callbacks=[st_cb]) #entire chathistory aya jay gy 
        st.session_state.messages.append({'role':'assistant',"content":response}) #respisen milyea gy 
        st.write(response)

