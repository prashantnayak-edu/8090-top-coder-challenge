import json

with open('public_cases.json', 'r') as f:
    data = json.load(f)

print("=== ANALYZING 1000 PUBLIC CASES FOR PATTERNS ===")
print()

# High-intensity cases (>500 miles/day)
print("🚗 HIGH-INTENSITY CASES (>500 miles/day):")
high_intensity = []
for i, case in enumerate(data):
    days = case['input']['trip_duration_days']
    miles = case['input']['miles_traveled'] 
    receipts = case['input']['total_receipts_amount']
    expected = case['expected_output']
    miles_per_day = miles / days
    if miles_per_day > 500:
        high_intensity.append((i, days, miles, receipts, expected, miles_per_day))

print(f"Found {len(high_intensity)} high-intensity cases")
for case in high_intensity[:8]:
    i, days, miles, receipts, expected, mpd = case
    rate = expected / miles if miles > 0 else 0
    print(f"Case {i:3d}: {days}d, {miles:4d}mi, ${receipts:6.0f} → ${expected:7.2f} ({mpd:3.0f} mi/day, ${rate:.2f}/mi)")

print()

# Low-mileage, high-receipt cases
print("💰 LOW-MILEAGE, HIGH-RECEIPT CASES:")
low_mile_high_receipt = []
for i, case in enumerate(data):
    days = case['input']['trip_duration_days']
    miles = case['input']['miles_traveled'] 
    receipts = case['input']['total_receipts_amount']
    expected = case['expected_output']
    miles_per_day = miles / days
    receipt_to_mile = receipts / miles if miles > 0 else 0
    if miles_per_day < 100 and receipt_to_mile > 5 and receipts > 500:
        low_mile_high_receipt.append((i, days, miles, receipts, expected, miles_per_day, receipt_to_mile))

print(f"Found {len(low_mile_high_receipt)} low-mileage, high-receipt cases")
for case in low_mile_high_receipt[:8]:
    i, days, miles, receipts, expected, mpd, rtm = case
    print(f"Case {i:3d}: {days}d, {miles:3d}mi, ${receipts:6.0f} → ${expected:7.2f} ({int(mpd):2d} mi/day, ${rtm:.1f} $/mi)")

print()

# Normal cases for comparison
print("📊 NORMAL CASES (100-300 mi/day, 1-5 $/mi):")
normal = []
for i, case in enumerate(data):
    days = case['input']['trip_duration_days']
    miles = case['input']['miles_traveled'] 
    receipts = case['input']['total_receipts_amount']
    expected = case['expected_output']
    miles_per_day = miles / days
    receipt_to_mile = receipts / miles if miles > 0 else 0
    if 100 <= miles_per_day <= 300 and 1 <= receipt_to_mile <= 5:
        normal.append((i, days, miles, receipts, expected, miles_per_day, receipt_to_mile))

print(f"Found {len(normal)} normal cases")
for case in normal[:8]:
    i, days, miles, receipts, expected, mpd, rtm = case
    rate = expected / miles if miles > 0 else 0
    print(f"Case {i:3d}: {days}d, {miles:3d}mi, ${receipts:6.0f} → ${expected:7.2f} ({int(mpd):3d} mi/day, ${rate:.2f}/mi)") 