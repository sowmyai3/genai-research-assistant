from transformers import pipeline
_gen = pipeline("text-generation", model="gpt2")

def generate_questions(doc_text: str, n: int = 3) -> list[str]:
    prompt = (f"Read the following text and craft {n} logic-based comprehension "
              f"questions that require inference:\n\n{doc_text[:1500]}\n\nQ:")
    raw = _gen(prompt, max_new_tokens=256, num_return_sequences=1)[0]["generated_text"]
    qs = [line.strip() for line in raw.split("\n") if line.strip().endswith("?")]
    return qs[:n]

def evaluate_answer(user_ans: str, gold_ans: str) -> str:
    return " Correct!" if user_ans.strip().lower() == gold_ans.strip().lower() \
           else f" Incorrect. Correct answer: {gold_ans}"
