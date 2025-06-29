import textwrap
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def chunk(text: str, size: int = 2000) -> list[str]:
    """Rough 2 000-character chunks."""
    return textwrap.wrap(text, size)

def build_index(chunks: list[str]) -> FAISS:
    return FAISS.from_texts(chunks, _embeddings)

def fetch(vdb: FAISS, query: str, k: int = 4) -> str:
    docs = vdb.similarity_search_with_relevance_scores(query, k)
    return "\n".join([doc.page_content for doc, _ in docs])
