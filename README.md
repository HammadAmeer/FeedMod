# FeedMod
Built a live feedback platform with Python (FastAPI) and JavaScript (AJAX) featuring admin moderation and real-time updates. Stored data persistently in SQLite and applied async handling for better UX.
Absolutely! Here’s a polished, professional `README.md` for your project — named **FeedMod** — that you can copy directly into your GitHub repo.

---

```markdown
# FeedMod 🗣️

**FeedMod** is a real-time feedback dashboard built using **FastAPI**, **JavaScript (AJAX)**, **HTML**, and **SQLite**. It allows users to submit live feedback while providing moderators with a separate admin panel to approve or reject submissions on the fly.

---

## 📌 Features

- 🚀 Real-time feedback submission using AJAX
- ✅ Admin moderation panel (Approve / Reject)
- 🗂️ Persistent storage via SQLite
- 🧩 Modular FastAPI backend
- 🔄 Auto-refreshing feedback list (polling)

---

## 🔧 Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Frontend  | HTML, CSS, JavaScript (Fetch API) |
| Backend   | Python, FastAPI    |
| Database  | SQLite + SQLAlchemy |
| Tools     | Uvicorn, CORS Middleware |

---

## 📸 Screenshots

### 🧑 User Feedback Panel
![User Feedback](screenshots/user_feedback.png)

### 🛡️ Admin Moderation Panel
![Admin Panel](screenshots/admin_panel.png)

---

## 📂 Folder Structure

```

FeedMod/
├── backend/
│   ├── main.py
│   ├── models.py
│   └── **init**.py
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── style.css
│   └── script.js
└── README.md

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/FeedMod.git
cd FeedMod
````

### 2. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### 3. Run the backend

```bash
uvicorn backend.main:app --reload
```

### 4. Open the frontend

* `frontend/index.html` → User view
* `frontend/admin.html` → Admin moderation panel

Use Live Server (VS Code extension) or simply double-click to open in browser.

---

## 🧠 How It Works

* Users submit feedback via a form using `fetch()`.
* Feedback is stored in a SQLite database with status `pending`.
* Admins view pending feedback and moderate it (approve/reject).
* Approved feedback is visible to all users in real-time via polling.

---

## 🏁 Future Improvements

* Add timestamps and usernames
* Add WebSocket support for true real-time push
* Deploy backend (Render/Railway) and frontend (Vercel/GitHub Pages)

---

## 📃 License

MIT License © 2025 [Hammad Ameer](https://www.linkedin.com/in/hammad-ameer/)

```

---

Let me know if you'd like the [screenshots section removed](f), a [logo/banner for GitHub](f), or a [deployment-ready version](f).
```
