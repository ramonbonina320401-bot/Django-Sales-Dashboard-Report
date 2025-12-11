# 📊 Django Sales Analytics Dashboard

A professional Sales Analytics Dashboard with CRUD operations, built with Django. Features real-time data visualization, product and sales management, machine learning predictions, and a modern dark/light theme interface.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎯 Overview

This project is a full-stack web application that combines data analytics, machine learning, and CRUD operations for managing sales data. It demonstrates Python programming concepts including NumPy, Matplotlib, SQL, Machine Learning (Regression & Classification), JSON handling, and Object-Oriented Programming.

**Key Features:**
- Complete CRUD operations for Products and Sales
- Real-time analytics dashboard with interactive charts
- Machine learning predictions
- Dark/Light theme with settings persistence
- Duplicate prevention with case-insensitive validation
- Auto-calculation for revenue, cost, and profit
- CSV and JSON export functionality

---

## ✨ Features by Module

### 📈 Module 1: Sales Dashboard
**Lessons Integrated:**
- **NumPy:** Statistical calculations (sum, mean, median, standard deviation)
- **Linear Regression:** Sales forecasting using scikit-learn
- **Matplotlib:** Line charts for monthly trends, histograms for distribution

**Functions:**
- `sales()` - Main dashboard view with comprehensive analytics
- Calculates total revenue, total capital, gross profit, and profit margin
- Monthly sales trends visualization
- Sales distribution by product category
- Real-time statistical analysis on all sales records

**What It Does:**
- Aggregates sales data using NumPy functions
- Predicts next month's sales using Linear Regression
- Visualizes data with interactive Chart.js graphs
- Provides filtering by product category (All, Laptop, Mouse, etc.)

---

### 📊 Module 2: Market Analysis
**Lessons Integrated:**
- **SQL:** Database queries with aggregation (GROUP BY, SUM)
- **OOP:** Class inheritance (GenericReport → MarketShareReport)
- **Matplotlib:** Pie charts, donut charts, bar charts

**Functions:**
- `market()` - Market share analysis view
- `MarketShareReport` class inheriting from `GenericReport`
- SQL queries using Django ORM for product-wise aggregation

**What It Does:**
- Calculates market share percentage for each product
- Ranks products by sales performance
- Displays product contribution to total revenue
- Uses inheritance to demonstrate DRY (Don't Repeat Yourself) principle

---

### 💾 Module 3: Raw Data & Export
**Lessons Integrated:**
- **SQL:** JOIN operations, SELECT queries
- **JSON:** Serialization with json.dumps()
- **CSV:** Data export functionality

**Functions:**
- `data()` - Raw data table view
- `export_csv()` - Export sales data as CSV file
- `export_json()` - Export sales data as JSON file

**What It Does:**
- Displays last 100 sales transactions with product details
- Joins SalesData and Product tables using SQL
- Exports data in CSV format for Excel analysis
- Exports data in JSON format for API integration
- Refresh button to reload latest data

---

### 🤖 Module 4: Model Evaluation
**Lessons Integrated:**
- **Machine Learning:** Classification model
- **Confusion Matrix:** True Positives, False Positives, True Negatives, False Negatives
- **Metrics:** Accuracy, Precision, Recall, F1 Score

**Functions:**
- `eval()` - Model performance evaluation view
- Binary classification for high/low sales prediction
- Performance metrics calculation

**What It Does:**
- Evaluates machine learning model performance
- Displays confusion matrix visualization
- Calculates accuracy, precision, recall, F1 score
- Demonstrates difference between Regression (Module 1) and Classification (Module 4)

---

### ➕ CRUD Operations (Add/Edit/Delete)
**Lessons Integrated:**
- **Django Forms:** Form validation and processing
- **SQL:** INSERT, UPDATE, DELETE operations
- **JavaScript:** Auto-calculation, input validation

**Functions:**
- `product_create()` - Add new product
- `product_update(pk)` - Edit existing product
- `product_delete(pk)` - Delete product
- `salesdata_create()` - Add new sales record
- `salesdata_update(pk)` - Edit existing sales record
- `salesdata_delete(pk)` - Delete sales record

**What It Does:**
- **Product Management:**
  - Add products with name, category, price, cost
  - Prevents duplicate names (case-insensitive)
  - Auto-converts names to Title Case
  - Edit/Delete existing products
  
- **Sales Management:**
  - Add sales records with product selection
  - Auto-calculates revenue (quantity × price)
  - Auto-calculates cost (quantity × product cost)
  - Auto-calculates profit (revenue - cost)
  - Date picker for transaction date
  - Edit/Delete existing sales records

---

## 🚀 Setup Instructions

### Prerequisites
Before you begin, ensure you have:
- **Python 3.10 or higher** ([Download](https://www.python.org/downloads/))
- **Node.js 18+** ([Download](https://nodejs.org/)) - Required for Tailwind CSS
- **Git** ([Download](https://git-scm.com/downloads))

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/ramonbonina320401-bot/Django-Sales-Dashboard-Report.git
cd Django-Sales-Dashboard-Report
```

#### 2. Create Virtual Environment
**Windows PowerShell:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Verify activation:** You should see `(venv)` at the start of your command line.

#### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

**What gets installed:**
- Django 6.0 - Web framework
- NumPy 2.3.5 - Numerical analysis
- Matplotlib 3.10.7 - Data visualization
- Pandas 2.3.3 - Data manipulation
- scikit-learn 1.7.2 - Machine learning
- django-tailwind - CSS framework integration

#### 4. Install Tailwind CSS
```bash
python manage.py tailwind install
```

This installs Node.js dependencies needed for Tailwind CSS compilation.

#### 5. Setup Database
```bash
python manage.py migrate
```

This creates the SQLite database with all necessary tables:
- Product table
- SalesData table
- User authentication tables

#### 6. Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

Follow prompts to create username and password for Django admin access.

#### 7. Populate Sample Data
```bash
python manage.py populate_sales
```

This generates:
- 5 products (Laptop, Mouse, Keyboard, Monitor, Headset)
- 4,678+ sales transactions
- 365 days of historical data
- Realistic pricing and quantities

#### 8. Run the Application

**Option A: Two Terminals (Recommended)**

Terminal 1 - Tailwind CSS:
```bash
python manage.py tailwind start
```

Terminal 2 - Django Server:
```bash
python manage.py runserver
```

**Option B: One Terminal (Background Tailwind)**

Windows PowerShell:
```powershell
Start-Process python -ArgumentList "manage.py","tailwind","start" -WindowStyle Hidden
python manage.py runserver
```

#### 9. Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:8000
```

**Default Login:**
- Create an account using the Signup page
- Or use the superuser account created in Step 6

---

## 🛠️ Tech Stack

### Backend
- **Django 6.0** - Web framework
- **Python 3.13** - Programming language
- **SQLite** - Database (db.sqlite3)

### Data Science Libraries
- **NumPy 2.3.5** - Numerical computations (`np.sum`, `np.mean`, `np.std`)
- **Matplotlib 3.10.7** - Chart generation (line, pie, bar charts)
- **Pandas 2.3.3** - Data manipulation and CSV export
- **scikit-learn 1.7.2** - Machine learning (LinearRegression, metrics)

### Frontend
- **Tailwind CSS v4** - Utility-first CSS framework
- **Chart.js** - Interactive JavaScript charts
- **Font Awesome 6.4** - Icon library
- **Vanilla JavaScript** - Theme switching, auto-calculations

---

## 📁 Project Structure

```
Django-Sales-Dashboard-Report/
├── accounts/                    # User authentication
│   ├── views.py                # Login, signup, logout
│   ├── urls.py                 # Auth URL routing
│   └── templates/              # Login/signup forms
│
├── dashboard/                   # Main application
│   ├── models.py               # Product & SalesData models
│   ├── forms.py                # ProductForm & SalesDataForm
│   ├── views.py                # All view functions (CRUD + Analytics)
│   ├── reports.py              # OOP classes (GenericReport, MarketShareReport)
│   ├── urls.py                 # Dashboard URL routing
│   ├── management/             # Custom management commands
│   │   └── populate_sales.py  # Sample data generator
│   ├── migrations/             # Database migrations
│   └── templates/              # HTML templates
│       └── dashboard/
│           ├── base.html       # Layout with sidebar and theme
│           ├── sales.html      # Module 1: Sales Dashboard
│           ├── market.html     # Module 2: Market Analysis
│           ├── data.html       # Module 3: Raw Data & Export
│           ├── eval.html       # Module 4: Model Evaluation
│           ├── product_form.html           # Add/Edit Product
│           ├── product_confirm_delete.html # Delete Product
│           ├── salesdata_form.html         # Add/Edit Sales
│           └── salesdata_confirm_delete.html # Delete Sales
│
├── djangowebapp/               # Project settings
│   ├── settings.py            # Configuration
│   ├── urls.py                # Root URL routing
│   └── wsgi.py                # WSGI config
│
├── theme/                      # Tailwind CSS
│   ├── static_src/            # Source CSS
│   └── static/                # Compiled CSS
│
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

---

## 🐛 Troubleshooting Guide

### Issue 1: "python: command not found" or "python3: command not found"
**Problem:** Python is not installed or not in system PATH.

**Solution:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Restart your terminal
4. Verify: `python --version` should show Python 3.10+

---

### Issue 2: "Permission denied" when activating virtual environment
**Problem:** PowerShell execution policy blocks script execution.

**Solution (Windows):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then retry: `.\venv\Scripts\Activate.ps1`

---

### Issue 3: "Module not found" errors
**Problem:** Dependencies not installed or virtual environment not activated.

**Solution:**
1. Ensure virtual environment is active: `(venv)` should appear in terminal
2. If not, activate it: `.\venv\Scripts\Activate.ps1` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Reinstall dependencies: `pip install -r requirements.txt`
4. Verify installation: `pip list`

---

### Issue 4: "Port 8000 is already in use"
**Problem:** Another Django server is running on port 8000.

**Solution:**
Option A - Kill existing process:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

Option B - Use different port:
```bash
python manage.py runserver 8080
```
Then access: `http://127.0.0.1:8080`

---

### Issue 5: Tailwind CSS not compiling (blank styles)
**Problem:** Node.js not installed or Tailwind not started.

**Solution:**
1. Install Node.js from [nodejs.org](https://nodejs.org/)
2. Verify: `node --version` (should be 18+)
3. Install Tailwind: `python manage.py tailwind install`
4. Start Tailwind: `python manage.py tailwind start`
5. Keep this terminal running while developing

---

### Issue 6: "No module named 'dashboard'"
**Problem:** Running commands from wrong directory.

**Solution:**
1. Navigate to project root: `cd Django-Sales-Dashboard-Report`
2. Verify: `ls` should show `manage.py`
3. Run commands from this directory

---

### Issue 7: Database migration errors
**Problem:** Database schema out of sync with models.

**Solution:**
```bash
# Delete database and start fresh
rm db.sqlite3  # Mac/Linux
del db.sqlite3  # Windows

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
python manage.py populate_sales
```

---

### Issue 8: "CSRF verification failed"
**Problem:** Browser cookies or session issues.

**Solution:**
1. Clear browser cache and cookies
2. Try incognito/private browsing mode
3. Restart Django server
4. Ensure `CSRF_COOKIE_SECURE = False` in settings.py for local development

---

### Issue 9: Charts not displaying
**Problem:** JavaScript errors or Chart.js not loading.

**Solution:**
1. Open browser DevTools (F12)
2. Check Console tab for errors
3. Verify internet connection (Chart.js loads from CDN)
4. Hard refresh page: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

---

### Issue 10: Can't create duplicate products
**Problem:** Product name already exists (case-insensitive check).

**Solution:**
This is intentional! The system prevents duplicates:
- "laptop", "LAPTOP", "Laptop" are all treated as the same product
- Use a different name or edit the existing product
- All product names are auto-converted to Title Case

---

### Issue 11: Auto-calculation not working in sales form
**Problem:** JavaScript not loading or product data missing.

**Solution:**
1. Ensure you've created at least one product first
2. Check browser Console (F12) for JavaScript errors
3. Verify product has both price and cost set
4. Hard refresh page: Ctrl+F5

---

### Issue 12: Settings not saving (theme/animations/auto-refresh)
**Problem:** localStorage blocked or browser privacy settings.

**Solution:**
1. Allow cookies and local storage in browser settings
2. Disable "Clear cookies on exit" setting
3. Try different browser
4. Check browser Console for errors

---

### Issue 13: Virtual environment packages not found after restart
**Problem:** Virtual environment not activated after closing terminal.

**Solution:**
Always activate before running commands:
```bash
# Windows
.\venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate
```

**Tip:** You should see `(venv)` in your terminal prompt when active.

---

### Issue 14: "Tailwind install" fails
**Problem:** Node.js/npm installation issues.

**Solution:**
1. Uninstall and reinstall Node.js
2. Clear npm cache: `npm cache clean --force`
3. Retry: `python manage.py tailwind install`
4. Check `theme/package.json` exists

---

## 💡 Pro Tips

**Tip 1: Quick Restart**
Create a batch/shell script to start both servers:

Windows (`start.bat`):
```batch
start cmd /k ".\venv\Scripts\Activate.ps1; python manage.py tailwind start"
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

Mac/Linux (`start.sh`):
```bash
#!/bin/bash
source venv/bin/activate
python manage.py tailwind start &
python manage.py runserver
```

**Tip 2: Use Django Admin**
Access admin panel at `http://127.0.0.1:8000/admin/` to:
- View all database records
- Manually add/edit/delete data
- See relationships between tables

**Tip 3: Sample Data Refresh**
Reset sample data anytime:
```bash
python manage.py flush  # Clears all data
python manage.py populate_sales  # Regenerates sample data
```

**Tip 4: Check Logs**
If something isn't working:
1. Check terminal output for Django errors
2. Open browser DevTools (F12) → Console tab
3. Look for red error messages

---

## 📚 Learning Resources

### Python Concepts Used
- **Variables & Data Types:** Strings, integers, floats, lists, dictionaries
- **Functions:** def keyword, parameters, return values
- **Loops:** for loops with range, list iteration
- **Conditionals:** if/elif/else statements
- **List Comprehensions:** [x for x in list]
- **Dictionary Operations:** .get(), .items(), .values()

### NumPy Functions
- `np.sum(array)` - Add all elements
- `np.mean(array)` - Calculate average
- `np.median(array)` - Find middle value
- `np.std(array)` - Measure spread
- `np.array(list)` - Convert list to array

### Django ORM (SQL Equivalent)
```python
# SELECT * FROM products
Product.objects.all()

# SELECT * FROM products WHERE category = 'Electronics'
Product.objects.filter(category='Electronics')

# SELECT SUM(revenue) FROM salesdata GROUP BY product
SalesData.objects.values('product').annotate(total=Sum('revenue'))

# SELECT * FROM salesdata JOIN products ON...
SalesData.objects.select_related('product')
```

### Machine Learning Flow
1. **Prepare Data:** Collect X (features) and y (target)
2. **Train Model:** `model.fit(X, y)`
3. **Make Predictions:** `model.predict(X_new)`
4. **Evaluate:** Calculate accuracy, precision, recall, F1

---

## 🎨 UI Features

### Settings Panel
Access via gear icon (⚙️) in top right:

**Theme Switcher:**
- **Dark Mode:** Default professional dark theme
- **Light Mode:** High-contrast light theme
- Persists across page refreshes using localStorage

**Display Settings:**
- **Animations:** Enable/disable CSS transitions and animations
- **Auto-refresh Data:** Automatically reload page every 30 seconds

All settings are saved to browser localStorage and applied immediately.

### Navigation
**Sidebar Menu:**
- 📊 Sales - Main analytics dashboard
- 📈 Market - Product market share analysis  
- 💾 Data - Raw sales data table
- 🎯 Evaluation - ML model performance
- ➕ Add Product - Create new product (green icon)
- 🧾 Add Sales - Create new sales record (blue icon)

### Interactive Features
- **Filter Buttons:** Filter sales by product category
- **Export Buttons:** Download data as CSV or JSON
- **Responsive Charts:** Auto-resize on window change
- **Form Auto-calculation:** Revenue and cost calculate automatically
- **Duplicate Prevention:** Case-insensitive product name validation

---

## 🎓 Educational Breakdown

### Database Models (models.py)

**Product Model:**
```python
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique, case-insensitive
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        # Auto-convert to Title Case
        self.name = self.name.title()
        super().save(*args, **kwargs)
```

**SalesData Model:**
```python
class SalesData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # SQL JOIN
    date = models.DateField()
    quantity = models.IntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        # Auto-calculate profit
        self.profit = self.revenue - self.cost
        super().save(*args, **kwargs)
```

**Lessons:**
- Foreign Keys (SQL relationships)
- Model validation
- Override save() method for custom logic
- DecimalField for precise financial data

---

### OOP Implementation (reports.py)

**Parent Class:**
```python
class GenericReport:
    """Base class for all reports"""
    def __init__(self, queryset):
        self.queryset = queryset
    
    def calculate_total(self):
        # Common method for all reports
        return self.queryset.aggregate(total=Sum('revenue'))['total']
```

**Child Class (Inheritance):**
```python
class MarketShareReport(GenericReport):
    """Inherits from GenericReport"""
    def __init__(self, queryset):
        super().__init__(queryset)  # Call parent constructor
    
    def get_market_shares(self):
        # Child-specific method
        # Uses self.queryset from parent
        return self.queryset.values('product__name').annotate(
            total=Sum('revenue')
        )
```

**Lessons:**
- Class inheritance (parent/child relationship)
- super() to call parent methods
- Method overriding
- Code reusability (DRY principle)

---

### NumPy Examples (views.py)

```python
import numpy as np

# Convert queryset to numpy array
revenues = np.array(list(sales.values_list('revenue', flat=True)))

# Statistical calculations
total_revenue = np.sum(revenues)        # Sum all values
avg_revenue = np.mean(revenues)         # Average
median_revenue = np.median(revenues)    # Middle value
std_dev = np.std(revenues)              # Standard deviation

# Histogram for distribution
hist, bins = np.histogram(revenues, bins=10)
```

**Lessons:**
- Convert Django QuerySet to NumPy array
- Aggregation functions
- Statistical analysis
- Data distribution

---

### Machine Learning (views.py)

**Linear Regression (Prediction):**
```python
from sklearn.linear_model import LinearRegression

# Prepare data
X = np.array(range(1, 13)).reshape(-1, 1)  # Months
y = monthly_values  # Sales values

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next month
next_month = np.array([[13]])
prediction = model.predict(next_month)[0]
```

**Classification (Evaluation):**
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Binary classification (High/Low sales)
y_true = [1, 0, 1, 1, 0]  # Actual
y_pred = [1, 0, 1, 0, 0]  # Predicted

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
```

**Lessons:**
- Difference between Regression (numbers) and Classification (categories)
- Model training with .fit()
- Predictions with .predict()
- Performance metrics

---

### Django Forms (forms.py)

**Form with Validation:**
```python
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'cost']
    
    def clean_name(self):
        # Custom validation for duplicate prevention
        name = self.cleaned_data.get('name')
        if Product.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(
                f"A product named '{name.title()}' already exists."
            )
        return name
```

**Lessons:**
- ModelForm for automatic form generation
- Custom validation with clean_<fieldname>()
- Case-insensitive queries with __iexact
- Form error handling

---

### SQL Operations (Django ORM)

**Basic Queries:**
```python
# SELECT all
Product.objects.all()

# SELECT with WHERE
Product.objects.filter(category='Electronics')

# SELECT with JOIN
SalesData.objects.select_related('product')
```

**Aggregation:**
```python
from django.db.models import Sum, Avg, Count

# GROUP BY product
SalesData.objects.values('product').annotate(
    total_sales=Sum('revenue'),
    avg_quantity=Avg('quantity'),
    num_transactions=Count('id')
)
```

**Lessons:**
- QuerySets (lazy evaluation)
- Filtering and chaining
- Aggregation functions
- JOIN operations with select_related()

---

### JSON Export (views.py)

```python
import json

def export_json(request):
    sales = SalesData.objects.select_related('product').all()
    
    data = []
    for sale in sales:
        data.append({
            'product': sale.product.name,
            'date': str(sale.date),
            'quantity': sale.quantity,
            'revenue': float(sale.revenue),
            'profit': float(sale.profit)
        })
    
    # Serialize to JSON
    json_data = json.dumps(data, indent=2)
    
    # Return as file download
    response = HttpResponse(json_data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="sales_data.json"'
    return response
```

**Lessons:**
- Dictionary creation from model instances
- json.dumps() for serialization
- HTTP response with file download
- Content-Type headers

---

## 🤝 Contributing

This is an educational project. Contributions welcome!

**How to Contribute:**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Submit a Pull Request

**Areas for Improvement:**
- Add more product categories
- Implement data filtering by date range
- Add PDF export functionality
- Create more ML models
- Add user roles and permissions
- Implement API endpoints

---

## 📝 License

This project is licensed under the MIT License.

**You are free to:**
- Use commercially
- Modify
- Distribute
- Sublicense

**Conditions:**
- Include original license
- State changes made

---

## 📧 Contact & Support

**Repository:** [https://github.com/ramonbonina320401-bot/Django-Sales-Dashboard-Report](https://github.com/ramonbonina320401-bot/Django-Sales-Dashboard-Report)

**Issues:** Report bugs or request features via GitHub Issues

**Questions:** Check Troubleshooting section first, then open an issue

---

## 🎯 Use Cases

**For Students:**
- Learn Python web development
- Understand NumPy and Matplotlib
- Practice SQL and database design
- Explore machine learning basics
- Study OOP principles

**For Teachers:**
- Teaching aid for Python classes
- Demonstrate real-world applications
- Show integration of multiple libraries
- Explain CRUD operations
- Illustrate best practices

**For Developers:**
- Django project template
- Reference for forms and validation
- Example of clean code structure
- Integration patterns for data science libraries

---

## 📊 Sample Data Details

**Generated by:** `python manage.py populate_sales`

**Products Created:**
1. **Laptop** - Electronics - ₱45,000 (Cost: ₱35,000)
2. **Mouse** - Accessories - ₱800 (Cost: ₱500)
3. **Keyboard** - Accessories - ₱1,500 (Cost: ₱1,000)
4. **Monitor** - Electronics - ₱12,000 (Cost: ₱9,000)
5. **Headset** - Accessories - ₱2,500 (Cost: ₱1,800)

**Sales Transactions:**
- Random dates over 365 days
- Quantities between 1-10 units
- Realistic revenue = quantity × price
- Automatic profit calculation

---

**⭐ If you find this project helpful, please star the repository!**

---

*Last Updated: December 11, 2025*  
*Version: 2.0*  
*Python 3.13 | Django 6.0 | NumPy 2.3.5*
