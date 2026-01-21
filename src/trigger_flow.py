import argparse
import json
import os
from typing import Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv


def parse_headers(pairs: Optional[List[str]]) -> Dict[str, str]:
    headers: Dict[str, str] = {}
    if not pairs:
        return headers
    for p in pairs:
        if ":" in p:
            k, v = p.split(":", 1)
            headers[k.strip()] = v.strip()
    return headers


def load_payload(payload_path: Optional[str], inline_data: Optional[str]) -> Dict:
    if payload_path:
        with open(payload_path, "r", encoding="utf-8") as f:
            return json.load(f)
    if inline_data:
        return json.loads(inline_data)
    return {}


def build_headers(
    bearer: Optional[str], secret: Optional[str], extra: Dict[str, str]
) -> Dict[str, str]:
    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if bearer:
        headers["Authorization"] = f"Bearer {bearer}"
    if secret:
        headers["X-Shared-Secret"] = secret
    headers.update(extra)
    return headers


def print_summary(method: str, url: str, headers: Dict[str, str], payload: Dict):
    summary = {
        "method": method,
        "url": url,
        "headers": headers,
        "payload": payload,
    }
    print(json.dumps(summary, indent=2))


def request_with_method(
    method: str, url: str, payload: Dict, headers: Dict[str, str], timeout: int
) -> Tuple[int, str]:
    m = method.upper()
    if m == "GET":
        r = requests.get(url, params=payload, headers=headers, timeout=timeout)
    else:
        r = requests.request(m, url, json=payload, headers=headers, timeout=timeout)
    content: str
    try:
        content = json.dumps(r.json(), indent=2)
    except ValueError:
        content = r.text
    return r.status_code, content


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Trigger a Power Automate flow via HTTP"
    )
    parser.add_argument("--url", help="Flow trigger URL (or set FLOW_URL)")
    parser.add_argument(
        "--payload", help="Path to JSON payload file", default=None
    )
    parser.add_argument(
        "--data", help="Inline JSON string payload", default=None
    )
    parser.add_argument(
        "--method", help="HTTP method", default="POST", choices=["GET", "POST", "PUT", "DELETE"]
    )
    parser.add_argument(
        "--bearer", help="Auth Bearer token (or set FLOW_BEARER)", default=None
    )
    parser.add_argument(
        "--secret", help="Shared secret header (or set FLOW_SECRET)", default=None
    )
    parser.add_argument(
        "--header", help="Extra header as 'Key:Value'", action="append"
    )
    parser.add_argument(
        "--timeout", type=int, default=30, help="Request timeout seconds"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print request and exit"
    )

    args = parser.parse_args()

    url = args.url or os.getenv("FLOW_URL")
    if not url:
        raise SystemExit("Missing --url or FLOW_URL")

    bearer = args.bearer or os.getenv("FLOW_BEARER")
    secret = args.secret or os.getenv("FLOW_SECRET")

    extra_headers = parse_headers(args.header)
    payload = load_payload(args.payload, args.data)
    headers = build_headers(bearer, secret, extra_headers)

    if args.dry_run:
        print_summary(args.method, url, headers, payload)
        return

    status, content = request_with_method(
        args.method, url, payload, headers, args.timeout
    )
    print(f"Status: {status}")
    print(content)


if __name__ == "__main__":
    main()
