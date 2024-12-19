from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

# information available here:
documents = SimpleDirectoryReader("information").load_data()

# print(documents)
print(type(documents))
for doc in documents:
    print(type(doc))
    print("\n\n")

# from sentence_transformers import SentenceTransformer

# # Initialize the model
# embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# # Example sentences
# sentences = ["This is an example sentence.", "Sentence transformers are useful for NLP tasks."]

# # Generate embeddings
# embeddings = embedding_model.encode(sentences)

# # Print the embeddings
# print(embeddings)