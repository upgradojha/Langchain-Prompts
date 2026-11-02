from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-6-luna')

chat_history = []
print(chat_history)
while True:
    user_input = input('Enter your Input: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    else:
        result = model.invoke(chat_history)
        print('============================================================')
        print()
        print("USER: ", user_input)
        print("AI: ", result.content)
        chat_history.append(result.content)
        print('============================================================')
        print()
