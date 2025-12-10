from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4

DATA_PATH = "data"
CHROMA_PATH = "chroma_db"

# Embeddings LOCAL & FREE ✅
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector store
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)

# Load PDFs
loader = PyPDFDirectoryLoader(DATA_PATH)
documents = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=100,
)

chunks = splitter.split_documents(documents)
ids = [str(uuid4()) for _ in chunks]

# Add to Chroma
vector_store.add_documents(chunks, ids=ids)

print("✅ PDFs indexed successfully")
