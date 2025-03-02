# 1. Download Ollama from https://ollama.com/
# 2. Install Ollama: pip install ollama
# 3. Run Ollama:
#    ollama pull llama3.1 && ollama run llama3.1:8b
# 4. Start Chatbot:

import ollama

while True:
    user = input('You: ')
    if user.lower() == 'bye':
        print('Goodbye!')
        break
    
    response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': user}])

    print('Chatbot:', response['message']['content'])
