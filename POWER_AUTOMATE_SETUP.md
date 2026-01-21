# Power Automate Setup Guide

Complete guide for integrating Ollama with Microsoft Power Automate flows.

## Prerequisites

- Microsoft 365 account with Power Automate access
- Ollama installed and running locally
- Python with `ollama` and `requests` packages installed

## Part 1: Create the Power Automate Flow

### Step 1: Create a New Flow

1. Go to [Power Automate](https://make.powerautomate.com/)
2. Click **+ Create** → **Instant cloud flow**
3. Name your flow: "Ollama AI Response Handler"
4. Choose trigger: **When an HTTP request is received**
5. Click **Create**

### Step 2: Configure HTTP Trigger

1. The trigger will generate a URL after you save the flow
2. Click **Use sample payload to generate schema**
3. Paste this JSON schema:

```json
{
    "response": "Sample AI response text here",
    "timestamp": "2025-07-30T12:00:00Z",
    "model": "mistral",
    "original_prompt": "What is AI?",
    "response_length": 150
}
```

4. Click **Done**

### Step 3: Add Actions

#### Option A: Send Email with AI Response

1. Click **+ New step**
2. Search for "Send an email (V2)"
3. Configure:
   - **To**: Your email address
   - **Subject**: `AI Response from Ollama`
   - **Body**: Use dynamic content `response` from the HTTP trigger

#### Option B: Save to SharePoint

1. Click **+ New step**
2. Search for "Create item" (SharePoint)
3. Configure:
   - **Site Address**: Your SharePoint site
   - **List Name**: Your list name
   - **Title**: Use `original_prompt`
   - **AI Response** (custom column): Use `response`

#### Option C: Post to Teams

1. Click **+ New step**
2. Search for "Post message in a chat or channel"
3. Configure:
   - **Post as**: Flow bot
   - **Post in**: Channel
   - **Team**: Your team
   - **Channel**: Your channel
   - **Message**: Format using `response` and `timestamp`

### Step 4: Save and Get URL

1. Click **Save** at the top
2. Expand the HTTP trigger
3. Copy the **HTTP POST URL** — you'll need this for Python!

---

## Part 2: Python Integration

### Basic Integration Example

```python
import ollama
import requests

# Your Power Automate trigger URL
FLOW_URL = "https://prod-##.westus.logic.azure.com:443/workflows/.../triggers/manual/paths/invoke?..."

# Get AI response
response = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Explain AI in simple terms'}],
    options={'temperature': 0.8}
)

# Send to Power Automate
payload = {'response': response['message']['content']}
r = requests.post(FLOW_URL, json=payload, headers={'Content-Type': 'application/json'})

print(f"Status: {r.status_code}")
```

### Advanced Integration

See [flow_trigger_complete.py](../examples/flow_trigger_complete.py) for a complete implementation with:
- Error handling
- Input validation
- Metadata tracking
- Timeout handling

---

## Part 3: Use Cases

### 1. Automated Email Responses

**Scenario**: Generate AI-powered email replies

**Flow**:
1. Python gets email content
2. Ollama generates response
3. Power Automate sends email via Outlook

### 2. Content Summarization

**Scenario**: Summarize documents and save to SharePoint

**Flow**:
1. Python reads document
2. Ollama creates summary
3. Power Automate saves to SharePoint library

### 3. Teams Notifications

**Scenario**: AI-powered alerts in Teams channels

**Flow**:
1. Python monitors events
2. Ollama generates insights
3. Power Automate posts to Teams

### 4. Approval Workflows

**Scenario**: AI-assisted decision support

**Flow**:
1. Python analyzes request
2. Ollama provides recommendation
3. Power Automate creates approval

---

## Part 4: Testing Your Integration

### Test from Python

```python
import requests

FLOW_URL = "YOUR_URL_HERE"

# Test payload
test_data = {
    "response": "This is a test from Ollama integration",
    "timestamp": "2025-07-30T10:00:00Z",
    "model": "mistral"
}

r = requests.post(FLOW_URL, json=test_data)
print(f"Test result: {r.status_code}")
```

### Test from Power Automate

1. In your flow, click **Test** (top right)
2. Choose **Manually**
3. Click **Test**
4. Run your Python script
5. Check if flow executes successfully

---

## Part 5: Troubleshooting

### Common Issues

**❌ 404 Not Found**
- Flow URL is incorrect or flow was deleted
- Verify the URL in Power Automate

**❌ 401 Unauthorized**
- Some flows require authentication
- Add authentication to your Python request

**❌ Timeout Errors**
- Increase timeout in Python: `requests.post(..., timeout=60)`
- Check if Ollama response is taking too long

**❌ Schema Validation Errors**
- Ensure your payload matches the schema
- Check for required fields

### Debugging Tips

1. **Check Flow Run History**
   - Go to your flow in Power Automate
   - Click "Run history"
   - View detailed execution logs

2. **Add Response Action**
   - Add "Response" action in Power Automate
   - Return data to Python for debugging

3. **Enable Logging**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

---

## Part 6: Security Best Practices

### Protect Your Flow URL

❌ **Don't**:
- Commit URLs to public repositories
- Share URLs in documentation
- Hardcode URLs in shared scripts

✅ **Do**:
- Use environment variables
- Store in `.env` files (add to `.gitignore`)
- Use Azure Key Vault for production

### Example with Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()

FLOW_URL = os.getenv('POWER_AUTOMATE_FLOW_URL')
```

Create `.env` file:
```
POWER_AUTOMATE_FLOW_URL=https://prod-##.westus.logic.azure.com:443/...
```

---

## Part 7: Advanced Features

### Conditional Logic in Flow

Add conditions based on AI response:

1. Add **Condition** action
2. Check if `response` contains specific keywords
3. Branch to different actions based on result

### Multiple Models

Support different Ollama models:

```python
payload = {
    'response': ai_response,
    'model': 'mistral',  # or 'llama2', 'gemma', etc.
    'confidence': 0.95
}
```

In Power Automate, route based on model type.

### Error Handling in Flow

1. Add **Scope** action to group steps
2. Add **Parallel branch** with error handling
3. Send error notifications if something fails

---

## Resources

- [Power Automate Documentation](https://learn.microsoft.com/en-us/power-automate/)
- [Ollama Python Library](https://github.com/ollama/ollama-python)
- [Example Scripts](../examples/)

---

**Ready to automate? Start building your AI-powered workflows today! 🚀**
