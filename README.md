# Phase 1: Foundations

Scripts built while learning core Python — variables, input handling, conditionals, loops, functions, and error handling — applied to real accounting calculations rather than generic exercises.

## Projects

### depreciation_toolkit.py
An interactive straight-line depreciation tool that accepts any number of assets, validates each one, and gracefully handles invalid input instead of crashing.

**What it does:**
- Calculates annual depreciation using the straight-line method: `(Cost − Salvage Value) / Useful Life`
- Prompts for assets one at a time until the user presses Enter with no name, so it works for a single asset or a whole list
- Validates each asset's numbers — rejects a useful life of zero, negative cost/salvage values, or a salvage value exceeding cost — without stopping the run for other assets
- Catches non-numeric input (e.g. someone typing "fifty thousand" instead of "50000") and re-prompts instead of crashing
- Core calculation logic lives in a single reusable function, so validation and calculation rules only need to be maintained in one place

**Why it matters:** a real client-facing tool has to survive typos and bad data without dying mid-run. This version does — it's built to be handed to someone else to use, not just run once by the person who wrote it.

**Run it:**
​```
python3 depreciation_toolkit.py
​```

### depreciation_calculator.py
An earlier, single-asset version with interactive input and validation, kept to show the progression toward the toolkit above.
