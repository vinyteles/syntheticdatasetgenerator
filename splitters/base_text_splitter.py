from langchain_core.documents import Document


class BaseTextSplitter:

    chunk_size: int
    """ Maximum chunk length"""

    chunk_overlap: int
    """ Lenght of one chunk overlapping its neighbor """


    def split(self, text: str, file_name: str) -> list[Document]:
        pass




