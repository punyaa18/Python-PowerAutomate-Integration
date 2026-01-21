"""
Power Automate Integration Example
Demonstrates how to create an API endpoint for Power Automate flows
"""

import ollama
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ai-chat', methods=['POST'])
def ai_chat():
    """
    API endpoint for Power Automate integration
    
    Expected JSON body:
    {
        "message": "Your question here",
        "model": "mistral",
        "temperature": 0.8
    }
    """
    try:
        data = request.get_json()
        
        user_message = data.get('message', '')
        model = data.get('model', 'mistral')
        temperature = data.get('temperature', 0.8)
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': user_message
                }
            ],
            options={
                'temperature': temperature
            }
        )
        
        return jsonify({
            'success': True,
            'response': response['message']['content'],
            'model': model
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/summarize', methods=['POST'])
def summarize():
    """
    Endpoint for text summarization
    Useful for Power Automate workflows that need content summaries
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        response = ollama.chat(
            model='mistral',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a helpful assistant that creates concise summaries.'
                },
                {
                    'role': 'user',
                    'content': f'Please summarize the following text:\n\n{text}'
                }
            ],
            options={
                'temperature': 0.3  # Lower temperature for more focused output
            }
        )
        
        return jsonify({
            'success': True,
            'summary': response['message']['content']
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == "__main__":
    print("Starting Ollama API server for Power Automate...")
    print("Available endpoints:")
    print("  - POST /ai-chat - General AI chat")
    print("  - POST /summarize - Text summarization")
    print("\nServer running on http://localhost:5000")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
