# Ollama Integration: Power Automate + VS Code

> **Run local AI models seamlessly with Power Automate workflows and VS Code development**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green.svg)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

This repository demonstrates how to integrate **Ollama** — a local Large Language Model (LLM) runtime — with **Power Automate** and **VS Code** to create powerful, privacy-focused AI workflows. Run models like LLaMA2, Mistral, or Gemma entirely on your machine without cloud dependencies.

### Why This Matters

- **🔒 Privacy-First**: Keep sensitive data local — no cloud APIs required
- **⚡ Real-Time Automation**: Trigger AI-powered workflows with Power Automate
- **🛠️ Developer-Friendly**: Full VS Code integration with Python
- **🌐 Offline Capable**: Works without internet connectivity
- **🎯 Custom Models**: Build and deploy your own models using Modelfiles

## Features

- ✅ Complete Ollama installation and setup guide
- ✅ Terminal command reference for model management
- ✅ VS Code Python integration examples
- ✅ Power Automate workflow templates
- ✅ Model interaction best practices
- ✅ Local API server configuration

## Quick Start

### Prerequisites

- Windows, macOS, or Linux
- Python 3.7 or higher
- VS Code (recommended)
- 8GB+ RAM (16GB recommended for larger models)

### Installation

1. **Install Ollama**
   ```bash
   # Visit https://ollama.com/download
   # Run the installer for your OS
   
   # Verify installation
   ollama --version
   ```

2. **Download a Model**
   ```bash
   # Pull a model (e.g., Mistral)
   ollama pull mistral
   
   # Verify download
   ollama list
   ```

3. **Install Python Package**
   ```bash
   pip install ollama
   ```

4. **Run Your First Query**
   ```bash
   ollama run mistral
   ```

## Usage Examples

### Python Integration (VS Code)

```python
import ollama

response = ollama.chat(
    model='mistral',
    messages=[{
        'role': 'user',
        'content': 'Explain quantum computing in simple terms'
    }],
    options={
        'temperature': 0.8  # More creative responses
    }
)

print(response['message']['content'])
```

### Terminal Commands

| Command | Description | Example |
|---------|-------------|---------|
| `ollama run <model>` | Start interactive chat | `ollama run mistral` |
| `ollama pull <model>` | Download a model | `ollama pull llama2` |
| `ollama list` | List installed models | `ollama list` |
| `ollama serve` | Start API server | `ollama serve` |

### In-Chat Commands

While interacting with a model:

- `/?` or `/help` - Show available commands
- `/bye` - Exit chat session
- `/system` - Set system prompt
- `/reset` - Clear conversation history

## Repository Structure

```
PA+VScode/
├── README.md                      # This file
├── blog.md                        # Complete tutorial blog post
├── POWER_AUTOMATE_SETUP.md        # Power Automate integration guide
├── GITHUB_SETUP.md                # GitHub setup instructions
├── CONTRIBUTING.md                # Contribution guidelines
├── LICENSE                        # MIT License
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
├── examples/
│   ├── basic_chat.py             # Simple chat example
│   ├── multi_turn_chat.py        # Conversation with context
│   ├── power_automate.py         # Flask API server
│   ├── flow_trigger_complete.py  # Complete flow trigger example
│   └── custom_model.py           # Custom model creation
└── modelfiles/
    ├── python_assistant.modelfile # Python coding assistant
    └── email_assistant.modelfile  # Email response assistant
```

## Documentation

**📘 Main Guides:**
- **[blog.md](blog.md)** - Complete tutorial and walkthrough
- **[POWER_AUTOMATE_SETUP.md](POWER_AUTOMATE_SETUP.md)** - Detailed Power Automate integration guide
- **[GITHUB_SETUP.md](GITHUB_SETUP.md)** - Instructions for pushing to GitHub
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines

**What you'll learn:**
- What Ollama is and why you need it
- Complete installation walkthrough
- Model selection and management
- VS Code Python integration
- Power Automate workflow creation
- Advanced customization options

## Available Models

Explore models at [ollama.com/library](https://ollama.com/library):

- **llama2** - Meta's powerful open-source model
- **mistral** - Fast and efficient 7B parameter model
- **gemma** - Google's lightweight AI model
- **codellama** - Specialized for code generation
- **phi** - Microsoft's small but capable model

## Power Automate Integration

This project enables you to:

1. Trigger AI responses from Power Automate flows
2. Generate automated email replies
3. Summarize content for SharePoint
4. Log AI interactions to Teams
5. Create custom approval workflows

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, open an issue first to discuss proposed changes.

## Troubleshooting

**Model not responding?**
- Ensure Ollama is running: `ollama serve`
- Check if model is downloaded: `ollama list`

**Connection issues?**
- Verify Ollama is running on port 11434 (default)
- Check firewall settings for localhost connections

**Performance issues?**
- Close unnecessary applications
- Use smaller models (e.g., phi instead of llama2)
- Adjust temperature settings for faster responses

## Resources

- [Ollama Official Documentation](https://ollama.com/)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Model Library](https://ollama.com/library)
- [Python Package Documentation](https://github.com/ollama/ollama-python)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Punyaa Dixit**

## Acknowledgments

- Ollama team for creating an excellent local LLM runtime
- The open-source AI community
- Contributors to this repository

---

⭐ **Star this repository** if you find it helpful!

🔗 **Share** with others building AI-powered automation workflows
