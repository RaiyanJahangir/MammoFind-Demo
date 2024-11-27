from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template="""
Here is the conversation history: {context}

Question: {question}

Answer:
"""


model = OllamaLLM(model="mistral")
prompt=ChatPromptTemplate.from_template(template)
chain=prompt|model


def handle_conversation():
    context=""
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input=input("You: ")
        if user_input.lower()=="exit":
            break
        result=chain.invoke({"context":context,"question":user_input})
        print("Bot: ",result)
        context+=f"\nUser: {user_input}\nAI: {result}"


if __name__=="__main__":
    handle_conversation()

    

from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize Flask app
app = Flask(__name__)

# Chatbot setup
template = """
Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Global conversation context
conversation_context = ""

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_context
    data = request.json
    user_message = data.get('prompt', '')  # Get user input from POST request
    
    if not user_message:
        return jsonify({"response": "No message provided!"}), 400

    # Invoke the chatbot
    try:
        result = chain.invoke({"context": conversation_context, "question": user_message})
        conversation_context += f"\nUser: {user_message}\nAI: {result}"  # Update context
        return jsonify({"response": result}), 200
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
