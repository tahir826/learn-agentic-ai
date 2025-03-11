from langchain_community.chat_models import AzureChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Set up Azure OpenAI model
llm = AzureChatOpenAI(
    openai_api_base="https://tahir826.openai.azure.com/",
    openai_api_version="2023-03-15-preview",
    deployment_name="your-deployment-name",
    openai_api_key="CS8G4Noeia6SwDGW4hq1oNfuL7QPRvdBrVoQDxMKNSvyAQoBqLo1JQQJ99BCACYeBjFXJ3w3AAAAACOGtCyp",
    openai_api_type="azure"
)

# Example conversation
messages = [
    SystemMessage(content="You are an AI assistant."),
    HumanMessage(content="Tell me a joke about AI.")
]

# Generate response
response = llm(messages)
print(response.content)
