import os
import streamlit as st
from groq import Groq

# Configuração da página no Streamlit
st.set_page_config(
    page_title="CidadãoClaro IA",
    page_icon="🏛️",
    layout="centered"
)

# Título e Introdução
st.title("🏛️ CidadãoClaro IA")
st.caption("Transparência Ativa e Linguagem Simples no Setor Público (Powered by Groq)")
st.markdown("---")

st.markdown("""
### Como funciona?
Cole abaixo o texto de um **despacho, notificação municipal ou documento jurídico**. 
A IA vai traduzir o conteúdo em linguagem simples, listar o que você precisa fazer e citar a fonte oficial.
""")

# Campo de entrada de texto
documento_texto = st.text_area(
    label="Texto do Documento Público:",
    height=200,
    placeholder="Cole aqui o texto do despacho ou documento burocrático..."
)

# Chave de API do Groq
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    api_key = st.sidebar.text_input("Sua Groq API Key:", type="password")

# Botão de Ação
if st.button("✨ Traduzir para Linguagem Simples", type="primary"):
    if not documento_texto.strip():
        st.warning("Por favor, cole um texto antes de continuar.")
    elif not api_key:
        st.error("Insira sua API Key do Groq na barra lateral para prosseguir.")
    else:
        with st.spinner("Analisando o documento com o Groq..."):
            try:
                client = Groq(api_key=api_key)

                system_prompt = """
Você é o "CidadãoClaro IA", um assistente de transparência pública treinado para traduzir documentos governamentais e jurídicos complexos para linguagem simples (acessível a pessoas com nível de escolaridade fundamental).

REGRAS OBRIGATÓRIAS:
1. Use frases curtas, voz ativa e substitua todo termo técnico por palavras do dia a dia.
2. Baseie-se APENAS nas informações fornecidas no documento. Não invente nada.
3. Você apenas explica o documento; deixe claro que não toma decisões pelo governo.

FORMATO DA RESPOSTA (Use Markdown exatamente assim):

### 📢 O que aconteceu? (Em linguagem simples)
[Explicação em 2 a 3 frases curtas do significado prático]

### 📋 O que você precisa fazer agora?
- **Ação:** [Passo a passo claro]
- **Prazo:** [Prazo final, se houver]
- **O que acontece se não fizer:** [Consequência prática]

### 🔍 Trilha de Transparência (Fonte Oficial)
> "[Cole aqui o trecho exato do texto original que justifica esta orientação]"
"""

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Documento original:\n\n{documento_texto}"}
                    ],
                    temperature=0.2
                )

                resultado = response.choices[0].message.content

                st.success("Tradução concluída com sucesso!")
                st.markdown("---")
                st.markdown(resultado)

            except Exception as e:
                st.error(f"Ocorreu um erro ao processar: {e}")