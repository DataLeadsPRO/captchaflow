import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://captcha.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('CaptchaFlow - Captcha Solver API')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "createTask",
    "method": "POST",
    "path": "/createTask",
    "description": "Create a captcha-solving task"
  },
  {
    "name": "getTaskResult",
    "method": "POST",
    "path": "/getTaskResult",
    "description": "Poll for task result"
  },
  {
    "name": "getBalance",
    "method": "POST",
    "path": "/getBalance",
    "description": "Check account balance"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
