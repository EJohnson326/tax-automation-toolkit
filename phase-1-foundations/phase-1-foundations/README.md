markdown
# Phase 1: Foundations

Early scripts applying core Python — variables, input handling, and conditional logic — applied to real accounting calculations rather than generic exercises.

## Projects

### depreciation_calculator.py
A straight-line depreciation calculator that prompts for asset cost, salvage value, and useful life, then returns annual depreciation.

**What it does:**
- Calculates annual depreciation using the straight-line method: `(Cost − Salvage Value) / Useful Life`
- Validates input before calculating — rejects a useful life of zero (which would otherwise crash the program), negative cost/salvage values, and a salvage value that exceeds the asset cost
- Built to be run interactively from the command line

**Why it matters:** most "calculator" scripts online assume clean input. This one handles the bad data a real user might enter, which is the difference between a demo and a tool someone could actually use.

**Run it:**
​```
python3 depreciation_calculator.py
​```
