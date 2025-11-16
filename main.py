from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate # for chat-based prompts

template = """
Your name is ChatGBT, an experimental AI model with a genius disposition

Here is the conversation we've had so far {context}
Question: {question}
Answer: Answer like a genius."""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print ("Welcome to ChatGBT! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        result = chain.invoke({"context": context, "question": user_input})
        
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nChatGBT: {result}"
        
if __name__ == "__main__":
        handle_conversation()
          
        
        



