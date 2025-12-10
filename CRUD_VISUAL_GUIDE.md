# CRUD System - Visual Guide & Workflow Examples

## 📱 Navigation Map

```
Main Dashboard
    ├── Home Icon (/)
    │   └── Sales Report (Main Dashboard)
    │
    ├── Chart Icon (/market/)
    │   └── Market Share Analysis
    │
    ├── Database Icon (/data/)
    │   └── Raw Data View
    │
    ├── Sliders Icon (/eval/)
    │   └── Model Evaluation
    │
    ├── 📦 BOX ICON (NEW) (/products/)
    │   ├── View All Products
    │   ├── → Add New Product (/products/create/)
    │   ├── → Edit Product (/products/<id>/edit/)
    │   └── → Delete Product (/products/<id>/delete/)
    │
    └── 📋 RECEIPT ICON (NEW) (/sales/)
        ├── View All Sales
        ├── → Record New Sale (/sales/create/)
        ├── → Edit Sale (/sales/<id>/edit/)
        └── → Delete Sale (/sales/<id>/delete/)
```

---

## 🔄 Complete Workflow Example

### **Scenario: New Business Starting Fresh**

#### **Week 1: Setup Products**

```
Monday:
├── Visit http://localhost:8000/products/
├── Click "+ Add New Product"
├── Fill form:
│   ├── Name: "USB-C Cable"
│   ├── Category: "Electronics"
│   ├── Price: $19.99
│   ├── Cost: $5.00
│   └── Watch margin calculate: 74.9% ✓
├── Click "Create Product" ✓
└── See success message

Tuesday:
├── Click "+ Add New Product"
├── Fill form:
│   ├── Name: "HDMI Cable"
│   ├── Category: "Electronics"
│   ├── Price: $29.99
│   ├── Cost: $8.00
│   └── Watch margin calculate: 73.4% ✓
└── Click "Create Product" ✓

Wednesday:
├── Click "+ Add New Product"
├── Fill form:
│   ├── Name: "USB Hub"
│   ├── Category: "Electronics"
│   ├── Price: $49.99
│   ├── Cost: $20.00
│   └── Watch margin calculate: 60.0% ✓
└── Click "Create Product" ✓

Now /products/ shows:
┌─────────────────────────────────────────┐
│ Total Products: 3                       │
│ Categories: 1                           │
│ Avg Profit Margin: 69.4%               │
│ Total Sales: 0 (No sales yet)          │
└─────────────────────────────────────────┘

Product Table:
┌────────────┬───────────┬────────┬────────┬────────┐
│ Name       │ Category  │ Price  │ Cost   │ Margin │
├────────────┼───────────┼────────┼────────┼────────┤
│ HDMI Cable │ Electron. │ $29.99 │ $8.00  │ 73.4%  │
│ USB Hub    │ Electron. │ $49.99 │ $20.00 │ 60.0%  │
│ USB-C Cable│ Electron. │ $19.99 │ $5.00  │ 74.9%  │
└────────────┴───────────┴────────┴────────┴────────┘
```

#### **Week 2: Record Sales**

```
Monday (Oct 1st):
├── Visit http://localhost:8000/sales/
├── Click "+ Record New Sale"
├── Fill form:
│   ├── Product: "USB-C Cable"
│   ├── Date: 2025-10-01
│   ├── Quantity: 50
│   │
│   └── Watch auto-calculations:
│       ├── Revenue: $999.50 (50 × $19.99)
│       ├── Cost: $250.00 (50 × $5.00)
│       ├── Profit: $749.50 ✓
│       └── Margin: 74.9% ✓
├── Click "Record Sale" ✓
└── See success: "Sale recorded: 50 units of USB-C Cable for $749.50 profit!"

Monday (Oct 1st) - Second Sale:
├── Click "+ Record New Sale"
├── Fill form:
│   ├── Product: "HDMI Cable"
│   ├── Date: 2025-10-01
│   ├── Quantity: 25
│   │
│   └── Watch auto-calculations:
│       ├── Revenue: $749.75
│       ├── Cost: $200.00
│       ├── Profit: $549.75 ✓
│       └── Margin: 73.4% ✓
└── Click "Record Sale" ✓

Wednesday (Oct 3rd):
├── Click "+ Record New Sale"
├── Fill form:
│   ├── Product: "USB Hub"
│   ├── Date: 2025-10-03
│   ├── Quantity: 10
│   │
│   └── Watch auto-calculations:
│       ├── Revenue: $499.90
│       ├── Cost: $200.00
│       ├── Profit: $299.90 ✓
│       └── Margin: 60.0% ✓
└── Click "Record Sale" ✓

Friday (Oct 10th):
├── Click "+ Record New Sale"
├── Fill form:
│   ├── Product: "USB-C Cable"
│   ├── Date: 2025-10-10
│   ├── Quantity: 75
│   └── Profit: $1,499.25
└── Click "Record Sale" ✓

Now /sales/ shows:
┌─────────────────────────────────────┐
│ Summary:                            │
│ Total Sales Records: 4              │
│ Total Revenue: $3,248.15            │
│ Total Profit: $3,098.40             │
│ Avg Profit Margin: 73.8%            │
└─────────────────────────────────────┘

Sales Table (sorted by date):
┌────────────┬────────────┬──────┬──────────┬──────────┐
│ Date       │ Product    │ Qty  │ Revenue  │ Profit   │
├────────────┼────────────┼──────┼──────────┼──────────┤
│ Oct 01     │ USB-C Cable│  50  │ $999.50  │ $749.50  │
│ Oct 01     │ HDMI Cable │  25  │ $749.75  │ $549.75  │
│ Oct 03     │ USB Hub    │  10  │ $499.90  │ $299.90  │
│ Oct 10     │ USB-C Cable│  75  │$1,499.25 │$1,499.25 │
└────────────┴────────────┴──────┴──────────┴──────────┘
```

#### **Week 3: Review & Adjust**

```
Friday (Reviewing data):
├── Go to /sales/
├── Filter by date: Oct 1 to Oct 10
├── See Summary:
│   ├── Total Revenue: $3,248.15
│   ├── Total Profit: $3,098.40
│   ├── Best Margin: USB-C Cable (74.9%)
│   └── Quantity Sold: 160 units
│
├── Realize HDMI is less profitable (73.4% vs 74.9%)
├── Go to /products/
├── Click Edit on "HDMI Cable"
├── See options to adjust price
│   ├── Current: Price $29.99, Cost $8.00, Margin 73.4%
│   ├── Option 1: Keep as is (profitable)
│   └── Option 2: Increase price to improve margin
│
└── Decide to keep price (good margin already)

Monday (Next week):
├── Continue recording sales
├── Use /sales/ to track daily revenue
├── Use filters to analyze by product/date range
└── Data automatically included in main dashboard reports
```

---

## 📊 Feature Demonstrations

### **1. Product Management - Creating**

```
Step 1: Click "+ Add New Product"
┌─────────────────────────────────────┐
│        ADD NEW PRODUCT              │
│ ═════════════════════════════════════ │
│                                     │
│ Product Name *                      │
│ ┌─────────────────────────────────┐ │
│ │ Enter product name...           │ │
│ └─────────────────────────────────┘ │
│                                     │
│ Category *                          │
│ ┌─────────────────────────────────┐ │
│ │ Electronics                     │ │
│ └─────────────────────────────────┘ │
│                                     │
│ Unit Price ($) *  │  Unit Cost ($)*│
│ ┌─────────────────┐ ┌─────────────┐ │
│ │ 1000.00         │ │ 700.00      │ │
│ └─────────────────┘ └─────────────┘ │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ Profit per Unit: $300.00        │ │
│ │ Profit Margin: 30.0% (GREEN)    │ │
│ └─────────────────────────────────┘ │
│                                     │
│     [✓ Create Product] [✗ Cancel]  │
└─────────────────────────────────────┘

Step 2: Form fills with values
        ↓
        Real-time calculation updates
        ↓
Step 3: Click "Create Product"
        ↓
Success: "Product 'Laptop Pro' created successfully!"
        ↓
Redirects to /products/
        ↓
Product appears in table with margin color-coded
```

### **2. Sales Management - Recording Past Sales**

```
Step 1: Click "+ Record New Sale"
┌─────────────────────────────────────┐
│      RECORD NEW SALE                │
│ ═════════════════════════════════════ │
│                                     │
│ Product *                           │
│ ┌─────────────────────────────────┐ │
│ │ Select... ▼                     │ │
│ └─────────────────────────────────┘ │
│                                     │
│ Sale Date *                         │
│ ┌─────────────────────────────────┐ │
│ │ [Calendar Icon] 2025-10-15      │ │
│ │ (Can be past dates!)            │ │
│ └─────────────────────────────────┘ │
│                                     │
│ Quantity Sold *                     │
│ ┌─────────────────────────────────┐ │
│ │ 5 units                         │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘

Step 2: Select Product "Laptop Pro"
        ↓
Product info appears:
┌─────────────────────────────────────┐
│ Unit Price: $1000  Unit Cost: $700  │
│ Profit per Unit: $300  Margin: 30%  │
└─────────────────────────────────────┘

Step 3: Enter Quantity "5"
        ↓
Auto-calculations update:
┌─────────────────────────────────────┐
│ Total Revenue: $5,000               │
│   (5 × $1000)                       │
│ Total Cost: $3,500                  │
│   (5 × $700)                        │
│ Total Profit: $1,500 ✓              │
│   (Revenue - Cost)                  │
│ Profit Margin: 30.0% ✓              │
└─────────────────────────────────────┘

Step 4: Click "Record Sale"
        ↓
Success: "Sale recorded: 5 units of Laptop Pro 
          for $1,500.00 profit!"
        ↓
Sale appears in /sales/ table
```

### **3. Sales Management - Filtering**

```
/sales/ page shows:
┌─────────────────────────────────────────────┐
│          SALES MANAGEMENT                   │
├─────────────────────────────────────────────┤
│
│ FILTERS:
│ ┌──────────────────────────────────────────┐
│ │ Search: [USB]      Category: [All]       │
│ │ From: [2025-10-01]  To: [2025-10-31]    │
│ │ Min Profit: [500]                        │
│ │    [Filter] [Clear]                      │
│ └──────────────────────────────────────────┘
│
│ SUMMARY:
│ Total Revenue: $2,500  Total Profit: $1,500  Margin: 60%
│
│ RESULTS (Filtered to Oct 2025, USB products, Profit ≥ $500):
│ ┌────────────┬──────────┬─────┬──────────┬────────┐
│ │ Date       │ Product  │ Qty │ Revenue  │ Profit │
│ ├────────────┼──────────┼─────┼──────────┼────────┤
│ │ Oct 01     │ USB-C    │ 50  │ $999.50  │ $749.50│
│ │ Oct 10     │ USB-C    │ 75  │$1,499.25 │$1,499.2│
│ │ Oct 15     │ USB Hub  │ 10  │ $499.90  │ $299.90│
│ └────────────┴──────────┴─────┴──────────┴────────┘
│
└─────────────────────────────────────────────┘
```

### **4. Editing - See Live Impact**

```
User edits sale quantity from 5 to 10:

BEFORE:
┌─────────────────────────┐
│ Total Profit: $1,500    │
│ Quantity: 5 units       │
└─────────────────────────┘

User changes to: 10 units
        ↓
REAL-TIME UPDATE:
┌─────────────────────────┐
│ Total Profit: $3,000    │ ← Changed!
│ Quantity: 10 units      │
└─────────────────────────┘

User sees feedback:
"Profit change: +$1,500.00"

Click Save → Success message
```

---

## 🎨 Color Coding System

### **Profit Margin Colors**

```
30% or higher     = GREEN   ✓ Excellent
┌─────────────────┐
│ Margin: 35.0%   │  (Product or Sale is very profitable)
└─────────────────┘

15% to 30%       = YELLOW  ⚠ Good  
┌─────────────────┐
│ Margin: 22.5%   │  (Product or Sale is reasonably profitable)
└─────────────────┘

Below 15%        = RED     ✗ Low
┌─────────────────┐
│ Margin: 8.0%    │  (Product or Sale has thin margin)
└─────────────────┘
```

---

## 📈 Data Flow Diagrams

### **Creating a Sale**

```
User Form Input
    │
    ├─ Product: USB Cable
    ├─ Date: 2025-10-15
    └─ Quantity: 50

         ↓

Backend Processing (Django)
    │
    ├─ Get Product details
    │   ├─ Price: $19.99
    │   └─ Cost: $5.00
    │
    ├─ Auto-Calculate
    │   ├─ Revenue = 50 × $19.99 = $999.50
    │   ├─ Cost = 50 × $5.00 = $250.00
    │   └─ Profit = $999.50 - $250.00 = $749.50
    │
    └─ Save to Database

         ↓

Database Entry Created
    │
    └─ SalesData(
        product_id=1,
        date=2025-10-15,
        quantity=50,
        revenue=999.50,
        cost=250.00,
        profit=749.50
       )

         ↓

Success Message
    │
    └─ "Sale recorded: 50 units of USB Cable for $749.50 profit!"
```

### **Viewing Sales with Filters**

```
User Goes to /sales/
         ↓
Backend Query
    │
    ├─ GET parameter: start_date=2025-10-01
    ├─ GET parameter: end_date=2025-10-31
    ├─ GET parameter: category=Electronics
    └─ GET parameter: min_profit=500

         ↓

Database Filter
    │
    └─ SalesData.objects.filter(
        date__gte='2025-10-01',
        date__lte='2025-10-31',
        product__category='Electronics',
        profit__gte=500
       )

         ↓

Aggregate Calculations
    │
    ├─ sum(revenue) = $3,248.15
    ├─ sum(profit) = $2,098.40
    └─ avg(profit/revenue*100) = 64.6%

         ↓

Render Template with Data
    │
    └─ Table with all matching sales
       Summary cards with totals
       Color-coded margin indicators
```

---

## ✅ Quick Reference Guide

### **Product URLs**
| Action | URL | HTTP | Purpose |
|--------|-----|------|---------|
| List | `/products/` | GET | View all products |
| Create | `/products/create/` | GET/POST | Add new product |
| Edit | `/products/<id>/edit/` | GET/POST | Update product |
| Delete | `/products/<id>/delete/` | GET/POST | Remove product |

### **Sales URLs**
| Action | URL | HTTP | Purpose |
|--------|-----|------|---------|
| List | `/sales/` | GET | View all sales |
| Create | `/sales/create/` | GET/POST | Record new sale |
| Edit | `/sales/<id>/edit/` | GET/POST | Update sale |
| Delete | `/sales/<id>/delete/` | GET/POST | Remove sale |

### **API Endpoints**
| Action | URL | HTTP | Returns |
|--------|-----|------|---------|
| Get Product | `/api/product/<id>/` | GET | JSON with price/cost |

---

## 🎯 Common Tasks

### **Task: Add product with historical sales**
```
1. /products/create/
   ├─ Name: "Headphones"
   ├─ Category: "Audio"
   ├─ Price: $79.99
   ├─ Cost: $35.00
   └─ Margin: 56.2%

2. /sales/create/ (Multiple times)
   ├─ Product: "Headphones"
   ├─ Date: 2025-09-01 (Past date)
   ├─ Quantity: 20
   │  └─ Profit: $899.80

3. /sales/create/
   ├─ Product: "Headphones"
   ├─ Date: 2025-09-15
   ├─ Quantity: 30
   │  └─ Profit: $1,349.70

4. /sales/
   ├─ Filter by Date: Sep 2025
   ├─ See both sales combined
   └─ Total Profit: $2,249.50
```

### **Task: Adjust product price for better margin**
```
1. /products/
2. Click Edit on product
3. Change Price from $79.99 to $99.99
4. Watch margin change: 56.2% → 64.8% ✓
5. Save
6. Note: Affects future sales, not past
```

### **Task: Review profitability by date**
```
1. /sales/
2. Filter by Date Range: Oct 1 - Oct 31
3. See:
   ├─ Total Revenue in Oct
   ├─ Total Profit in Oct
   ├─ Which products sold most
   └─ Which had best margins
4. Compare to different month
5. Identify trends
```

---

## 💡 Pro Tips

**✓ For Historical Data:**
- Start with oldest date and work forward
- Use date picker for accuracy
- Review summary stats after adding

**✓ For Accuracy:**
- Double-check product prices before recording sales
- Can edit sales if quantity was wrong
- Price changes only affect future sales

**✓ For Analysis:**
- Filter by date range to see seasonal trends
- Filter by minimum profit to find unprofitable items
- Use product edit page to see recent sales history
- Compare profit margins between products

**✓ For Management:**
- Regular review of low-margin products
- Track which products generate most revenue
- Monitor if costs are increasing
- Adjust prices if needed (for future sales)

---

This visual guide should help you understand the complete CRUD system workflow!
For detailed instructions, see: `CRUD_QUICK_START.md`
