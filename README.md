# Minimal Web API (Flask) Template

A minimal, clean, and well-commented starter template for building a Web API with Python and Flask.

This repository is a **GitHub Template**. Click the "**Use this template**" button above to create your own new repository with this code.

## 🚀 How to Run This API

You can get this server running on your local machine in 3 steps.

### Step 1: Clone & Set Up

1.  **Create your repository:** Click "Use this template" to create a new repository in your account.
2.  **Clone your new repo:**
    ```bash
    git clone [https://github.com/YourUsername/your-new-repo-name.git](https://github.com/YourUsername/your-new-repo-name.git)
    cd your-new-repo-name
    ```
3.  **Create a Virtual Environment (Recommended):**
    ```bash
    # Create the environment
    python3 -m venv venv
    # Activate it (macOS/Linux)
    source venv/bin/activate
    # (Windows)
    # .\venv\Scripts\activate
    ```

### Step 2: Install Dependencies

With your virtual environment active, install Flask using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Server!

That's it. Now, run the `app.py` script:

```bash
python app.py
```

You will see output like this, which means your server is live:

```text
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
 * Debug mode: on
 * Running on [http://0.0.0.0:5000/](http://0.0.0.0:5000/) (Press CTRL+C to quit)
```

---

## Try Your Live API

Your API is now running. Open these URLs in your web browser:

* **Home:** `http://127.0.0.1:5000/`
    * *Should show: "Welcome to the Minimal Flask API!"*
* **JSON Data:** `http://127.0.0.1:5000/api/hello`
    * *Should show: `{"message": "Hello, world!", "status": "ok"}`*
* **Dynamic Route:** `http://127.0.0.1:5000/api/greet/Professor`
    * *Should show: `{"greeting": "Hello, Professor!", ...}`*
