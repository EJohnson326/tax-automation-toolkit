# Phase 1: Foundations

Early scripts built while learning core Python — variables, input handling, conditionals, loops, and functions — applied to real accounting calculations rather than generic exercises.

## Projects

### depreciation_toolkit.py
A straight-line depreciation tool that processes a batch of assets at once and validates each one before calculating.

**What it does:**
- Calculates annual depreciation using the straight-line method: `(Cost − Salvage Value) / Useful Life`
- Processes any number of assets in a single run, via a list of asset records
- Validates each asset's data independently — rejects a useful life of zero, negative cost/salvage values, or a salvage value exceeding cost — without stopping the batch for the other assets
- Core logic lives in a single reusable function, so validation and calculation rules only need to be maintained in one place

**Why it matters:** real bookkeeping work rarely involves one asset at a time. This version reflects how the tool would actually get used — processing a client's full fixed asset list in one pass, flagging bad records without derailing the rest.
