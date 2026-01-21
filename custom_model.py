"""
Custom Model Example
Demonstrates how to create and use custom models with specific behaviors
"""

import ollama
import os

def create_custom_model():
    """
    Create a custom model using a Modelfile
    This example creates a specialized coding assistant
    """
    
    modelfile = """
FROM mistral

# Set the system message
SYSTEM You are an expert Python programmer. Provide clear, concise code examples with explanations.

# Set parameters
PARAMETER temperature 0.7
PARAMETER top_p 0.9
"""
    
    # Save modelfile temporarily
    with open('temp_modelfile', 'w') as f:
        f.write(modelfile)
    
    # Create the custom model
    print("Creating custom model 'python_assistant'...")
    os.system('ollama create python_assistant -f temp_modelfile')
    
    # Clean up
    os.remove('temp_modelfile')
    
    print("Custom model created successfully!")

def use_custom_model():
    """Use the custom model for code assistance"""
    
    response = ollama.chat(
        model='python_assistant',
        messages=[
            {
                'role': 'user',
                'content': 'Write a Python function to calculate fibonacci numbers'
            }
        ]
    )
    
    print("Python Assistant Response:")
    print(response['message']['content'])

if __name__ == "__main__":
    # Uncomment to create the model first
    # create_custom_model()
    
    # Use the custom model
    use_custom_model()