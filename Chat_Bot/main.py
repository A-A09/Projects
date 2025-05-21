import json
import streamlit as st

def load_knowledge_base():
    file_path = "C:\\Users\\abdul\\OneDrive\\Desktop\\projects\\chat bot\\knowledge_base.json"
    try:
        with open(file_path, 'r') as file:
            knowledge_base = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, create an empty knowledge base
        knowledge_base = {"questions": {}}
    return knowledge_base

def save_knowledge_base(knowledge_base):
    with open('knowledge_base.json', 'w') as file:
        json.dump(knowledge_base, file, indent=2)

def chat_bot(question, knowledge_base):
    question = question.lower()
    if question in knowledge_base['questions']:
        return knowledge_base['questions'][question]
    else:
        answer = st.text_input(f"I don't know the answer to '{question}'. Can you please teach me?")
        knowledge_base['questions'][question] = answer
        save_knowledge_base(knowledge_base)
        return f"Thank you! I have learned that '{question}' is '{answer}'."

def main():
    st.title("ChatBot")

    # Load or create knowledge base
    knowledge_base = load_knowledge_base()

    # User input
    user_input = st.text_input("You:")

    # ChatBot response
    if user_input:
        response = chat_bot(user_input, knowledge_base)
        st.text("ChatBot: " + response)

if __name__ == "__main__":
    main()
