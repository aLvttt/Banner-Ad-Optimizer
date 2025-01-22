import tkinter as tk
from tkinter import messagebox

def best_variant():
    try:
        budget = float(entry_budget.get())
        cpm = float(entry_cpm.get())
        cpc = float(entry_cpс.get())
        fixed_price = float(entry_fixed_price.get())
        daily_visits = int(entry_daily_visits.get())
        target_percentage = float(entry_target_percentage.get())
        ctr = float(entry_ctr.get())

        # cpm
        impressions = budget / cpm * 1000
        cpm_clicks = impressions * (ctr / 100)

        # cpc
        cpc_clicks = budget / cpc

        # click for fixed placement
        weekly_visits = daily_visits * 7
        target_audience = weekly_visits * (target_percentage / 100)
        fixed_clicks = target_audience * (ctr / 100)

        # result
        if cpm_clicks > cpc_clicks and cpm_clicks > fixed_clicks:
            result = "CPM"
        elif cpc_clicks > cpm_clicks and cpc_clicks > fixed_clicks:
            result = "CPC"
        else:
            result = "Fixed"

        result_text = f"Results: \nCPM-model: {cpm_clicks:.2f} clicks\nCPC-model: {cpc_clicks:.2f} clicks\nFixed placement: {fixed_clicks:.2f} clicks\nBest variant: {result}"
        messagebox.showinfo("Results", result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# visual
root = tk.Tk()
root.title("Ad optimizer")
root.geometry("400x400")

tk.Label(root, text="Budget ($):").pack()
entry_budget = tk.Entry(root)
entry_budget.pack()

tk.Label(root, text="CPM ($ per 1000 impressions):").pack()
entry_cpm = tk.Entry(root)
entry_cpm.pack()

tk.Label(root, text="CPC ($ per click):").pack()
entry_cpс = tk.Entry(root)
entry_cpс.pack()

tk.Label(root, text="Fixed price ($ per week):").pack()
entry_fixed_price = tk.Entry(root)
entry_fixed_price.pack()

tk.Label(root, text="Average number of visits per day:").pack()
entry_daily_visits = tk.Entry(root)
entry_daily_visits.pack()

tk.Label(root, text="target audience percentage (%):").pack()
entry_target_percentage = tk.Entry(root)
entry_target_percentage.pack()

tk.Label(root, text="CTR (%):").pack()
entry_ctr = tk.Entry(root)
entry_ctr.pack()

tk.Button(root, text="Calculate", command=best_variant).pack()

root.mainloop()