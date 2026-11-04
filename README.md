<img width="1366" height="768" alt="Captura de tela 2026-11-04 162311" src="https://github.com/user-attachments/assets/700b5cad-583e-47b5-bc1f-024f166d7426" />
<img width="1366" height="768" alt="Captura de tela 2026-11-04 161931" src="https://github.com/user-attachments/assets/3650f2d0-9c77-4749-913c-b74d283c0ac8" />
<img width="1366" height="768" alt="Captura de tela 2026-11-04 161937" src="https://github.com/user-attachments/assets/97f0178e-4c7d-46e9-bd0f-b3204bb5a327" />
# 🏛️ CidadãoClaro IA — Transparência Ativa e Linguagem Simples no Setor Público

> **Projeto desenvolvido para o Processo Seletivo Futures Trainee Softplan**  
> **Foco:** GovTech, Inteligência Artificial Responsável e Experiência do Cidadão.

---
https://cidadao-claro-ia.onrender.com/

## 📌 1. O Problema Real

No Brasil, mais de 90% dos cidadãos enfrentam dificuldades para compreender o andamento de processos judiciais, editais ou despachos administrativos devido ao uso intensivo de linguagem técnica ("juridiquês" e burocratês). 

- **Gargalo Atual:** O cidadão não entende o status da sua solicitação e recorre ao atendimento presencial ou telefônico, gerando sobrecarga nos órgãos públicos.
- **Limitação dos Métodos Tradicionais:** Glossários estáticos e manuais em PDF não resolvem a dúvida em tempo real nem personalizam a explicação para o contexto específico da pessoa.

---

## 💡 2. A Solução com Inteligência Artificial

O **CidadãoClaro IA** é uma solução assistiva que recebe documentos públicos complexos e gera instantaneamente:

1. **Tradução em Linguagem Simples:** Explicação do documento em linguagem de nível fundamental (6º ano).
2. **Guia Prático de Ação (Próximos Passos):** O que o cidadão precisa fazer, prazos e documentos necessários.
3. **Trilha de Evidência & Transparência:** Indicação direta do parágrafo/trecho original do documento que embasa a resposta (evitando desinformação).

### 🛡️ Governança, Ética e IA Responsável
- **Human-in-the-Loop:** A IA atua estritamente na **simplificação e comunicação**, sem tomar decisões administrativas ou judiciais pelo servidor público.
- **Mitigação de Alucinações (RAG):** O modelo é restrito ao contexto do documento fornecido, impedindo que a IA gere fatos inexistentes.

---

## 🏗️ 3. Arquitetura Técnica e Método

[ Documento Público (PDF/Texto) ]
│
▼
[ Processamento & Extração ]
│
▼
[ Pipeline RAG + LLM (Prompt de Linguagem Simples) ]
│
▼
[ Interface Cidadão: Resumo + Guia + Fonte Oficial ]


- **Tecnologias Pretendidas:** Python, Streamlit, LLM (OpenAI API / Claude API), RAG (Retrieval-Augmented Generation).
- **Abordagem de Prompting:** Engenharia de Prompt focada em *Visual Law*, tom empático e regras rígidas de formatação.

---

## 📹 4. Demonstração em Vídeo
*(Espaço reservado para o vídeo de 1 a 2 minutos demonstrando o protótipo em funcionamento)*

---

## 🚀 5. Visão de Escala no Ecossistema Softplan

Esta solução possui aderência direta ao core de **GovTech e Justiça** da Softplan, podendo ser integrada nativamente aos sistemas de gestão pública para:
- Enviar notificações automáticas simplificadas via WhatsApp para a população.
- Reduzir em até 40% o volume de atendimentos de triagem em balcões de órgãos públicos.
- Promover acessibilidade por voz para cidadãos analfabetos funcionais ou com deficiência visual.
