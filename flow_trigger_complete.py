"""
Power Automate Flow Trigger Example
Complete implementation showing Ollama → Power Automate integration
"""

import ollama
import requests
import json
from datetime import datetime

def get_ollama_response(prompt, model='mistral', temperature=0.8):
    """
    Get a response from Ollama model
    
    Args:
        prompt (str): The user's question or prompt
        model (str): Ollama model to use (default: mistral)
        temperature (float): Creativity level 0.0-1.0 (default: 0.8)
    
    Returns:
        str: The model's response text
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'user', 'content': prompt}
            ],
            options={'temperature': temperature}
        )
        
        return response['message']['content']
    
    except Exception as e:
        print(f"Error getting Ollama response: {e}")
        return None

def trigger_power_automate(flow_url, response_text, additional_data=None):
    """
    Send data to Power Automate flow via HTTP trigger
    
    Args:
        flow_url (str): Your Power Automate HTTP trigger URL
        response_text (str): The AI response to send
        additional_data (dict): Optional extra data to include
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Prepare payload
        payload = {
            'response': response_text,
            'timestamp': datetime.now().isoformat(),
            'model': 'mistral'
        }
        
        # Add any additional data
        if additional_data:
            payload.update(additional_data)
        
        # Set headers
        headers = {
            'Content-Type': 'application/json'
        }
        
        # Send POST request
        r = requests.post(flow_url, json=payload, headers=headers, timeout=30)
        
        # Check response
        if r.status_code == 200 or r.status_code == 202:
            print(f"✓ Power Automate triggered successfully! Status: {r.status_code}")
            return True
        else:
            print(f"✗ Power Automate trigger failed. Status: {r.status_code}")
            print(f"Response: {r.text}")
            return False
    
    except requests.exceptions.Timeout:
        print("✗ Request timed out. Check your flow URL and network connection.")
        return False
    
    except Exception as e:
        print(f"✗ Error triggering Power Automate: {e}")
        return False

def main():
    """Main execution flow"""
    
    # Configuration
    FLOW_URL = 'YOUR_POWER_AUTOMATE_HTTP_TRIGGER_URL_HERE'
    
    # Check if URL is configured
    if 'YOUR_POWER_AUTOMATE' in FLOW_URL:
        print("⚠ Please configure your Power Automate flow URL first!")
        print("Update the FLOW_URL variable in this script.")
        return
    
    # Step 1: Get user input
    print("=== Ollama + Power Automate Integration ===\n")
    user_prompt = input("Enter your question for AI: ")
    
    if not user_prompt.strip():
        print("No prompt provided. Exiting.")
        return
    
    # Step 2: Get Ollama response
    print("\n🤖 Querying Ollama...")
    ai_response = get_ollama_response(user_prompt)
    
    if not ai_response:
        print("Failed to get response from Ollama.")
        return
    
    print(f"\n✓ AI Response received:")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(ai_response)
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    
    # Step 3: Send to Power Automate
    print("📤 Sending to Power Automate...")
    
    additional_data = {
        'original_prompt': user_prompt,
        'response_length': len(ai_response)
    }
    
    success = trigger_power_automate(FLOW_URL, ai_response, additional_data)
    
    if success:
        print("\n✓ Complete! Check your Power Automate flow for results.")
    else:
        print("\n✗ Integration failed. Please check your configuration.")

if __name__ == "__main__":
    main()
