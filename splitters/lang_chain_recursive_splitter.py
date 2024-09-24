from langchain_core.documents import Document
from splitters.base_text_splitter import BaseTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


class LangChainRecursiveSplitter(BaseTextSplitter):


    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def split(self, text: str, file_name: str) -> list[Document]:
        chunks = self.model.create_documents (texts= [text], metadatas = [{"file_name": file_name}])

        return chunks



