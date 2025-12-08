"""
Object-Oriented Programming: Report Classes with Inheritance

This module demonstrates OOP concepts:
- Inheritance: Child classes extend GenericReport parent class
- Encapsulation: Data and methods bundled in classes
- Code Reusability: Common functionality in parent class
"""

import numpy as np
from datetime import datetime
from .models import SalesData, Product


class GenericReport:
    """
    Parent Class: Generic Report Template
    
    Provides common functionality for all report types.
    Demonstrates OOP Inheritance and Reusability.
    """
    
    def __init__(self, title):
        self.title = title
        self.generated_at = datetime.now()
        self.data = None
    
    def get_title(self):
        """Return formatted report title"""
        return f"Report: {self.title}"
    
    def get_timestamp(self):
        """Return formatted generation timestamp"""
        return self.generated_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def fetch_data(self):
        """Abstract method - to be overridden by child classes"""
        raise NotImplementedError("Subclasses must implement fetch_data()")
    
    def process_data(self):
        """Abstract method - to be overridden by child classes"""
        raise NotImplementedError("Subclasses must implement process_data()")


class SalesReport(GenericReport):
    """
    Child Class: Sales Report
    
    Inherits from GenericReport and adds specific sales analysis.
    Uses NumPy for statistical calculations.
    """
    
    def __init__(self):
        super().__init__("Sales Analysis Report")
        self.statistics = {}
    
    def fetch_data(self):
        """Fetch sales data from database"""
        self.data = SalesData.objects.all()
        return self.data
    
    def process_data(self):
        """Process sales data using NumPy"""
        if not self.data:
            self.fetch_data()
        
        revenues = np.array([float(s.revenue) for s in self.data])
        
        self.statistics = {
            'total': np.sum(revenues),
            'mean': np.mean(revenues),
            'median': np.median(revenues),
            'std': np.std(revenues),
            'count': len(revenues)
        }
        
        return self.statistics
    
    def get_summary(self):
        """Return formatted summary of sales statistics"""
        if not self.statistics:
            self.process_data()
        
        return {
            'title': self.get_title(),
            'timestamp': self.get_timestamp(),
            'total_revenue': f"₱{self.statistics['total']:,.2f}",
            'mean_revenue': f"₱{self.statistics['mean']:,.2f}",
            'median_revenue': f"₱{self.statistics['median']:,.2f}",
            'std_deviation': f"₱{self.statistics['std']:,.2f}",
            'record_count': f"{self.statistics['count']:,}",
        }


class MarketShareReport(GenericReport):
    """
    Child Class: Market Share Report
    
    Inherits from GenericReport and adds market analysis.
    Uses Django ORM for data aggregation.
    """
    
    def __init__(self):
        super().__init__("Market Share Analysis Report")
        self.market_data = {}
    
    def fetch_data(self):
        """Fetch product sales data"""
        from django.db.models import Sum
        self.data = Product.objects.annotate(
            total_sales=Sum('sales__revenue')
        ).order_by('-total_sales')
        return self.data
    
    def process_data(self):
        """Calculate market share percentages"""
        if not self.data:
            self.fetch_data()
        
        total_revenue = sum([float(p.total_sales or 0) for p in self.data])
        
        self.market_data = []
        for product in self.data:
            sales = float(product.total_sales or 0)
            percentage = (sales / total_revenue * 100) if total_revenue > 0 else 0
            
            self.market_data.append({
                'product': product.name,
                'category': product.category,
                'sales': sales,
                'percentage': percentage
            })
        
        return self.market_data
    
    def get_summary(self):
        """Return formatted market share summary"""
        if not self.market_data:
            self.process_data()
        
        return {
            'title': self.get_title(),
            'timestamp': self.get_timestamp(),
            'top_product': self.market_data[0] if self.market_data else None,
            'products': self.market_data,
        }


class PredictionReport(GenericReport):
    """
    Child Class: Prediction Report
    
    Inherits from GenericReport and adds ML predictions.
    Uses scikit-learn for Linear Regression (Numerical Prediction).
    """
    
    def __init__(self):
        super().__init__("Sales Prediction Report (Linear Regression)")
        self.predictions = {}
    
    def fetch_data(self):
        """Fetch historical sales data for prediction"""
        from django.db.models import Sum
        from django.db.models.functions import TruncMonth
        from datetime import datetime, timedelta
        
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=365)
        
        # Get monthly aggregated data
        self.data = SalesData.objects.filter(
            date__gte=start_date,
            date__lte=end_date
        ).annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total=Sum('revenue')
        ).order_by('month')
        
        return self.data
    
    def process_data(self):
        """Apply Linear Regression for future prediction"""
        from sklearn.linear_model import LinearRegression
        
        if not self.data:
            self.fetch_data()
        
        if len(self.data) < 2:
            return None
        
        # Prepare data for regression
        X = np.array(range(len(self.data))).reshape(-1, 1)
        y = np.array([float(d['total']) for d in self.data])
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict next 3 months
        future_X = np.array([len(self.data), len(self.data)+1, len(self.data)+2]).reshape(-1, 1)
        future_predictions = model.predict(future_X)
        
        self.predictions = {
            'next_month': float(future_predictions[0]),
            'second_month': float(future_predictions[1]),
            'third_month': float(future_predictions[2]),
            'slope': float(model.coef_[0]),
            'intercept': float(model.intercept_),
            'model_type': 'Linear Regression (Continuous Prediction)'
        }
        
        return self.predictions
    
    def get_summary(self):
        """Return formatted prediction summary"""
        if not self.predictions:
            self.process_data()
        
        if not self.predictions:
            return None
        
        return {
            'title': self.get_title(),
            'timestamp': self.get_timestamp(),
            'next_month_prediction': f"₱{self.predictions['next_month']:,.2f}",
            'second_month_prediction': f"₱{self.predictions['second_month']:,.2f}",
            'third_month_prediction': f"₱{self.predictions['third_month']:,.2f}",
            'trend_slope': f"₱{self.predictions['slope']:,.2f} per month",
            'model_info': self.predictions['model_type']
        }
