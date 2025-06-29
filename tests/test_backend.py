from backend.summarizer import summarize
from backend.challenge import evaluate_answer

def test_summary_length():
    text = "AI is transforming the world." * 30
    summary = summarize(text)
    assert isinstance(summary, str)
    assert len(summary.split()) <= 150

def test_evaluate_answer():
    assert evaluate_answer("Yes", "yes") == " Correct!"
    assert "Incorrect" in evaluate_answer("No", "Yes")
