from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd


#Load dataset
filename = "Mammography_Dataset.xlsx"
MainSheet = pd.read_excel(filename, sheet_name='main', skiprows=0)
TaskDescriptionSheet = pd.read_excel(filename, sheet_name='TaskDescription', skiprows=0)
StatusDescriptionSheet = pd.read_excel(filename, sheet_name='StatusDescription', skiprows=0)
DatatypeDescriptionSheet = pd.read_excel(filename, sheet_name='DatatypeDescription', skiprows=0)
FiletypeDescriptionSheet = pd.read_excel(filename, sheet_name='FiletypeDescription', skiprows=0)
LocationDescriptionSheet = pd.read_excel(filename, sheet_name='LocationDescription', skiprows=0)



# Global conversation context
combined_context=""

combined_context = "\n".join(
    MainSheet.apply(lambda row: " | ".join(map(str, row.values)), axis=1)
) + "\n"
combined_context += "\n".join(
    TaskDescriptionSheet.apply(lambda row: " | ".join(map(str, row.values)), axis=1)
) + "\n"
combined_context += "\n".join(
    StatusDescriptionSheet.apply(lambda row: " | ".join(map(str, row.values)), axis=1)
) + "\n"
combined_context += "\n".join(
    DatatypeDescriptionSheet.apply(lambda row: " | ".join(map(str, row.values)), axis=1)
) + "\n"
combined_context += "\n".join(
    FiletypeDescriptionSheet.apply(lambda row: " | ".join(map(str, row.values)), axis=1)
) + "\n"
combined_context += "\n".join(
   LocationDescriptionSheet.apply(lambda row: " | ".join(map(str, row.values)), axis=1)
) + "\n"

# Chatbot setup
template = """
You are an expert in Mammogram datasets. 

Here is the conversation history: {combined_context}

Please provide a concise answer to the following question, using no more than 70 words:

Question: {question}

Answer:
"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# This is a POST route for chat, which you already have
@app.route('/chat', methods=['POST'])
def chat():
    global combined_context
    data = request.get_json()  # Get the JSON data sent from the frontend
    user_message = data.get('prompt')  # Extract the 'prompt' sent from the frontend
    
    if user_message:
        result = chain.invoke({"combined_context": combined_context, "question": user_message})
        combined_context += f"\nUser: {user_message}\nAI: {result}"  # Update context
        return jsonify({"response": result})
    else:
        return jsonify({"response": "Error: No message received"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
