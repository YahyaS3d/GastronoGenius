### README

#### Description
This script implements a conversational retrieval system using the LangChain library. It leverages the OpenAI API for conversational responses and performs retrieval-based question answering.

#### Usage
1. **Install Dependencies**: 
   Install the required dependencies by running:
   ```bash
   pip install langchain openai
   ```

2. **Set Up API Key**: 
   Set up your OpenAI API key by replacing `constants.APIKEY` with your actual API key.

3. **Enable Persistence (Optional)**: 
   Optionally, set the `PERSIST` variable to `True` if you want to save the index to disk for reuse.

4. **Run the Script**: 
   Execute the script with an optional query argument:
   ```bash
   python chatgpt.py "what is my favorite food?"
   ```
   If no query argument is provided, the script will prompt for input.

5. **Interactive Queries**: 
   Enter your query when prompted, and the system will respond with an answer. Type 'quit', 'q', or 'exit' to stop the script.

#### Components
- **LangChain**: A library for natural language processing tasks.
- **OpenAI**: Provides the conversational model for generating responses.
- **VectorStoreIndexCreator**: Creates an index for efficient retrieval.
- **ConversationalRetrievalChain**: Combines the conversational model and retrieval index for interactive conversations.
- **DirectoryLoader**: Loads text data from a directory.
- **ChatOpenAI**: Model for conversational chat.
- **Chroma**: Vector store for storing and querying embeddings.

#### Notes
- **API Key Setup**: Ensure proper setup of the OpenAI API key for authentication.
- **Configuration Adjustments**: Adjust the data directory and other configurations as needed.
- **Extendability**: This script can be extended or integrated into larger conversational systems for various applications.

