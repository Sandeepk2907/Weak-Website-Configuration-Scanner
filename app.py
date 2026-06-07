from flask import Flask, render_template, request
import requests

app = Flask(__name__)


SECURITY_HEADERS = {
    "Content-Security-Policy": "Stops harmful scripts",
    "Strict-Transport-Security": "Forces secure connection (HTTPS)"
}

COMMON_ADMIN_PATHS = ["/admin", "/login", "/dashboard"]
  

def check_headers(url):
    result = {}
    try:
        response = requests.get(url, timeout=2)
        headers = response.headers

        for header, meaning in SECURITY_HEADERS.items():
            if header in headers:
                result[header] = f"Safe  ({meaning})"
            else:
                result[header] = f"Missing  ({meaning})"

    except Exception as e:
        result["Error"] = f"Could not connect to website: {str(e)}"

    return result


def check_directory_listing(url):
    test_dirs = ["/uploads/", "/backup/", "/files/"]
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
                    exposed.append(f"{path} → Login Required ")
                else:
                    exposed.append(f"{path} → Open Access ")
        except:
            pass
    return exposed


@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        url = request.form["url"].strip()

        
        if not url.startswith("http"):
            url = "http://" + url

        result["headers"] = check_headers(url)
        result["directories"] = check_directory_listing(url)
        result["admin_pages"] = check_admin_pages(url)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
