def calculate_depreciation(cost, salvage, life): — this defines a function: a named, reusable block of code. cost, salvage, life are parameters — placeholders for whatever values get passed in when the function is called.
The """...""" line — a docstring, a description of what the function does. Good practice, and something reviewers (or future-you) appreciate.
return — instead of print-ing inside the function, it returns a value back to whoever called it. That's what lets the same function feed a result into a print statement, a report, a spreadsheet export — anywhere.
calculate_depreciation(asset["cost"], asset["salvage"], asset["life"]) — this calls the function, passing in that asset's specific values. The loop calls it once per asset, so the formula and the validation logic exist in exactly one place instead of being copy-pasted.

I also added a fourth test asset with bad data (salvage > cost) to confirm the validation logic — which used to only live in your single-asset script — now works inside the batch/loop version too. It correctly flagged it instead of crashing or producing nonsense.

