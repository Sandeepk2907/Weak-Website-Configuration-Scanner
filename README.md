# Weak Website Configuration Scanner

A simple web-based security tool built with **Flask** that scans websites for common misconfigurations — including missing security headers, exposed directories, and accessible admin pages.

---

##  Features

-  **Security Header Check** — Detects missing HTTP security headers like `Content-Security-Policy` and `Strict-Transport-Security`
-  **Directory Listing Detection** — Checks for exposed directories like `/uploads/`, `/backup/`, `/files/`
-  **Admin Page Exposure** — Scans for publicly accessible admin paths like `/admin`, `/login`, `/dashboard`

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, CSS |
| HTTP Requests | `requests` library |

---

##  Project Structure

```
CNS/
│
├── app.py              # Flask backend — scanning logic & routes
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI (Jinja2 template)
└── static/
    └── style.css       # Styling
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weak-website-scanner.git
cd weak-website-scanner
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

##  How to Use

1. Enter a website URL in the input box (e.g., `https://example.com`)
2. Click **Scan Website**
3. View the results:
   -  **Safe** — header/config is properly set
   -  **Missing / Vulnerable** — potential misconfiguration detected

---

##  What Gets Scanned

### Security Headers
| Header | Purpose |
|--------|---------|
| `Content-Security-Policy` | Prevents harmful/injected scripts |
| `Strict-Transport-Security` | Forces HTTPS connections |

### Directory Listing
Checks if these paths are openly browsable:
- `/uploads/`
- `/backup/`
- `/files/`

### Admin Pages
Checks if these pages are publicly accessible:
- `/admin`
- `/login`
- `/dashboard`

---

## Disclaimer

> This tool is intended for **educational purposes only**.  
> Only scan websites you **own** or have **explicit permission** to test.  
> Unauthorized scanning of websites may be **illegal**.

---

## Requirements

```
flask
requests
```

Install with:
```bash
pip install -r requirements.txt
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

Made for learning web security concepts as part of a CNS (Computer and Network Security) project.
