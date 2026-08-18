from app.core.config import settings
from openai import OpenAI


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.llm_api_key,
            base_url=settings.llm_base_url,
        )

        self.model = settings.llm_model

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:
        system_prompt = """
You are a helpful document question-answering assistant.

Answer the user's question using only the provided context.

Rules:
1. Do not invent information.
2. If the answer cannot be found in the context,
   say that the information is not available.
3. Be concise and factual.
4. Do not use external knowledge.
"""

        user_prompt = f"""
Context:

{context}

Question:

{question}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            temperature=0.0,
        )

        return response.choices[0].message.content or ""
