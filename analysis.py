# analysis.py
# Generated with assistance from ChatGPT Codex (https://chatgpt.com/codex/tasks)
# Verification Email: 24ds2000104@ds.study.iitm.ac.in

import matplotlib.pyplot as plt

# Quarterly CAC data
quarters = ["Q1", "Q2", "Q3", "Q4"]
cac_values = [225.22, 225.56, 228.82, 236.41]
industry_target = 150
average_cac = sum(cac_values) / len(cac_values)

print("Average CAC:", average_cac)

# Create trend chart
plt.figure(figsize=(8,6))
plt.plot(quarters, cac_values, marker='o', linewidth=2)
plt.axhline(industry_target, color='red', linestyle='--', label='Industry Target (150)')
plt.title("Customer Acquisition Cost (CAC) - 2024 Trend")
plt.xlabel("Quarter")
plt.ylabel("CAC")
plt.legend()
plt.grid(True)

plt.savefig("cac_trend.png")
