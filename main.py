#from syntheticDatasetGenerator import SyntheticDatasetGenerator
from splitters.lang_chain_recursive_splitter import LangChainRecursiveSplitter
from langchain_core.documents import Document
import regex as re
from utils import choose_random_chunks


def load_data(file_path) -> str:
    with open( "input/10462_22.txt" , "r" ) as f:
        text = f.read()

    file_name = re.search(r"[^/]+(?=\.\w+$)", file_path).group()

    return text, file_name


def main():
    # Load txt file from input folder
    text, file_name = load_data( "input/10462_22.txt" )

    # Split data into chunks (metadata, page_content)
    splitter = LangChainRecursiveSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split(text, file_name)

    # Choose k aleatory chunks
    chunks = choose_random_chunks(chunks=chunks, k=2)

    # Build prompt


    # Generate k tuples


    return None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
