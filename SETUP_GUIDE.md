# 🚀 Sales Analytics Dashboard - Setup Guide

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.10+** (Python 3.13 recommended)
- **Git** for cloning the repository
- **Node.js 18+** (for Tailwind CSS compilation)
- **pip** (Python package manager, comes with Python)

---

## 🔧 Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/ramonbonina320401-bot/Django-Sales-Dashboard-Report.git
cd Django-Sales-Dashboard-Report
```

### Step 2: Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> **Note:** If you encounter execution policy errors on Windows PowerShell, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Step 3: Install Python Dependencies

With your virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

**Required packages include:**
- Django 6.0
- django-tailwind 4.4.2
- numpy 2.3.5
- matplotlib 3.10.7
- pandas 2.3.3
- scikit-learn 1.7.2

### Step 4: Install Tailwind CSS

```bash
python manage.py tailwind install
```

This will install Node.js dependencies for Tailwind CSS.

### Step 5: Run Database Migrations

```bash
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) and all necessary tables.

### Step 6: Create Superuser (Optional but Recommended)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account. This allows you to access the Django admin panel at `/admin`.

### Step 7: Populate Sample Data

```bash
python manage.py populate_sales
```

This generates 4,678 sample sales records across 5 products for the past 365 days.

---

## ▶️ Running the Application

### Option 1: Run with Tailwind Auto-Compilation (Recommended for Development)

**Terminal 1 - Start Tailwind Compiler:**
```bash
python manage.py tailwind start
```

**Terminal 2 - Start Django Server:**
```bash
python manage.py runserver
```

### Option 2: Build Tailwind Once (For Production)

```bash
python manage.py tailwind build
python manage.py runserver
```

### Access the Dashboard

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

---

## 📦 System Requirements

### Minimum Requirements
- **RAM:** 4 GB
- **Storage:** 500 MB free space
- **Processor:** Dual-core CPU
- **OS:** Windows 10/11, macOS 10.14+, or Linux

### Recommended Requirements
- **RAM:** 8 GB or more
- **Storage:** 1 GB free space
- **Processor:** Quad-core CPU
- **OS:** Latest stable version

---

## 🗂️ Project Structure

```
Django-Sales-Dashboard-Report/
├── accounts/                   # User authentication (not used in current version)
├── dashboard/                  # Main application
│   ├── management/
│   │   └── commands/
│   │       └── populate_sales.py  # Data generation script
│   ├── migrations/             # Database migrations
│   ├── static/                 # Static CSS files
│   ├── templates/              # HTML templates
│   │   └── dashboard/
│   │       ├── base.html       # Base template
│   │       ├── sales.html      # Module 1: Sales Report
│   │       ├── market.html     # Module 2: Market Shares
│   │       ├── data.html       # Module 3: Raw Data
│   │       └── eval.html       # Module 4: Model Evaluation
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # URL routing
│   ├── reports.py              # OOP report classes
│   └── admin.py                # Admin configuration
├── djangowebapp/               # Project settings
│   ├── settings.py             # Main settings
│   └── urls.py                 # Root URL configuration
├── theme/                      # Tailwind CSS theme
├── db.sqlite3                  # SQLite database (generated)
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies
```

---

## 🎓 Features Overview

### Module 1: Sales Report
- **NumPy Calculations:** Sum, mean, median, standard deviation
- **Statistical Analysis:** Central tendency and data spread
- **Linear Regression:** Future sales prediction
- **Matplotlib Visualizations:** Line graphs and histograms

### Module 2: Market Shares
- **SQL Aggregation:** GROUP BY, SUM, ORDER BY
- **Market Share Analysis:** Dynamic percentage calculations
- **Matplotlib Charts:** Donut and bar charts
- **OOP Demonstration:** Class inheritance examples

### Module 3: Raw Data Previews
- **SQL Database Integration:** SELECT with JOIN operations
- **CRUD Operations:** Read and export functionality
- **JSON Handling:** json.dumps() and json.loads()
- **Data Export:** CSV and JSON formats

### Module 4: Model Evaluation
- **Machine Learning Classification:** Binary prediction
- **Confusion Matrix:** TP, FP, TN, FN calculations
- **Performance Metrics:** Accuracy, Precision, Recall, F1 Score
- **Regression vs Classification:** Clear distinction

---

## 🐛 Troubleshooting

### Issue: "Module not found" errors

**Solution:** Make sure your virtual environment is activated and all packages are installed:
```bash
pip install -r requirements.txt
```

### Issue: Tailwind CSS not working

**Solution:** Install Node.js dependencies:
```bash
python manage.py tailwind install
```

Then start the Tailwind compiler:
```bash
python manage.py tailwind start
```

### Issue: Database errors

**Solution:** Run migrations and regenerate data:
```bash
python manage.py migrate
python manage.py populate_sales
```

### Issue: Port 8000 already in use

**Solution:** Use a different port:
```bash
python manage.py runserver 8080
```

Or kill the existing process:

**Windows:**
```powershell
Get-Process python | Where-Object {$_.CommandLine -like "*runserver*"} | Stop-Process -Force
```

**macOS/Linux:**
```bash
lsof -ti:8000 | xargs kill -9
```

### Issue: Permission denied on PowerShell

**Solution:** Change execution policy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🔄 Updating the Application

To get the latest changes from the repository:

```bash
git pull origin main
pip install -r requirements.txt
python manage.py migrate
python manage.py tailwind install
```

---

## 📚 Additional Resources

### Django Documentation
- Official Docs: https://docs.djangoproject.com/
- Tutorial: https://docs.djangoproject.com/en/stable/intro/tutorial01/

### Python Libraries Used
- **NumPy:** https://numpy.org/doc/
- **Matplotlib:** https://matplotlib.org/stable/contents.html
- **Pandas:** https://pandas.pydata.org/docs/
- **scikit-learn:** https://scikit-learn.org/stable/

### Tailwind CSS
- Documentation: https://tailwindcss.com/docs
- django-tailwind: https://django-tailwind.readthedocs.io/

---

## 🆘 Getting Help

If you encounter any issues:

1. Check the **Troubleshooting** section above
2. Verify all prerequisites are installed correctly
3. Ensure your virtual environment is activated
4. Check that you're in the correct directory
5. Contact the project maintainer

---

## 📝 Quick Start Checklist

- [ ] Python 3.10+ installed
- [ ] Node.js 18+ installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Tailwind installed (`python manage.py tailwind install`)
- [ ] Database migrated (`python manage.py migrate`)
- [ ] Sample data populated (`python manage.py populate_sales`)
- [ ] Tailwind compiler running (`python manage.py tailwind start`)
- [ ] Django server running (`python manage.py runserver`)
- [ ] Browser opened to http://127.0.0.1:8000

---

## ⚙️ Environment Variables (Optional)

For production deployment, create a `.env` file:

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

---

## 🚀 Deployment Notes

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Use a production WSGI server (Gunicorn, uWSGI)
4. Use a production database (PostgreSQL, MySQL)
5. Serve static files with a web server (Nginx, Apache)
6. Enable HTTPS/SSL

---

**Last Updated:** December 9, 2025  
**Version:** 1.0.0  
**Maintainer:** ramonbonina320401-bot
