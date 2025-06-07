#!/bin/bash

# Activate the UV environment and run ensemble prediction
uv run python -c "
import sys
from ensemble import EnsemblePredictor

# Create ensemble predictor
predictor = EnsemblePredictor()

# Get inputs from command line
days = float(sys.argv[1])
miles = float(sys.argv[2])
receipts = float(sys.argv[3])

# Predict using ensemble
result = predictor.predict(days, miles, receipts)

# Output result
print(f'{result:.2f}')
" $1 $2 $3