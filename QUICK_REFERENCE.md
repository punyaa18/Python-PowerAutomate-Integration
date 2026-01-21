# Quick Reference Card

## Ollama Commands

### Installation & Setup
```bash
# Check version
ollama --version

# View help
ollama --help

# Start API server
ollama serve
```

### Model Management
```bash
# Download a model
ollama pull mistral

# List installed models
ollama list

# Run interactive chat
ollama run mistral

# Delete a model
ollama rm mistral
```

### Chat Commands (Inside Model Session)
```bash
/?          # Show help
/bye        # Exit session
/reset      # Clear conversation
/system     # Set system prompt
```

---

## Python Quick Start

### Basic Chat
```python
import ollama

response = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Your question'}],
    options={'temperature': 0.8}
)

print(response['message']['content'])
```

### With Context
```python
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant'},
    {'role': 'user', 'content': 'First question'},
    {'role': 'assistant', 'content': 'First answer'},
    {'role': 'user', 'content': 'Follow-up question'}
]

response = ollama.chat(model='mistral', messages=messages)
```

### Streaming Response
```python
stream = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Tell me a story'}],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

---

## Power Automate Integration

### 1. Create HTTP Trigger Flow
1. Go to [make.powerautomate.com](https://make.powerautomate.com)
2. Create → Instant cloud flow
3. Add "When an HTTP request is received" trigger
4. Save and copy the URL

### 2. Python Code
```python
import ollama
import requests

# Get AI response
response = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Your prompt'}]
)

# Send to Power Automate
url = "YOUR_FLOW_URL_HERE"
payload = {'response': response['message']['content']}
r = requests.post(url, json=payload)

print(f"Status: {r.status_code}")
```

---

## Model Parameters

| Parameter | Range | Effect |
|-----------|-------|--------|
| `temperature` | 0.0 - 2.0 | Higher = more creative/random |
| `top_p` | 0.0 - 1.0 | Nucleus sampling threshold |
| `top_k` | 1 - 100 | Limits vocabulary selection |
| `repeat_penalty` | 0.0 - 2.0 | Reduces repetition |

### Example
```python
options = {
    'temperature': 0.7,
    'top_p': 0.9,
    'top_k': 40,
    'repeat_penalty': 1.1
}

response = ollama.chat(model='mistral', messages=messages, options=options)
```

---

## Popular Models

| Model | Size | Best For |
|-------|------|----------|
| `mistral` | 7B | General purpose, fast |
| `llama2` | 7B-70B | Conversational AI |
| `codellama` | 7B-34B | Code generation |
| `gemma` | 2B-7B | Lightweight tasks |
| `phi` | 2.7B | Small, efficient |

---

## Custom Models

### Create Modelfile
```
FROM mistral

SYSTEM You are a helpful coding assistant.

PARAMETER temperature 0.7
PARAMETER top_p 0.9
```

### Build Model
```bash
ollama create my_assistant -f Modelfile
```

### Use Model
```bash
ollama run my_assistant
```

---

## Troubleshooting

### Ollama Not Responding
```bash
# Check if running
ps aux | grep ollama  # Linux/Mac
Get-Process ollama    # Windows

# Restart service
ollama serve
```

### Connection Errors
- Default port: `11434`
- Check firewall settings
- Verify `http://localhost:11434` is accessible

### Model Not Found
```bash
# List available models
ollama list

# Pull missing model
ollama pull <model_name>
```

### Out of Memory
- Close other applications
- Use smaller models (phi, gemma 2B)
- Lower context window size

---

## Useful Resources

- **Documentation**: [ollama.com/docs](https://ollama.com/)
- **Model Library**: [ollama.com/library](https://ollama.com/library)
- **Python Package**: [github.com/ollama/ollama-python](https://github.com/ollama/ollama-python)
- **Community**: [discord.gg/ollama](https://discord.gg/ollama)

---

## File Locations

### Windows
- Models: `C:\Users\<username>\.ollama\models`
- Config: `%USERPROFILE%\.ollama`

### macOS
- Models: `~/.ollama/models`
- Config: `~/.ollama`

### Linux
- Models: `/usr/share/ollama/.ollama/models`
- Config: `~/.ollama`

---

**Print this card for quick reference! 📋**
