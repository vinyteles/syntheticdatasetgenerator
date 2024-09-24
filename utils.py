import random
from langchain_core.documents import Document


def choose_random_chunks(chunks, k) -> list[Document]:
    number_chunks = len(chunks) - 1

    index_selected = random.choices(range(number_chunks), k=k)

    selected_chunks = [chunks[i] for i in index_selected]

    return selected_chunks