
from rag.retriever import PolicyRetriever


retriever = PolicyRetriever(
    "documents/Campus_Policies.pdf"
)


def get_relevant_policy(question, top_k=3):

    results = retriever.search(
        question,
        top_k=top_k
    )

    return results
