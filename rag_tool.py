from vector_store import load_vector_store


def retrieve_documents(query):

    db = load_vector_store()

    docs = db.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context
