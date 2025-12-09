# 📊 Django Sales Analytics Dashboard

A comprehensive educational Sales Analytics Dashboard built with Django, demonstrating advanced Python programming concepts including NumPy, Matplotlib, SQL, Machine Learning, JSON handling, and Object-Oriented Programming.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎯 Purpose

This project serves as an **educational demonstration** of Python programming concepts and data science techniques applied to a real-world sales analytics scenario. Perfect for learning or teaching:

- NumPy for numerical analysis
- Matplotlib for data visualization
- SQL database operations
- Machine Learning (Regression & Classification)
- JSON data handling
- Object-Oriented Programming with Inheritance

---

## ✨ Features

### 📈 Module 1: Sales Report
- **NumPy Statistical Analysis:** Sum, Mean, Median, Standard Deviation
- **Linear Regression:** Predict future sales using scikit-learn
- **Matplotlib Visualizations:** Line graphs and histograms
- Real-time calculations on 4,678+ sales records

### 📊 Module 2: Market Shares
- **SQL Aggregation:** Dynamic market share calculations
- **Matplotlib Charts:** Donut and bar charts
- **OOP Demonstration:** Class inheritance with GenericReport parent class
- Product performance ranking

### 💾 Module 3: Raw Data Previews
- **SQL Database Integration:** SELECT with JOIN operations
- **CRUD Operations:** Read, Export, Refresh functionality
- **JSON Handling:** Export data with json.dumps()
- CSV and JSON export options

### 🤖 Module 4: Model Evaluation
- **Machine Learning Classification:** Binary prediction model
- **Confusion Matrix:** TP, FP, TN, FN calculations
- **Performance Metrics:** Accuracy, Precision, Recall, F1 Score
- Clear distinction between Regression and Classification

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Node.js 18+ (for Tailwind CSS)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ramonbonina320401-bot/Django-Sales-Dashboard-Report.git
   cd Django-Sales-Dashboard-Report
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows PowerShell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python manage.py tailwind install
   ```

4. **Setup database and data:**
   ```bash
   python manage.py migrate
   python manage.py populate_sales
   ```

5. **Run the application:**
   ```bash
   # Terminal 1: Start Tailwind
   python manage.py tailwind start
   
   # Terminal 2: Start Django
   python manage.py runserver
   ```

6. **Open browser:**
   ```
   http://127.0.0.1:8000
   ```

📖 **For detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)**

---

## 🛠️ Tech Stack

### Backend
- **Django 6.0** - Web framework
- **Python 3.13** - Programming language
- **SQLite** - Database

### Data Science Libraries
- **NumPy 2.3.5** - Numerical computations
- **Matplotlib 3.10.7** - Data visualization
- **Pandas 2.3.3** - Data manipulation
- **scikit-learn 1.7.2** - Machine learning

### Frontend
- **Tailwind CSS v4** - Styling framework
- **Chart.js** - Interactive charts
- **Font Awesome 6.4** - Icons

---

## 📚 Learning Objectives

This project demonstrates:

✅ **Python Fundamentals**
- Variables, functions, control flow
- List comprehensions and dictionaries
- Module imports and package management

✅ **NumPy (Numerical Analysis)**
- `np.sum()` - Aggregation
- `np.mean()` - Central tendency
- `np.median()` - Percentile calculations
- `np.std()` - Data spread measurement
- `np.histogram()` - Distribution analysis

✅ **Matplotlib (Visualization)**
- Line graphs for trends
- Histograms for distributions
- Pie/Donut charts for proportions
- Bar charts for comparisons

✅ **SQL (Database Management)**
- SELECT, JOIN, GROUP BY, ORDER BY, LIMIT
- Aggregation functions (SUM, COUNT)
- Django ORM integration

✅ **Machine Learning**
- **Linear Regression** - Continuous value prediction
- **Classification** - Category prediction
- Confusion matrix evaluation
- Performance metrics calculation

✅ **JSON Handling**
- `json.dumps()` - Serialization
- `json.loads()` - Parsing
- Data export functionality

✅ **Object-Oriented Programming**
- Class inheritance
- Parent and child classes
- Method overriding
- Code reusability (DRY principle)

---

## 📁 Project Structure

```
Django-Sales-Dashboard-Report/
├── dashboard/              # Main application
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── reports.py         # OOP class hierarchy
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
├── djangowebapp/          # Project settings
├── theme/                 # Tailwind CSS
├── requirements.txt       # Python dependencies
├── SETUP_GUIDE.md        # Detailed setup instructions
├── LESSON_COVERAGE.md    # Educational documentation
└── manage.py             # Django management
```

---

## 📊 Sample Data

The system includes a management command that generates realistic sample data:

- **4,678 sales transactions**
- **5 different products** (Laptop, Mouse, Keyboard, Monitor, Headset)
- **365 days** of historical data
- Random but realistic quantities and pricing

Generate data with:
```bash
python manage.py populate_sales
```

---

## 🎨 UI Features

- **Dark/Light Theme Toggle** with localStorage persistence
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Interactive Charts** - Powered by Chart.js
- **Educational Panels** - Color-coded learning sections on each module
- **Functional Buttons** - All filters and exports work
- **Settings Modal** - Theme and preferences

---

## 📖 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete installation and troubleshooting guide
- **[LESSON_COVERAGE.md](LESSON_COVERAGE.md)** - Detailed breakdown of all educational concepts
- **[ENHANCEMENTS_SUMMARY.md](ENHANCEMENTS_SUMMARY.md)** - Feature enhancements overview

---

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork the repository
- Create feature branches
- Submit pull requests
- Report issues
- Suggest improvements

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Team Setup

For team members setting up the project, follow these steps:

1. Clone the repository
2. Read [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions
3. Install all dependencies from `requirements.txt`
4. Run migrations and populate sample data
5. Start both Tailwind and Django servers

All team members should be able to run the application smoothly by following the setup guide.

---

## 🐛 Troubleshooting

Common issues and solutions are documented in [SETUP_GUIDE.md](SETUP_GUIDE.md#-troubleshooting).

For additional help:
- Check that Python 3.10+ is installed
- Verify virtual environment is activated
- Ensure all dependencies are installed
- Confirm Tailwind CSS is running

---

## 📧 Contact

**Maintainer:** ramonbonina320401-bot  
**Repository:** https://github.com/ramonbonina320401-bot/Django-Sales-Dashboard-Report

---

## 🎓 Educational Use

Perfect for:
- Learning Python data science
- Understanding Django web development
- Teaching NumPy and Matplotlib
- Demonstrating OOP concepts
- Machine Learning fundamentals
- SQL database operations

---

**⭐ If you find this project helpful, please consider giving it a star!**

---

*Last Updated: December 9, 2025*
