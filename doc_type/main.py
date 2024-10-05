from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import regex as re
import pandas as pd
import prompt.prompt_template as prompt_template
import os



def load_data(file_path: str) -> (str, str):
    with open(file_path, "r" ) as f:
        text = f.read()

    file_name = re.search(r"[^/]+(?=\.\w+$)", file_path).group()

    return text, file_name


def post_processing(answer: str) -> str:
    type_pattern = r"base|altera|revoga"

    doc_type = re.search(type_pattern, answer)
    if doc_type:
        doc_type = doc_type.group()

    return str(doc_type)

def main(dir_path):
    csv_file = {"source": [], "type": [], "raw_answer": []}

    directory = os.fsencode (dir_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        text, file_name = load_data(directory.decode()+"/"+filename)

        template = prompt_template.generate_type_template

        prompt = ChatPromptTemplate.from_template (template.format(text=text))

        model = OllamaLLM ( model = "llama3:latest" )

        chain = prompt | model
        answer = chain.invoke({})
        doc_type = post_processing(answer)

        csv_file["source"].append(file_name)
        csv_file["type"].append(doc_type)
        csv_file["raw_answer"].append(answer)

    df = pd.DataFrame(csv_file)
    df.to_csv("/home/vinicius/PycharmProjects/syntheticdatasetgenerator/output/annotated.csv")

    return None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(dir_path= "/home/vinicius/PycharmProjects/syntheticdatasetgenerator/input")
