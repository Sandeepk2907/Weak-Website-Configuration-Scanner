from flask import Flask, render_template, request
import requests

app = Flask(__name__)


SECURITY_HEADERS = {
    "Content-Security-Policy": "Stops harmful scripts (XSS attacks)",
    "Strict-Transport-Security": "Forces secure connection (HTTPS)",
    "X-Frame-Options": "Prevents Clickjacking attacks",
    "X-Content-Type-Options": "Stops MIME type sniffing",
    "Referrer-Policy": "Controls referrer information leakage",
    "Permissions-Policy": "Restricts browser features (camera, mic, GPS)",
    "X-XSS-Protection": "Enables browser XSS filtering",
    "Cross-Origin-Opener-Policy": "Isolates browsing context (prevents data leaks)",
    "Cross-Origin-Resource-Policy": "Controls cross-origin resource sharing",
    "Cross-Origin-Embedder-Policy": "Prevents unauthorized cross-origin embeds",
    "Cache-Control": "Prevents sensitive data caching",
    "Clear-Site-Data": "Clears browser data on logout",
    "X-Permitted-Cross-Domain-Policies": "Restricts Adobe Flash/PDF cross-domain requests",
    "Expect-CT": "Enforces Certificate Transparency (prevents fake SSL certs)",
}

COMMON_ADMIN_PATHS = ["/admin", "/login", "/dashboard", "/wp-admin", "/admin/login", "/administrator"]


def check_headers(url):
    result = {}
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        for header, meaning in SECURITY_HEADERS.items():
            if header in headers:
                result[header] = {"status": "safe", "message": f" Present — {meaning}", "value": headers[header]}
            else:
                result[header] = {"status": "danger", "message": f" Missing — {meaning}", "value": None}

    except Exception as e:
        result["Error"] = {"status": "danger", "message": f"Could not connect: {str(e)}", "value": None}

    return result


def check_directory_listing(url):
    test_dirs = ["/uploads/", "/backup/", "/files/", "/images/", "/data/", "/logs/", "/tmp/"]
    vulnerable_dirs = []

    for d in test_dirs:
        try:
            r = requests.get(url + d, timeout=2)
            if "Index of" in r.text:
                vulnerable_dirs.append(d)
        except:
            pass

    return vulnerable_dirs


def check_admin_pages(url):
    exposed = []
    for path in COMMON_ADMIN_PATHS:
        try:
            r = requests.get(url + path, timeout=2)
            if r.status_code == 200:
                if "password" in r.text.lower() or "login" in r.text.lower():
                    exposed.append(f"{path} → Login Page Detected ")
                else:
                    exposed.append(f"{path} → Open Access ")
        except:
            pass
    return exposed


def get_summary(headers_result):
    total = len(headers_result)
    safe = sum(1 for v in headers_result.values() if v["status"] == "safe")
    missing = total - safe
    score = int((safe / total) * 100) if total > 0 else 0
    return {"total": total, "safe": safe, "missing": missing, "score": score}


@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    summary = {}

    if request.method == "POST":
        url = request.form["url"].strip()

        if not url.startswith("http"):
            url = "http://" + url

        result["headers"] = check_headers(url)
        result["directories"] = check_directory_listing(url)
        result["admin_pages"] = check_admin_pages(url)
        summary = get_summary(result["headers"])

    return render_template("index.html", result=result, summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
