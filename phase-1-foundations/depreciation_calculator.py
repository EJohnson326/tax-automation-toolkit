# Straight-line depreciation calculator with input validation

asset_cost = float(input("Asset cost: "))
salvage_value = float(input("Salvage value: "))
useful_life_years = float(input("Useful life (years): "))

if useful_life_years <= 0:
    print("Useful life must be greater than zero.")
elif asset_cost < 0 or salvage_value < 0:
    print("Cost and salvage value cannot be negative.")
elif salvage_value > asset_cost:
    print("Salvage value cannot exceed asset cost.")
else:
    annual_depreciation = (asset_cost - salvage_value) / useful_life_years
    print("Annual depreciation:", annual_depreciation)
