# ToolHub - Free, Open-Source & Privacy-Friendly Web Tools

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Flask Framework](https://img.shields.io/badge/framework-Flask%203.0-green.svg)](https://flask.palletsprojects.com/)
[![Vercel Deployment](https://img.shields.io/badge/deploy-Vercel-black.svg)](https://vercel.com)

**ToolHub** is a free, privacy-first, open-source online platform providing powerful tools for developers, students, content creators, and everyday users.

---

## 🚀 Deploying to Vercel (Step-by-Step)

ToolHub is configured for zero-config serverless deployment on **Vercel** using `@vercel/python`.

### Method 1: Deploy via Vercel Dashboard (GitHub Integration)

1. **Push Code to GitHub:**
   ```bash
   git add .
   git commit -m "Configure Vercel serverless deployment"
   git push origin main
   ```

2. **Import Project to Vercel:**
   - Go to [vercel.com/new](https://vercel.com/new).
   - Select your GitHub repository (`toolhub`).
   - Framework Preset: **Other**.
   - Root Directory: `./`.

3. **Configure Environment Variables in Vercel:**
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: `[generate-random-32-byte-secret]`
   - *(Optional)* `DATABASE_URL`: Your Supabase / Neon / Vercel Postgres URI.

4. **Click Deploy!**
   Vercel will build the project and issue a live serverless URL (e.g. `https://toolhub.vercel.app`).

---

### Method 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Log in to Vercel
vercel login

# Deploy to Production
vercel --prod
```

---

## 🌐 Connecting Custom Subdomain on Vercel (`toolhub.runs-at.dev` or `toolhub.MYDOMAIN.com`)

1. Go to your **Vercel Project Dashboard** -> **Settings** -> **Domains**.
2. Enter your custom subdomain: `toolhub.runs-at.dev` (or `toolhub.MYDOMAIN.com`) and click **Add**.
3. Vercel will show the required DNS record:
   - **Type:** `CNAME`
   - **Name:** `toolhub`
   - **Value:** `cname.vercel-dns.com`
4. Log into your DNS provider (e.g. Cloudflare, Namecheap, GoDaddy, or `runs-at.dev` dashboard) and add the `CNAME` record.
5. Vercel automatically verifies the domain and provisions a free SSL certificate within seconds.

---

## 🏗️ Project Architecture for Vercel

```text
ToolHub/
├── vercel.json             # Vercel deployment routes & @vercel/python builder
├── api/
│   └── index.py            # Vercel Serverless Function entrypoint
├── app.py                  # Main Flask application
├── config.py               # Environment & Vercel /tmp database fallback
├── tool_registry.py        # Centralized tool registry definitions
├── requirements.txt        # Python package dependencies
├── static/                 # Static assets (CSS, JS, PWA manifest, service-worker)
├── templates/              # HTML workspace templates
└── tests/                  # Pytest automated test suite
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).
