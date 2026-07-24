# 🌾 Dealer Finder Web Application

A **production-ready Dealer Finder** web application built with **FastAPI, HTML, CSS, and JavaScript**. The application allows users to quickly find nearby dealers using their current location or search by dealer name, pincode, district, or mobile number. It provides a clean, responsive interface along with one-click **Call**, **WhatsApp**, and **Google Maps Directions**.

---

## ✨ Features

* 🔍 Search dealers by:

  * Dealer Name
  * Pincode
  * District / Place
  * Mobile Number
* 📍 Find nearest dealers using current location
* 📏 Distance-based dealer sorting
* 📞 One-click phone calling
* 💬 WhatsApp integration
* 🗺️ Google Maps directions
* 📱 Mobile-first responsive design
* ⚡ FastAPI REST APIs
* 🏗️ Modular backend architecture
* ❤️ Clean and modern UI

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Jinja2 Templates
* Uvicorn

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)

### Data

* CSV Dataset

---

## 📂 Project Structure

```text
dealer-finder/
│
├── app.py
├── config.py
├── models.py
├── services.py
├── utils.py
├── dealers.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/dealer-finder.git
cd dealer-finder
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn app:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

---

## 📌 API Endpoints

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| GET    | `/`            | Home Page            |
| GET    | `/api/search`  | Search dealers       |
| GET    | `/api/nearest` | Find nearest dealers |
| GET    | `/health`      | Health Check         |

---

## 📱 Application Highlights

* Responsive design for desktop and mobile devices
* Fast dealer search with REST APIs
* Real-time location support
* Distance-based dealer recommendations
* Easy communication through Call and WhatsApp
* Google Maps integration for navigation

---

## 🔮 Future Improvements

* Database integration (MySQL/PostgreSQL)
* Dealer authentication
* Admin dashboard
* Dealer management panel
* Pagination and filtering
* Docker deployment
* Cloud deployment (AWS/Render)

---

