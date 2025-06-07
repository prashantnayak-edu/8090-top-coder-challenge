import pandas as pd
import numpy as np

def engineer_features(df):
    # Prevent divide by zero and add small epsilon
    df = df.copy()
    
    # Safe division with minimum of 0.1 to prevent divide by zero
    df['miles_per_day'] = df['miles_traveled'] / np.maximum(df['trip_duration_days'], 0.1)
    df['receipts_per_day'] = df['total_receipts_amount'] / np.maximum(df['trip_duration_days'], 0.1)
    
    # Log transformations for high values (expert recommendation)
    df['log_miles_per_day'] = np.log1p(df['miles_per_day'])
    df['log_receipts_per_day'] = np.log1p(df['receipts_per_day'])
    
    # Continuous efficiency score instead of binary (expert recommendation)
    # Peaks at 200 miles/day, tapers off gradually
    df['efficiency_score'] = np.exp(-((df['miles_per_day'] - 200)**2) / (2 * 50**2))
    
    # 5-day trip bonus (Lisa's observation)
    df['sweet_spot_5day'] = (df['trip_duration_days'] == 5).astype(int)
    
    # Continuous penalty scores instead of binary
    df['low_receipt_score'] = np.where(df['total_receipts_amount'] < 50, 
                                     1 - (df['total_receipts_amount'] / 50), 0)
    
    # High spending penalty - continuous scale
    df['high_spending_penalty'] = np.maximum(0, (df['receipts_per_day'] - 150) / 100)
    
    # Remove restrictive caps - use higher caps (expert recommendation)
    df['miles_per_day_soft_cap'] = np.minimum(df['miles_per_day'], 1000)  # Much higher cap
    df['receipts_per_day_soft_cap'] = np.minimum(df['receipts_per_day'], 1000)  # Much higher cap
    
    # remove problematic polynomial features
    # Removed: miles_per_day_squared, receipts_per_day_squared (causing instability)
    
    # Enhanced interaction features between mileage and receipts (expert recommendation)
    # Basic interaction terms
    df['miles_receipts_interaction'] = df['miles_per_day'] * df['receipts_per_day']
    df['receipts_to_miles_ratio'] = df['total_receipts_amount'] / np.maximum(df['miles_traveled'], 0.1)
    df['sqrt_miles'] = np.sqrt(df['miles_traveled'])
    df['sqrt_receipts'] = np.sqrt(df['total_receipts_amount'])
    
    # Advanced interaction features for edge case detection
    
    # 1. Mileage-Receipt Balance Score (balanced vs imbalanced patterns)
    expected_receipts_per_mile = 1.5  # Reasonable expectation
    df['mileage_receipt_balance'] = np.abs(df['receipts_to_miles_ratio'] - expected_receipts_per_mile) / expected_receipts_per_mile
    
    # 2. Intensity-Spending Correlation (high miles should have moderate receipts)
    df['intensity_spending_score'] = df['miles_per_day'] * np.log1p(df['receipts_per_day'])
    
    # 3. Efficiency-Cost Ratio (miles achieved per dollar spent)
    df['efficiency_cost_ratio'] = df['miles_traveled'] / np.maximum(df['total_receipts_amount'], 1)
    
    # 4. Trip Pattern Classification Features
    # High-intensity, low-receipt pattern (legitimate high-mileage business trips)
    df['high_miles_low_receipt'] = np.where(
        (df['miles_per_day'] > 400) & (df['receipts_to_miles_ratio'] < 2),
        df['miles_per_day'] / 100, 0
    )
    
    # Low-intensity, high-receipt pattern (potential fraud or unusual expense patterns)
    df['low_miles_high_receipt'] = np.where(
        (df['miles_per_day'] < 100) & (df['receipts_to_miles_ratio'] > 5),
        df['receipts_to_miles_ratio'] / 10, 0
    )
    
    # 5. Proportional Spending Score (receipts proportional to trip characteristics)
    df['proportional_spending'] = (df['receipts_per_day'] * df['trip_duration_days']) / np.maximum(df['miles_traveled'], 1)
    
    # 6. Extreme Pattern Detection (for outlier cases like Case 996)
    df['extreme_receipt_pattern'] = np.where(
        (df['receipts_to_miles_ratio'] > 3) & (df['miles_per_day'] > 500),
        df['receipts_to_miles_ratio'] * df['miles_per_day'] / 1000, 0
    )
    
    # 7. Duration-Adjusted Interaction (how mileage/receipts scale with trip length)
    df['duration_miles_interaction'] = df['trip_duration_days'] * df['miles_per_day'] / 100
    df['duration_receipts_interaction'] = df['trip_duration_days'] * df['receipts_per_day'] / 100
    
    # 8. Cross-Ratio Features (capture non-linear relationships)
    df['miles_squared_per_receipt'] = (df['miles_per_day'] ** 2) / np.maximum(df['receipts_per_day'], 1)
    df['receipts_squared_per_mile'] = (df['receipts_per_day'] ** 2) / np.maximum(df['miles_per_day'], 1)
    
    # Keep useful derived features
    df['trip_intensity'] = df['miles_traveled'] * df['total_receipts_amount'] / df['trip_duration_days']
    df['high_miles_efficiency'] = df['miles_per_day_soft_cap']
    df['total_trip_score'] = df['miles_traveled'] * df['trip_duration_days']
    df['spending_category'] = pd.cut(df['receipts_per_day_soft_cap'], 
                                   bins=[0, 75, 120, float('inf')], 
                                   labels=[0, 1, 2]).astype(int)
    
    # Long trip receipt penalty to fix 30-40% over-reimbursement
    df['long_trip_receipt_penalty'] = np.where(df['trip_duration_days'] > 7, 
                                               df['receipts_per_day'] / 1000, 0)
    
    # Additional targeted features for remaining problem cases
    # Extreme case indicators to help with Case 940 type issues
    df['extreme_mileage_flag'] = (df['miles_per_day'] > 1000).astype(int)
    df['extreme_intensity'] = np.where(df['miles_per_day'] > 500, 
                                       (df['miles_per_day'] - 500) / 1000, 0)
    
    # High spend + low miles pattern (problematic combination)
    df['high_spend_low_miles'] = np.where(
        (df['receipts_per_day'] > 200) & (df['miles_per_day'] < 100),
        df['receipts_per_day'] / 100, 0
    )
    
    return df