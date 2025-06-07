#!/bin/bash

echo "🧾 Quick Test Suite - Key Cases"
echo "==============================="
echo ""

# Normal cases
echo "📊 Normal Cases:"
echo "----------------"
printf "%-30s %-12s %-12s %-12s\n" "Case Description" "Got" "Expected" "Error %"

# Normal case 1: 3 days, 150 miles, $100
got1=$(./run.sh 3 150 100)
expected1="369.00"  # Estimate based on baseline
error1=$(echo "scale=1; (($got1 - $expected1) / $expected1) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "3 days, 150 miles, \$100" "$got1" "$expected1" "${error1}%"

# Normal case 2: 1 day, 50 miles, $10  
got2=$(./run.sh 1 50 10)
expected2="149.00"  # Estimate based on baseline
error2=$(echo "scale=1; (($got2 - $expected2) / $expected2) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "1 day, 50 miles, \$10" "$got2" "$expected2" "${error2}%"

echo ""
echo "🔥 High-Intensity Cases (Rules):"
echo "--------------------------------"
printf "%-30s %-12s %-12s %-12s\n" "Case Description" "Got" "Expected" "Error %"

# High-intensity case 1: 2 days, 1189 miles, $1164
gothi1=$(./run.sh 2 1189 1164.74)
expectedhi1="1666.52"
errorhi1=$(echo "scale=1; (($gothi1 - $expectedhi1) / $expectedhi1) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "2 days, 1189 miles, \$1164" "$gothi1" "$expectedhi1" "${errorhi1}%"

# High-intensity case 2: 1 day, 809 miles, $1734
gothi2=$(./run.sh 1 809 1734.56)
expectedhi2="1447.25"
errorhi2=$(echo "scale=1; (($gothi2 - $expectedhi2) / $expectedhi2) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "1 day, 809 miles, \$1734" "$gothi2" "$expectedhi2" "${errorhi2}%"

echo ""
echo "💰 High-Receipt Cases (ML):"
echo "---------------------------"
printf "%-30s %-12s %-12s %-12s\n" "Case Description" "Got" "Expected" "Error %"

# High-receipt case 1: 4 days, 69 miles, $2321
gothr1=$(./run.sh 4 69 2321.49)
expectedhr1="322.00"
errorhr1=$(echo "scale=1; (($gothr1 - $expectedhr1) / $expectedhr1) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "4 days, 69 miles, \$2321" "$gothr1" "$expectedhr1" "${errorhr1}%"

# High-receipt case 2: 5 days, 516 miles, $1878
gothr2=$(./run.sh 5 516 1878.49)
expectedhr2="669.85"
errorhr2=$(echo "scale=1; (($gothr2 - $expectedhr2) / $expectedhr2) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "5 days, 516 miles, \$1878" "$gothr2" "$expectedhr2" "${errorhr2}%"

# High-receipt case 3: 8 days, 792 miles, $2437
gothr3=$(./run.sh 8 792 2437.24)
expectedhr3="1556.70"
errorhr3=$(echo "scale=1; (($gothr3 - $expectedhr3) / $expectedhr3) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "8 days, 792 miles, \$2437" "$gothr3" "$expectedhr3" "${errorhr3}%"

echo ""
echo "🚨 Problem Cases from Eval:"
echo "---------------------------"
printf "%-30s %-12s %-12s %-12s\n" "Case Description" "Got" "Expected" "Error %"

# Problem Case 996: 1 day, 1082 miles, $1809
got996=$(./run.sh 1 1082 1809.49)
expected996="446.94"
error996=$(echo "scale=1; (($got996 - $expected996) / $expected996) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "1 day, 1082 miles, \$1809" "$got996" "$expected996" "${error996}%"

# Problem Case 536: 5 days, 233 miles, $1862
got536=$(./run.sh 5 233 1862.04)
expected536="1562.23"
error536=$(echo "scale=1; (($got536 - $expected536) / $expected536) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "5 days, 233 miles, \$1862" "$got536" "$expected536" "${error536}%"

# Problem Case 527: 3 days, 133 miles, $1728
got527=$(./run.sh 3 133 1728.5)
expected527="1373.40"
error527=$(echo "scale=1; (($got527 - $expected527) / $expected527) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "3 days, 133 miles, \$1728" "$got527" "$expected527" "${error527}%"

# Problem Case 464: 7 days, 336 miles, $1843
got464=$(./run.sh 7 336 1843.58)
expected464="1691.68"
error464=$(echo "scale=1; (($got464 - $expected464) / $expected464) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "7 days, 336 miles, \$1843" "$got464" "$expected464" "${error464}%"

# Problem Case 869: 4 days, 198 miles, $2106
got869=$(./run.sh 4 198 2106.63)
expected869="1450.67"
error869=$(echo "scale=1; (($got869 - $expected869) / $expected869) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "4 days, 198 miles, \$2106" "$got869" "$expected869" "${error869}%"

echo ""
echo "🚨 High-Error Cases from Latest Eval:"
echo "------------------------------------------"
printf "%-30s %-12s %-12s %-12s\n" "Case Description" "Got" "Expected" "Error %"

# High-Error Case 152: 4 days, 69 miles, $2321.49 (Note: Also in High-Receipt section above)
got152=$(./run.sh 4 69 2321.49)
expected152="322.00"
error152=$(echo "scale=1; (($got152 - $expected152) / $expected152) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "4 days, 69 miles, \$2321" "$got152" "$expected152" "${error152}%"

# High-Error Case 352: 1 day, 43 miles, $2149.22
got352=$(./run.sh 1 43 2149.22)
expected352="1134.47"
error352=$(echo "scale=1; (($got352 - $expected352) / $expected352) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "1 day, 43 miles, \$2149" "$got352" "$expected352" "${error352}%"

# High-Error Case 166: 2 days, 165 miles, $1813.32
got166=$(./run.sh 2 165 1813.32)
expected166="1273.45"
error166=$(echo "scale=1; (($got166 - $expected166) / $expected166) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "2 days, 165 miles, \$1813" "$got166" "$expected166" "${error166}%"

# High-Error Case 286: 3 days, 266 miles, $2178.16
got286=$(./run.sh 3 266 2178.16)
expected286="1447.95"
error286=$(echo "scale=1; (($got286 - $expected286) / $expected286) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "3 days, 266 miles, \$2178" "$got286" "$expected286" "${error286}%"

# High-Error Case 638: 1 day, 170 miles, $2452.85
got638=$(./run.sh 1 170 2452.85)
expected638="1209.08"
error638=$(echo "scale=1; (($got638 - $expected638) / $expected638) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "1 day, 170 miles, \$2452" "$got638" "$expected638" "${error638}%"

echo ""
echo "🚨 New High-Error Cases from Previous Eval:"
echo "------------------------------------------"
printf "%-30s %-12s %-12s %-12s\n" "Case Description" "Got" "Expected" "Error %"

# New High-Error Case 151: 12 days, 528 miles, $2476.41
got151=$(./run.sh 12 528 2476.41)
expected151="1662.88"
error151=$(echo "scale=1; (($got151 - $expected151) / $expected151) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "12 days, 528 miles, \$2476" "$got151" "$expected151" "${error151}%"

# New High-Error Case 736: 11 days, 532 miles, $2419.86
got736=$(./run.sh 11 532 2419.86)
expected736="1653.69"
error736=$(echo "scale=1; (($got736 - $expected736) / $expected736) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "11 days, 532 miles, \$2419" "$got736" "$expected736" "${error736}%"

# New High-Error Case 392: 12 days, 398 miles, $2481.44
got392=$(./run.sh 12 398 2481.44)
expected392="1755.18"
error392=$(echo "scale=1; (($got392 - $expected392) / $expected392) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "12 days, 398 miles, \$2481" "$got392" "$expected392" "${error392}%"

# New High-Error Case 500: 14 days, 467 miles, $2176.26
got500=$(./run.sh 14 467 2176.26)
expected500="1809.83"
error500=$(echo "scale=1; (($got500 - $expected500) / $expected500) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "14 days, 467 miles, \$2176" "$got500" "$expected500" "${error500}%"

# New High-Error Case 940: 1 day, 1002 miles, $2320.13
got940=$(./run.sh 1 1002 2320.13)
expected940="1475.40"
error940=$(echo "scale=1; (($got940 - $expected940) / $expected940) * 100" | bc -l 2>/dev/null || echo "N/A")
printf "%-30s %-12s %-12s %-12s\n" "1 day, 1002 miles, \$2320" "$got940" "$expected940" "${error940}%"

echo ""
echo "🎯 Key Metrics to Watch:"
echo "------------------------"

# Calculate some basic error metrics for our test cases
high_intensity_1=$(./run.sh 2 1189 1164.74)
high_intensity_2=$(./run.sh 1 809 1734.56)
high_receipt_1=$(./run.sh 4 69 2321.49)
high_receipt_2=$(./run.sh 5 516 1878.49)
high_receipt_3=$(./run.sh 8 792 2437.24)

echo "High-intensity cases: Closer to expected = better"
echo "High-receipt cases: Lower values = better (avoiding over-reimbursement)"
echo ""
echo "💡 Run './eval.sh' for full 1000-case evaluation"
echo "💡 Run 'uv run python train_ensemble.py' to retrain models"
