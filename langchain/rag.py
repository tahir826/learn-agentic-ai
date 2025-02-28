from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferWindowMemory
import os
from dotenv import load_dotenv
load_dotenv()


llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

memory = ConversationBufferWindowMemory(k=5)

loader = TextLoader("./data/data.txt", encoding="utf-8")

# try:
#     loader = TextLoader("./data/data.txt")
# except Exception as e:
#     print("Error while loading file=", e)

if loader is None:
    raise ValueError("Failed to load the file.")

text_splitter1 = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
# Create embeddings
embedding1 = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


# Create the index with the specified embedding model and text splitter
index_creator = VectorstoreIndexCreator(
    embedding=embedding1,
    text_splitter=text_splitter1
)
store = index_creator.from_loaders([loader])

# Query the index with the LLM
while True:
    human_message = input("How can I help you today? ")
    if input == "exit":
        break
    response = store.query(human_message, llm=llm, memory=memory)
    print(response)
