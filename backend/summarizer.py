from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

_MODEL = "facebook/bart-large-cnn"          # reproducible
_summarize = pipeline(
    "summarization",
    model=AutoModelForSeq2SeqLM.from_pretrained(_MODEL),
    tokenizer=AutoTokenizer.from_pretrained(_MODEL),
)

def summarize(text: str, max_tokens: int = 150) -> str:
    """≤150-word summary."""
    return _summarize(
        text,
        max_length=max_tokens,
        min_length=50,
        do_sample=False,
        truncation=True,
    )[0]["summary_text"].strip()
