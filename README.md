# flask-tutorial
VS Code Run through of Flask https://code.visualstudio.com/docs/python/tutorial-flask

This is a slimmed down view of the article above

```
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
python -m pip install --upgrade pip
python -m pip install flask
```

The rest of the files are:
- app.py (Code what to serve people via HTML or API)
- static/data.json (Needed for serving data via an API)
- templates/index.html (Used to serve content/UI)

## Let's checkout a similar frame work with FASTApi

```
pip install fastapi
pip install "uvicorn[standard]"
```

