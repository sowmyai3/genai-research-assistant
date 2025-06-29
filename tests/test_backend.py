from backend.summarizer import summarize
from backend.challenge import evaluate_answer

def test_summary_length():
    txt = "AI is the field of study that gives computers the ability to learn." * 30
    assert len(summarize(txt).split()) <= 150

def test_eval_exact():
    assert evaluate_answer("Machine Learning", "machine learning") == " Correct!"
