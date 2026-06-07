#  Weak Website Configuration Scanner

A Flask-based web tool that scans any website for common security misconfigurations — including missing security headers, open directory listings, and exposed admin pages — and gives an overall security score.

---

##  Features

-  Checks **14 security headers** and explains what each one does
-  Generates a **Security Score (%)** with a color-coded progress bar
-  Detects **open directory listings** (e.g. `/uploads/`, `/backup/`)
-  Scans for **exposed admin pages** (e.g. `/admin`, `/wp-admin`)
-  Clean dark-themed UI

---
## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, CSS |
| HTTP Requests | `requests` library |

---
##  Security Headers Checked

| Header | Purpose |
|--------|---------|
| `Content-Security-Policy` | Blocks harmful scripts (XSS attacks) |
| `Strict-Transport-Security` | Forces HTTPS connections |
| `X-Frame-Options` | Prevents Clickjacking |
| `X-Content-Type-Options` | Stops MIME type sniffing |
| `Referrer-Policy` | Controls referrer info leakage |
| `Permissions-Policy` | Restricts camera, mic, GPS access |
| `X-XSS-Protection` | Enables browser XSS filter |
| `Cross-Origin-Opener-Policy` | Isolates browsing context |
| `Cross-Origin-Resource-Policy` | Controls cross-origin resource sharing |
| `Cross-Origin-Embedder-Policy` | Prevents unauthorized cross-origin embeds |
| `Cache-Control` | Prevents sensitive data caching |
| `Clear-Site-Data` | Clears browser data on logout |
| `X-Permitted-Cross-Domain-Policies` | Restricts Flash/PDF cross-domain requests |
| `Expect-CT` | Enforces Certificate Transparency |

---

##  Project Structure

```
CNS/
├── app.py               # Flask backend — all scanning logic
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Frontend UI (Jinja2 template)
└── static/
    └── style.css        # Dark theme styles
```

---

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/website-config-scanner.git
cd website-config-scanner
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

### 4. Open in Browser
```
http://127.0.0.1:5000
```

---

##  Usage

1. Enter any website URL in the input box (e.g. `https://example.com`)
2. Click **Scan Website**
3. View results:
   - **Security Score** — overall percentage with color bar
   - **Headers Table** — each header's status and current value
   - **Directory Listing** — any open/exposed directories
   - **Admin Pages** — any accessible admin or login pages

---

##  Requirements

```
flask
requests
```

Install with:
```bash
pip install -r requirements.txt
```

---

##  Disclaimer

This tool is intended for **educational purposes** and **authorized security testing only**.  
Do **not** scan websites you do not own or have explicit permission to test.  
Unauthorized scanning may be **illegal** in your country.


---

##  License

This project is open-source and available under the [MIT License](LICENSE).
