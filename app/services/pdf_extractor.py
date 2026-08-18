import fitz


class PDFExtractor:
    def extract(self, path: str):
        with fitz.open(path) as pdf:
            pages = []

            for page in pdf:
                pages.append(page.get_text())

            return {
                "text": "\n".join(pages),
                "page_count": len(pdf),
            }
