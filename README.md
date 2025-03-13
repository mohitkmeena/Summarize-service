# 🚀 Summarize Service (Flask + Mistral AI + MySQL)

This is a **Summarization Service** built using **Flask** and **Mistral AI**. It fetches a blog from **MySQL (blogdb)** based on `blog_id` and returns a **summarized version** of the blog.

---

## ⚡ Tech Stack
- **Flask** (Python Web Framework)
- **MySQL** (Database for Blog Storage)
- **Mistral AI** (Text Summarization)
- **Requests** (HTTP Client)
- **Python Dotenv** (Environment Variables)

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/mohitkmeena/summarize-service.git
cd summarize-service
```

### 2️⃣ Create a Virtual Environment  
```sh
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Add/Update `.env` File
```sh
# Database Config
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=blogdb

# Mistral AI API Key
MISTRAL_API_KEY=your-api-key
```

### 5️⃣ Run the Application  
```sh
python src/app/__init__.py
```

---

## 🔑 API Endpoints  

### 1️⃣ Blog Summarization Endpoint  

📌 **Summarize Blog by ID**  
```http
GET /summarize/{blog_id}
```
🔹 **Example Request (Using Curl)**
```sh
curl -X GET "http://localhost:5000/summarize/123"
```
🔹 **Example Request (Using Postman)**  
- **Method:** `GET`  
- **URL:** `http://localhost:5000/summarize/123`

🔹 **Response Schema (JSON)**
```json
{
  "blog_id": "123",
  "title": "Understanding REST APIs",
  "summary": "A quick guide on REST API principles and implementation."
}
```

---

## 🔐 Features  
- ✅ Fetches Blog Content from **MySQL (`blogdb`)**  
- ✅ Uses **Mistral AI** for **Summarization**  
- ✅ Simple & Fast **REST API**  

---
🚀 **Built with ❤️ by Mohit Kumar Meena**
