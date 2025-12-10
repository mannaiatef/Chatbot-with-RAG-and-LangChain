from langchain_community.llms import Ollama
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import gradio as gr

# ======================
# CONFIG
# ======================
CHROMA_PATH = "chroma_db"

# ======================
# EMBEDDINGS (FREE)
# ======================
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ======================
# LLM LOCAL (OLLAMA)
# ======================
llm = Ollama(
    model="mistral",
    temperature=0.5
)

# ======================
# VECTOR STORE
# ======================
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})

# ======================
# CHAT FUNCTION
# ======================
def stream_response(message, history):
    docs = retriever.invoke(message)
    knowledge = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an assistant that answers questions ONLY using the knowledge below.
Do not use your own knowledge.
Do not mention the knowledge source.

Question:
{message}

Knowledge:
{knowledge}
"""

    partial = ""
    for chunk in llm.stream(prompt):
        partial += chunk
        yield partial

# ======================
# GRADIO UI
# ======================
chatbot = gr.ChatInterface(
    stream_response,
    textbox=gr.Textbox(
        placeholder="Ask a question about your PDFs...",
        scale=7
    ),
)

chatbot.launch()
