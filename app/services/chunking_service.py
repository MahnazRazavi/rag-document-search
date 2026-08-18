from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkingService:
    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""],
        )

    def chunk_text(self, text: str) -> list[dict]:
        chunks = self.splitter.split_text(text)
        return [
            {"text": chunk, "token_count": max(1, len(chunk) // 4)} for chunk in chunks
        ]
