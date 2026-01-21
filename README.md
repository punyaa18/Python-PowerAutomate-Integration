# Python Meets Power Automate: Trigger via URL

A compact, developer-friendly reference and working Python client for triggering Microsoft Power Automate flows via HTTP. It includes:

- Step-by-step setup for an HTTP-triggered flow
- A reusable Python script to POST/GET to your flow
- Sample payloads, environment config, and quick usage
- Security tips and common use cases

## Prerequisites
- A Power Automate environment and access to create flows
- A generated HTTP trigger URL (POST is typical)
- Python 3.9+ on your machine

## Setup: Power Automate HTTP Trigger
1. Open Power Automate (https://make.powerautomate.com).
2. Create an Instant cloud flow and choose "When an HTTP request is received".
3. Define the JSON schema for the request body if you plan to pass data (example in `examples/payload.json`).
4. Add one or more actions (e.g., send an email, update a SharePoint list).
5. Save the flow and copy the generated HTTP URL from the trigger card.

## Python Client
This repo provides `src/trigger_flow.py` to send HTTP requests to your flow with:
- JSON payload from file or inline
- Optional headers (Authorization Bearer, shared secret)
- `--dry-run` mode to preview without sending

### Install dependencies
```
python -m pip install -r requirements.txt
```

### Configure environment (optional but recommended)
Copy `.env.example` to `.env` and fill in values:
```
FLOW_URL=https://prod-00.westus.logic.azure.com/... (your flow URL)
FLOW_SECRET=your-shared-secret-if-used
FLOW_BEARER=your-bearer-token-if-used
```

### Try it (dry-run)
```
python src/trigger_flow.py --url "https://httpbin.org/post" --payload examples/payload.json --dry-run
```

### Send to your flow (POST)
```
python src/trigger_flow.py --url "<your-flow-url>" --payload examples/payload.json
```

### Inline data
```
python src/trigger_flow.py --url "<your-flow-url>" --data '{"username":"Mark.Holland","action":"start"}'
```

### Add headers
```
python src/trigger_flow.py --url "<your-flow-url>" --payload examples/payload.json --secret "my-shared-secret"
python src/trigger_flow.py --url "<your-flow-url>" --payload examples/payload.json --bearer "<token>"
python src/trigger_flow.py --url "<your-flow-url>" --payload examples/payload.json --header "X-Custom:Value" --header "Another:123"
```

## Use Cases
- Triggering workflows from external apps or scripts
- Webhooks and third-party integrations
- IoT devices sending events to Power Platform
- Custom buttons on internal web pages

## Security Tips
- Treat the flow URL as a secret; avoid public exposure.
- Use Azure API Management or Custom Connectors for governance.
- Validate a shared secret or token in your flow logic.
- Log and monitor flow invocations and failures.

## Repository Structure
```
.
├─ src/
│  └─ trigger_flow.py
├─ examples/
│  └─ payload.json
├─ .env.example
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## Publish to GitHub (optional)
1. Create a new empty repo on GitHub.
2. Run:
```
git init
git add .
git commit -m "Initial commit: Power Automate HTTP trigger + Python client"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Notes
- HTTP methods: GET (read), POST (create/trigger), PUT (update), DELETE (remove).
- Most flows will be POST; consider adopting a schema for structured data.