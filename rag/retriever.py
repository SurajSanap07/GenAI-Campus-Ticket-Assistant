
import faiss
import numpy as np

from rag.pdf_loader import load_pdf
from rag.embeddings import create_chunks, create_embeddings


class PolicyRetriever:

    def __init__(self, pdf_path):

        # Load PDF
        text = load_pdf(pdf_path)

        # Create chunks
        self.chunks = create_chunks(text)

        # Create embeddings
        embeddings = create_embeddings(
            self.chunks
        )

        # Convert to float32
        embeddings = np.array(
            embeddings
        ).astype("float32")

        # Create FAISS index
        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        # Add embeddings
        self.index.add(embeddings)

    def search(self, query, top_k=3):

        # Create query embedding
        query_embedding = create_embeddings(
            [query]
        )

        query_embedding = np.array(
            query_embedding
        ).astype("float32")

        # Search FAISS
        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for index in indices[0]:

            if index < len(self.chunks):

                results.append(
                    self.chunks[index]
                )

        return results
