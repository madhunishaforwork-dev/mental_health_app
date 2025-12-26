# How to Turn Your App into a Weblink (Deployment)

To make your Mental Health App accessible to anyone on the internet, you need to "deploy" it. I have prepared your project for deployment by creating a `Procfile` and updating `requirements.txt`.

Here are the two best ways to do this:

## Option 1: Permanent Free Website (Recommended)
This will generate a permanent URL (e.g., `https://my-mental-health-app.onrender.com`) that keeps running even when you close your computer. We will use **Render** (a popular free cloud provider).

### Step 1: Push Your Code to GitHub
1. Create a new repository on [GitHub](https://github.com/new).
2. Open your VS Code terminal in the project folder and run:
   ```bash
   git init
   git add .
   git commit -m "Initial deployment setup"
   # Replace the URL below with your new repository URL
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. Go to [dashboard.render.com](https://dashboard.render.com/) and create a free account.
2. Click **New +** and select **Web Service**.
3. Connect your GitHub account and select the repository you just pushed.
4. In the setup page, scroll down and make sure these settings are correct:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (This should be auto-detected from the Procfile I created)
   - **Instance Type**: Free
5. Click **Create Web Service**.

Wait a few minutes, and Render will give you a live URL!

---

## Option 2: Temporary Link (e.g. for testing)
If you just want to show a friend *right now* and don't care if the link stops working when you close your laptop, use **ngrok**.

1. Download and install [ngrok](https://ngrok.com/download).
2. Start your app locally in one terminal:
   ```bash
   python app.py
   ```
3. Open a **second** terminal and run:
   ```bash
   ngrok http 5000
   ```
4. Copy the `https://....ngrok-free.app` link shown in the terminal.
