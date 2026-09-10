
from sentence_transformers import SentenceTransformer


# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_chunks(text, chunk_size=500, overlap=50):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks


def create_embeddings(chunks):

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings
