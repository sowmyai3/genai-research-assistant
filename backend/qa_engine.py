from transformers import pipeline

_qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(context: str, question: str) -> tuple[str, float]:
    res = _qa(question=question, context=context)
    return res["answer"], res["score"]
