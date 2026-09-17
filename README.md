# CaptchaFlow - Captcha Solver API

> Universal captcha solving with the industry-standard createTask / getTaskResult protocol, 19 task types.

Part of the **DataLeads** API suite (Tools category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/createTask` | Create a captcha-solving task |
| POST | `/getTaskResult` | Poll for task result |
| POST | `/getBalance` | Check account balance |

## Quick start

```bash
curl -X POST https://captcha.dataleads.pro/v1/createTask \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "task": {"type": "RecaptchaV2TaskProxyless", "websiteURL": "https://example.com", "websiteKey": "SITE_KEY"}}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://captcha.dataleads.pro](https://captcha.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://captcha.dataleads.pro/mcp/captchaflow`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/captchaflow-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://captcha.dataleads.pro](https://captcha.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
