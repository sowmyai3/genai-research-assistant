import streamlit as st, textwrap
from backend.doc_parser import parse
from backend.summarizer import summarize
from backend.retriever import chunk, build_index, fetch
from backend.qa_engine import answer_question
from backend.challenge import generate_questions, evaluate_answer

st.set_page_config(page_title="Assistant")
st.title(" GenAI Research Assistant")

uploaded = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])

if uploaded:
    # --- Parse & summarise ----------------------------------------------------
    if "doc" not in st.session_state:
        raw = parse(uploaded)
        st.session_state.doc = raw
        st.session_state.summary = summarize(raw)
        st.session_state.vdb = build_index(chunk(raw))
    st.subheader(" Summary (≤150 words)")
    st.write(st.session_state.summary)

    # --- Modes ---------------------------------------------------------------
    mode = st.radio("Choose interaction mode", ["Ask Anything", "Challenge Me"])

    # ---------- ASK ANYTHING --------------------------------------------------
    if mode == "Ask Anything":
        q = st.text_input(" Your question about the document")
        if q:
            ctx = fetch(st.session_state.vdb, q)
            ans, score = answer_question(ctx, q)
            st.success(ans)
            st.caption(f"Confidence: {score:.2f}\n\nContext:\n{ctx[:300]}…")

    # ---------- CHALLENGE ME --------------------------------------------------
    else:
        if "qs" not in st.session_state:
            st.session_state.qs = generate_questions(st.session_state.doc)
        st.write(" Answer the questions below:")
        for i, q in enumerate(st.session_state.qs, 1):
            user = st.text_input(f"{i}. {q}", key=f"q{i}")
            if user:
                ctx = fetch(st.session_state.vdb, q)
                gold, _ = answer_question(ctx, q)
                st.write(evaluate_answer(user, gold))
                with st.expander("Justification snippet"):
                    st.write(textwrap.shorten(ctx, 400, placeholder=" …"))
