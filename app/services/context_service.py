class ContextService:
    def build_context(self, results) -> str:
        contexts = []

        for index, result in enumerate(results):
            payload = result.payload or {}

            text = payload.get("text", "")

            contexts.append(
                f"""
[Source {index + 1}]

{text}
"""
            )

        return "\n".join(contexts)
