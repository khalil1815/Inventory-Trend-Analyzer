import pandas as pd
from datetime import datetime

class TrendAnalyzer:
    """
    Processes inventory logs to identify stockout risks.
    Demonstrates data cleansing and analytical logic.
    """
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def analyze_stock(self, threshold=10):
        # Data Cleansing: Ensure numerical types
        self.df['stock_level'] = pd.to_numeric(self.df['stock_level'])
        
        # Identify low stock items
        at_risk = self.df[self.df['stock_level'] < threshold]
        return at_risk

# --- Demonstration ---
if __name__ == "__main__":
    # Simulated "messy" inventory data
    inventory_data = {
        'product': ['Engine Oil', 'Tires', 'Brake Pads', 'Filters', 'Coolant'],
        'stock_level': [45, 8, 12, "5", 50],  # Note the string "5" to test cleaning
        'last_restock': ['2026-05-01', '2026-05-15', '2026-05-20', '2026-05-22', '2026-06-01']
    }
    
    analyzer = TrendAnalyzer(inventory_data)
    risky_items = analyzer.analyze_stock(threshold=10)
    
    print("--- Inventory Analysis Report ---")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d')}")
    print("\nProducts requiring immediate reorder:")
    print(risky_items[['product', 'stock_level']])
