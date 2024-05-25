import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants

# Set the OpenAI API key from the constants file
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

query = None
if len(sys.argv) > 1:
    query = sys.argv[1]  # Get query from command line arguments if provided

# Check if persistence is enabled and if the persisted index exists
if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    # Load documents from the specified directory
    loader = DirectoryLoader("data/")
    if PERSIST:
        # Create and persist the index for future reuse
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
    else:
        # Create the index without persistence
        index = VectorstoreIndexCreator().from_loaders([loader])

# Create a Conversational Retrieval Chain with the specified LLM and retriever
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 5}),  # Increase 'k' to get more results
)

chat_history = []
while True:
    if not query:
        query = input("Prompt: ")  # Prompt user for input if no query is provided
    if query in ['quit', 'q', 'exit']:
        sys.exit()  # Exit the program if user inputs 'quit', 'q', or 'exit'
    result = chain({"question": query, "chat_history": chat_history})
    print(result['answer'])  # Print the result

    # Add the current query and result to the chat history
    chat_history.append((query, result['answer']))
    query = None  # Reset query to None for the next iteration
