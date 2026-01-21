"""
Basic Ollama Chat Example
Demonstrates simple interaction with a local Ollama model
"""

import ollama

def basic_chat():
    """Simple chat interaction with Ollama"""
    
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'user',
                'content': 'Explain quantum computing in simple terms'
            }
        ],
        options={
            'temperature': 0.8  # More creative and diverse output
        }
    )
    
    print("AI Response:")
    print(response['message']['content'])

if __name__ == "__main__":
    basic_chat()
