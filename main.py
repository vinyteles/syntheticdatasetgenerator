from itertools import count
from tempfile import template

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import regex as re
import pandas as pd
import prompt.prompt_template as prompt_template
import os
import csv


def load_data(file_path: str) -> (str, str):
    with open(file_path, "r") as f:
        text = f.read()

    file_name = re.search(r"[^/]+(?=\.\w+$)", file_path).group()

    return text, file_name


def generate_questions(text: str) -> str:
    template = prompt_template.global_question_template

    prompt = ChatPromptTemplate.from_template(template.format(text=text))

    model = OllamaLLM(model="llama3:latest")

    chain = prompt | model
    question = chain.invoke({})

    return question


def generate_answers(question: str, text: str):
    template = prompt_template.answer_template

    prompt = ChatPromptTemplate.from_template(template.format(document=text, question=question))

    model = OllamaLLM(model="llama3:latest")

    chain = prompt | model
    answer = chain.invoke({})

    return answer


def generate_summary(text: str) -> str:
    template = prompt_template.summary_template

    prompt = ChatPromptTemplate.from_template(template.format(text=text))

    model = OllamaLLM(model="llama3:latest")

    chain = prompt | model
    answer = chain.invoke({})

    return answer


def main(dir_path):
    csv_file = {"doc_id": [], "question_type": [], "question": [], "answer": [], "summary": []}
    count = 0
    with open(dir_path, mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            print(lines)
            text, file_name = load_data(
                "/home/vinicius/PycharmProjects/syntheticdatasetgenerator/input" + "/" + lines["source"] + ".txt"
                )
            count += 1

            ## falta ver como voce vai fazer pra usar os tipos pra gerar as perguntas, e como separar global de local
            summary = generate_summary(text=text)
            question = generate_questions(text=text)
            answer = generate_answers(question=question, text=text)

            csv_file["doc_id"].append(lines["source"])
            csv_file["question_type"].append(lines["type"])
            csv_file["question"].append(question)
            csv_file["answer"].append(answer)
            csv_file["summary"].append(summary)

        df = pd.DataFrame(csv_file)
        df.to_csv("/home/vinicius/PycharmProjects/syntheticdatasetgenerator/output/dataset_2024_v2.csv")

    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(dir_path="/home/vinicius/PycharmProjects/syntheticdatasetgenerator/output/annotated.csv")
