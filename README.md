# 🎓 AskUni

> A modern university community platform where students can ask questions, share knowledge, and help each other—all in one place.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)
![JWT](https://img.shields.io/badge/Auth-JWT-green.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

# 📖 Overview

AskUni is a university-focused Question & Answer platform inspired by Stack Overflow and Reddit, designed specifically for college students.

Students can:

- ❓ Ask academic and campus-related questions
- 💬 Answer questions from other students
- 👍 Upvote and downvote answers
- 🔍 Search for existing questions
- 👤 Manage their profiles
- 🔔 Receive notifications
- 📚 Build a helpful knowledge base for the university community

The platform aims to reduce repetitive questions in WhatsApp groups while creating a centralized hub for student discussions.

---

# ✨ Features

## 👤 Authentication

- User Registration
- Secure Login
- JWT Authentication
- Password Hashing
- Protected Routes
- Refresh Tokens

---

## 👨‍🎓 User Profile

- Edit Profile
- Upload Avatar
- Bio
- Department
- Batch
- Skills
- Reputation Score

---

## ❓ Questions

- Create Question
- Edit Question
- Delete Question
- View All Questions
- View Individual Question
- Tags
- Rich Text Support
- Search Questions

---

## 💬 Answers

- Post Answer
- Edit Answer
- Delete Answer
- Accept Answer
- Multiple Answers per Question

---

## 👍 Voting System

- Upvote
- Downvote
- Prevent Duplicate Voting
- Reputation Update

---

## 🔔 Notifications

Receive notifications when:

- Someone answers your question
- Someone upvotes your answer
- Someone mentions you
- Someone comments on your post

---

## 🔍 Search

Search by

- Title
- Tags
- User
- Keywords

---

## 📊 Dashboard

Users can view

- Total Questions
- Total Answers
- Reputation
- Recent Activity
- Saved Posts

---

## 🛡️ Security

- JWT Authentication
- Password Hashing (bcrypt)
- Input Validation
- SQL Injection Protection
- CORS
- Role-based Authorization

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- Uvicorn
- JWT
- Passlib
- Python

---

## Database

- PostgreSQL

---

## Frontend

- React
- Vite
- Tailwind CSS
- Axios

---

## Deployment

- Docker
- Nginx
- Render / Railway / VPS

---

# 📂 Project Structure

```
AskUni/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── middleware/
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── docs/
│
├── docker-compose.yml
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/askuni.git
```

```bash
cd askuni
```

---

## Backend Setup

Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env`

```env
DATABASE_URL=postgresql://user:password@localhost/askuni

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Database Migration

```bash
alembic upgrade head
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 💻 Frontend

```bash
cd frontend
```

Install

```bash
npm install
```

Run

```bash
npm run dev
```

---

# 📸 Screenshots

```
Add screenshots here
```

Examples

- Login
- Home Feed
- Ask Question
- Question Detail
- User Profile
- Dashboard

---

# 🚀 Future Improvements

- AI-powered answer suggestions
- Semantic search
- Real-time chat
- Dark mode
- Mobile application
- Email verification
- OAuth Login (Google/GitHub)
- File attachments
- Markdown editor
- Admin dashboard
- Recommendation engine
- Analytics dashboard

---

# 🧪 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
/docs
```

ReDoc

```
/redoc
```

---

# 📈 Roadmap

- [x] Authentication
- [x] User Profiles
- [x] Questions
- [x] Answers
- [x] Voting System
- [x] Search
- [x] Notifications
- [ ] AI Features
- [ ] Mobile App
- [ ] Deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Mohd Imran Siddiqui**

B.Tech Computer Science & Engineering

Passionate about Backend Development, FastAPI, AI/ML, and Open Source.

---

⭐ If you found this project useful, consider giving it a star!
