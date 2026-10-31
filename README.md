# 💻 Xompiler v1.0 — Local Discord Code Execution Bot

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Discord.py](https://img.shields.io/badge/discord.py-2.0+-5865F2?logo=discord&logoColor=white)
![E2B](https://img.shields.io/badge/Sandbox-E2B_SDK-orange)
![Platform](https://img.shields.io/badge/Host-Local_PC-lightgrey)

**Xompiler v1.0** is the initial local-hosted prototype of the Xompiler Discord bot. It runs directly from a local machine (`bot.py`) while offloading untrusted user code execution to secure, isolated **E2B Cloud Sandboxes** so local system files and hardware remain completely protected.

---

## ✨ Key Features (v1.0)
* **Local Host, Cloud Execution:** Runs the Discord bot client locally on your PC while executing all `!run` commands inside disposable E2B micro-VMs.
* **Zero Local Risk:** Malicious or heavy user scripts execute inside an isolated Linux container rather than on your personal computer.
* **Markdown Parsing:** Automatically strips Discord code blocks (` ```py ... ``` `) before sending code to the compiler.
* **Pre-Loaded Libraries:** Supports Python 3 along with `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`, `requests`, and `psutil` out of the box.

---

## 🛠️ Project Structure
```text
e2b-discord-bot/
├── bot.py             # Main Discord bot & E2B sandbox handler
├── requirements.txt   # Required Python dependencies
└── .env               # Local secret keys (Not uploaded to GitHub)
```

---

## ⚙️ Local Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Yashbhende123/Xompiler.git](https://github.com/Yashbhende123/Xompiler.git)
cd Xompiler
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install discord.py e2b-code-interpreter python-dotenv
```
*(Or run `pip install -r requirements.txt`)*

### 3. Configure Environment Variables (`.env`)
Create a file named `.env` in the project folder and add your Discord Bot Token and E2B API Key:
```env
DISCORD_TOKEN=your_discord_bot_token_here
E2B_API_KEY=your_e2b_api_key_here
```

### 4. Run the Bot Locally
Open Command Prompt or PowerShell inside your project directory and run:
```bash
python bot.py
```

---

## 🚀 Usage in Discord

Once your local terminal displays `✅ Logged in as Xompiler`, test it in any Discord channel the bot has access to:

**Single-line execution:**
```text
!run print("Xompiler v1.0 running from my local PC!")
```

**Multi-line code block execution:**
```text
!run ```python
for i in range(1, 6):
    print(f"Step {i}: Sandbox execution active!")
```
```

---

## 🔄 Evolution to Xompiler 2.0 (Cloud Edition)
Because v1.0 required keeping a local terminal open on the host PC, it was later upgraded to **Xompiler 2.0**, which added:
* Asynchronous thread offloading (`asyncio.to_thread()`) to prevent event-loop blocking.
* A background `Flask` keep-alive server.
* 24/7 cloud deployment on **Render** paired with **UptimeRobot** monitoring.
