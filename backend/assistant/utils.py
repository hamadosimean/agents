# ===============================
# Prompts
# ===============================
def build_prompt(question: str, KNOWLEDGE_BASE: str) -> str:
    return f"""
You are an AI assistant designed to answer user questions using ONLY the provided knowledge base.

RULES:
1. Read the USER QUESTION carefully.
2. Search for the exact answer inside the KNOWLEDGE BASE.
3. If the answer exists in the KNOWLEDGE BASE:
   - Respond clearly, helpfully, and directly.
   - Do NOT mention the knowledge base.
4. If the answer does NOT exist in the KNOWLEDGE BASE:
   - Respond with ONLY this exact word:
     web_search
   - Do NOT add punctuation, explanation, or extra text.

USER QUESTION:
{question}

KNOWLEDGE BASE:
{KNOWLEDGE_BASE}
"""


def build_web_prompt(question: str, content: str) -> str:
    return f"""
You are an AI assistant.

TASK:
- Clean, summarize, and synthesize the CONTENT.
- Answer the USER QUESTION clearly and helpfully.
- Do NOT mention scraping, tools, or sources.
- Provide a final, user-ready answer.

CONTENT:
{content}

USER QUESTION:
{question}
"""
