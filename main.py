#IMPORTAÇÃO DE BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

#carregando as variaveis de ambiente
load_dotenv(find_dotenv())

groq_api_key = os.getenv("GROQ_API_KEY")

#CRIAR O MODELO GROQ
llm = ChatGroq(
    model = "Gemma2-9b-It", #modelo de llm utilizado
    groq_api_key = groq_api_key, #chave de API do GROQ
)

#criar o prompt **** estudar sobre prompt engineering (few-shot, zero-shot, one-shot, chain of thoughts)
messages = [
    SystemMessage (content="Translate the following sentences from english to french")
    
]

#parser de saída: isso é necessário para que o sistema entenda a saída do modelo
parser = StrOutputParser()

#prompt template:
generic_template = "Translate the following sentences into {language}"
prompt =ChatPromptTemplate(
[
("system", generic_template),
("user","{text}")
]
)

#o que é uma chain?
# uma cadeia é uma sequencia de componentes que são executados em ordem

chain = prompt | llm | parser # serve de concatenaçãp | é um ou

#executar a chain
print(chain.invoke({'language':'German', 'text':'como você está'}))

