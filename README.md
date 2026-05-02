# 📊 Data Analysis Agent

Este projeto é um agente inteligente de análise de dados. Ele analisa datasets em formato CSV de forma autônoma, usando banco de dados vetorial (ChromaDB) para contexto e LLMs para extrair insights por meio de agregações SQL. Ao finalizar a análise, o agente envia um relatório diretamente via email.

## 🚀 Funcionalidades

- **Análise Autônoma de Dados:** Processa arquivos CSV com limites restritos (agregações como COUNT, AVG, etc).
- **RAG e Vetorização:** Integração com ChromaDB e `SentenceTransformer` para conhecimento de contexto.
- **Geração de PDF:** Cria automaticamente um relatório em PDF usando a biblioteca `reportlab`.
- **Integração com Gmail:** Gera um relatório em PDF e dispara automaticamente como anexo para o seu email.
- **Prevenção de Loops:** Regras rígidas para evitar processamento excessivo de dados e travamentos nas chamadas de ferramentas.

## 🛠️ Tecnologias

- Python 3
- [Agno](https://github.com/agno-ai/agno) (Agentes AI)
- API Nvidia NIM (Provedor de Modelos LLM)
- ChromaDB (Banco Vetorial)
- Gmail API
- [uv](https://github.com/astral-sh/uv) (Gerenciador de pacotes)

## ⚙️ Como Rodar

1. Certifique-se de que possui as dependências instaladas via `uv`.
2. Configure as credenciais de ambiente:
   - Configure as variáveis no `.env` (ex: `EMAIL_ADDRESS`, chaves de API).
   - Coloque as credenciais do Google em `credentials/credentials.json`.
3. Rode o projeto:
   ```bash
   uv run python main.py
   ```
