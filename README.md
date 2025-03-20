

```markdown
# Aplicação Básica Usando LLM - LCEL

Este repositório contém um exemplo de implementação de uma aplicação básica utilizando **Groq** para processamento de linguagem natural com o uso da biblioteca **LangChain**.

## Índice

1. [Criar repositório no GitHub](#criar-repositório-no-github)
2. [Configuração Local - CMD](#configuração-local---cmd)
3. [Configuração Local - VS Code](#configuração-local---vs-code)
4. [Configuração da API do Groq](#configuração-da-api-do-groq)
5. [Configuração do Ambiente de Desenvolvimento](#configuração-do-ambiente-de-desenvolvimento)
6. [Exemplo de Código](#exemplo-de-código)
7. [Arquivos de Configuração](#arquivos-de-configuração)
8. [Dependências](#dependências)
9. [Gerar requirements.txt](#gerar-requirestxt)

---

## Criar repositório no GitHub

1. Vá para [GitHub](https://github.com) e crie um novo repositório.
2. Dê um nome ao repositório e defina as permissões de visibilidade.
3. Após criar, copie a URL do repositório para clonar no seu computador.

---

## Configuração Local - CMD

1. **Crie uma nova pasta** no diretório onde deseja armazenar o projeto:

   ```sh
   mkdir AplicacaoBasica-UsandoLLM-LCEL
   ```

2. **Entre na pasta criada**:

   ```sh
   cd AplicacaoBasica-UsandoLLM-LCEL
   ```

3. **Clone o repositório do GitHub**:

   ```sh
   git clone #suaurl
   ```

4. **Abra o VS Code na pasta**:

   ```sh
   code .
   ```

---

## Configuração Local - VS Code

1. **Abra o terminal no VS Code** pressionando `Ctrl + '` (crase).

2. **Entre na pasta do projeto**:

   ```sh
   cd .\AplicacaoBasica-UsandoLLM-LCEL\
   ```

3. **Crie um ambiente virtual**:

   ```sh
   python -m venv .venv
   ```

4. **Ative o ambiente virtual**:
   - No **Windows**:
   
     ```sh
     .venv\Scripts\Activate
     ```

   - No **Linux/macOS**:
   
     ```sh
     source .venv/bin/activate
     ```

5. **Instale as dependências necessárias**:

   ```sh
   pip install langchain langchain-core langchain-groq pydotenv
   ```

---

## Configuração da API do Groq

1. **Acesse o site do Groq**: [Groq](https://groq.com/)

2. **Entre na sua conta do Groq**.

3. **Vá até as chaves de API**: [API Keys](https://console.groq.com/keys)

4. **Crie uma chave de API** clicando em "Create API Key" e copie a chave gerada.

---

## Configuração do Ambiente de Desenvolvimento

1. **Crie um arquivo `.env`** na raiz do seu projeto e insira a chave da API do Groq da seguinte forma:

   `.env`:
   ```text
   GROQ_API_KEY= #sua chave
   ```

2. **Crie o arquivo `.gitignore`** para evitar que dados sensíveis como a chave da API e o ambiente virtual sejam versionados:

   `.gitignore`:
   ```text
   .venv/
   .env
   ```

---

## Exemplo de Código

### `main.py`

```python
# IMPORTAÇÃO DE BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

# Carregando as variáveis de ambiente
load_dotenv(find_dotenv())

groq_api_key = os.getenv("GROQ_API_KEY")

# CRIAR O MODELO GROQ
llm = ChatGroq(
    model="Gemma2-9b-It",  # Modelo de LLM utilizado
    api_key=groq_api_key,   # Chave de API do Groq
)

# Criar o prompt (estudar sobre prompt engineering - few-shot, zero-shot, one-shot, chain of thoughts)
messages = [
    SystemMessage(content="Translate the following sentences from english to french")
]

# Parser de saída: Isso é necessário para que o sistema entenda a saída do modelo
parser = StrOutputParser()

# Prompt template
generic_template = "Translate the following sentences into {language}"
prompt = ChatPromptTemplate(
    [
        ("system", generic_template),
        ("user", "{text}")
    ]
)

# Definindo a Chain (sequência de componentes executados em ordem)
chain = prompt | llm | parser  # A concatenação é feita com '|'

# Executar a chain
print(chain.invoke({'language': 'German', 'text': 'como você está'}))
```

---

## Arquivos de Configuração

### `.env`

```text
GROQ_API_KEY=
```

### `.gitignore`

```text
.venv/
.env
```

### `requirements.txt`

```sh
langchain
langchain-core
langchain-groq
pydotenv
```

---

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```sh
pip install -r requirements.txt
```

---

## Gerar requirements.txt

Caso queira gerar um novo arquivo `requirements.txt` com as dependências instaladas, execute:

```sh
pip freeze > requirements.txt
```

---

Este README proporciona uma explicação completa e detalhada do processo de configuração do projeto, desde a criação do repositório até a execução do código. Se você encontrar algum erro ou precisar de mais ajuda, sinta-se à vontade para abrir um "issue" no repositório! 🚀
```

---
