# Python Meets Power Automate: Trigger via URL
(or read directly on - https://blogs.perficient.com/2025/07/16/python-meets-power-automate-trigger-via-url/ )
A compact, developer-friendly reference and working Python client for triggering Microsoft Power Automate flows via HTTP. It includes:

- Step-by-step setup for an HTTP-triggered flow
- A reusable Python script to POST/GET to your flow
- Sample payloads, environment config, and quick usage
- Security tips and common use cases

## Prerequisites
- A Power Automate environment and access to create flows
- A generated HTTP trigger URL (POST is typical)
- Python 3.9+ on your machine
This is what your flow would look like
<img width="750" height="379" alt="image" src="https://github.com/user-attachments/assets/b7d0acec-ae21-4724-87ce-9bad618c6061" />

## Setup: Power Automate HTTP Trigger
1. Open Power Automate (https://make.powerautomate.com).
2. Create an Instant cloud flow and choose "When an HTTP request is received".
3. Define the JSON schema for the request body if you plan to pass data (example in `examples/payload.json`).
4. Add one or more actions (e.g., send an email, update a SharePoint list).
5. Save the flow and copy the generated HTTP URL from the trigger card.
<img width="750" height="377" alt="image" src="https://github.com/user-attachments/assets/dfded0b4-6e01-44de-b70f-625097e8ed0c" />  
<img width="750" height="328" alt="image" src="https://github.com/user-attachments/assets/6c4eb3f3-652f-4dbd-addc-80c252578726" />  
<img width="750" height="378" alt="image" src="https://github.com/user-attachments/assets/92278dc4-484b-4e66-ac8f-d0c5b73a5380" />  
<img width="750" height="361" alt="image" src="https://github.com/user-attachments/assets/45284ca3-003b-4d48-ab39-a619b8268820" />   
   
## Python Client
This repo provides `src/trigger_flow.py` to send HTTP requests to your flow with:
- JSON payload from file or inline
- Optional headers (Authorization Bearer, shared secret)
- `--dry-run` mode to preview without sending

Important: Replace placeholder URLs with your own flow URL. The examples use `<your-flow-url>` or demo endpoints; you must paste the actual HTTP trigger URL from your Power Automate flow.

### Install dependencies
```
python -m pip install -r requirements.txt
```


### Send to your flow (POST)
```
python src/trigger_flow.py --url "<your-flow-url>" --payload examples/payload.json
```
<img width="742" height="550" alt="image" src="https://github.com/user-attachments/assets/d700258a-dc36-4bd1-a592-b5ae00998aec" />

Or use the simple example script in [examples/trigger_simple.py](examples/trigger_simple.py). Make sure to replace the `url` value in that file with your actual flow URL before running:
```
python examples/trigger_simple.py
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



