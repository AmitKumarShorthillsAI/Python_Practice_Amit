This project implements a user authentication system using:
- **FastAPI (backend API)**
- **Django (HTML frontend)**
- **MySQL (Database)**
- **Selenium with Unittest (Browser Automation Testing)**

---


---

## 🚀 How to Run the Project

### 1. 📦 Install Requirements

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

Make sure to install:

    fastapi, uvicorn, sqlalchemy, python-dotenv

    django

    selenium

2. Start FastAPI Backend

cd fastapi_backend
uvicorn main:app --reload

This will run FastAPI at http://127.0.0.1:8000/

3. Start Django Frontend

cd django_frontend
python manage.py migrate
python manage.py runserver 9000

This will run Django HTML frontend at http://127.0.0.1:9000/

    Register: http://127.0.0.1:9000/register/

    Login: http://127.0.0.1:9000/login/


4. Run Selenium UI Tests

cd selenium_tests
python test_user_registration_login.py

The tests will:

    Open browser (Brave)

    Test valid/invalid registration

    Test valid/invalid login

⚙️ Configuration

    Make sure you have Brave browser installed.

    Ensure chromedriver is installed and available globally.

    Update path in options.binary_location in the Selenium script if needed.