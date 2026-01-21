"""
Multi-Turn Conversation Example
Demonstrates maintaining context across multiple messages
"""

import ollama

def multi_turn_chat():
    """Maintain conversation context across multiple messages"""
    
    messages = [
        {
            'role': 'user',
            'content': 'What is machine learning?'
        }
    ]
    
    # First response
    response = ollama.chat(model='mistral', messages=messages)
    print("AI:", response['message']['content'])
    
    # Add AI response to conversation history
    messages.append(response['message'])
    
    # Follow-up question
    messages.append({
        'role': 'user',
        'content': 'Can you give me a practical example?'
    })
    
    # Second response with context
    response = ollama.chat(model='mistral', messages=messages)
    print("\nAI:", response['message']['content'])

if __name__ == "__main__":
    multi_turn_chat()
