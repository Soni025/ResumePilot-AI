# 🚀 ResumePilot AI

**ResumePilot AI** is an AI-powered resume analysis platform that helps students, job seekers, and professionals enhance their resumes through intelligent feedback and role-specific recommendations. Built with **Streamlit**, **Python**, and the **OpenAI API**, the application evaluates resume quality, identifies improvement areas, and provides actionable suggestions to increase the chances of securing interviews.

---

## ✨ Key Features

- 📄 Upload resumes in **PDF** or **TXT** format
- 🎯 Receive personalized feedback tailored to a target job role
- 🤖 AI-powered analysis of resume content and structure
- 📈 Improve resume quality through:
  - Content enhancement
  - Skills presentation
  - Experience optimization
  - Keyword recommendations
- ⚡ Simple, interactive, and user-friendly web interface

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | OpenAI API |
| PDF Processing | PyPDF2 |
| Environment Management | Python Dotenv |
| Dependency Management | UV / pyproject.toml |

---

## 📂 Project Structure

```text
ResumePilot-AI/
│── main.py
│── README.md
│── pyproject.toml
│── python-version
│── uv.lock
└── .gitignore
```

---

## ⚙️ How It Works

1. Upload your resume in PDF or TXT format.
2. Enter the target job role (optional).
3. The application extracts the resume content.
4. An AI model evaluates the resume against industry best practices.
5. Personalized recommendations are generated to improve resume quality and relevance.

---

## 🎯 Applications

- Internship preparation
- Campus placements
- Software engineering roles
- Data science and AI roles
- Career transition and job applications
- Resume refinement for professionals

---

## 💡 Future Enhancements

- ATS (Applicant Tracking System) compatibility score
- Resume scoring dashboard
- DOCX file support
- Keyword gap analysis
- Resume rewriting suggestions
- Cover letter generation
- Job description matching
- Downloadable PDF feedback report

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/ResumePilot-AI.git
cd ResumePilot-AI
```

### Install Dependencies

```bash
uv sync
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run main.py
```

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

---

**Empowering better resumes through AI-driven insights.**
