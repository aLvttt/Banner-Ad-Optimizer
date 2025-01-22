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

def calculate_metrics():
    try:
        impressions = float(entry_impressions.get())
        unique_views = float(entry_unique_views.get())
        clicks = int(entry_clicks.get())
        cpm = float(entry_cpm_metrics.get())

        ad_freq = impressions / unique_views
        camp_cost = impressions / 1000 * cpm
        cost_per_contact = camp_cost / unique_views

        result_text = f"Results: \nAd frequency: {ad_freq:.2f}\nCampaign cost: {camp_cost:.2f}\nCost per contact: {cost_per_contact:.2f}"
        messagebox.showinfo("Results", result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# visual

def show_best_option_menu():
    clear_window()

    tk.Label(root, text="Budget ($):").pack()
    global entry_budget
    entry_budget = tk.Entry(root)
    entry_budget.pack()

    tk.Label(root, text="CPM ($ per 1000 impressions):").pack()
    global entry_cpm
    entry_cpm = tk.Entry(root)
    entry_cpm.pack()

    tk.Label(root, text="CPC ($ per click):").pack()
    global entry_cpс
    entry_cpс = tk.Entry(root)
    entry_cpс.pack()

    tk.Label(root, text="Fixed price ($ per week):").pack()
    global entry_fixed_price
    entry_fixed_price = tk.Entry(root)
    entry_fixed_price.pack()

    tk.Label(root, text="Average number of visits per day:").pack()
    global entry_daily_visits
    entry_daily_visits = tk.Entry(root)
    entry_daily_visits.pack()

    tk.Label(root, text="target audience percentage (%):").pack()
    global entry_target_percentage
    entry_target_percentage = tk.Entry(root)
    entry_target_percentage.pack()

    tk.Label(root, text="CTR (%):").pack()
    global entry_ctr
    entry_ctr = tk.Entry(root)
    entry_ctr.pack()

    tk.Button(root, text="Calculate", command=best_variant).pack()

def show_metrics_menu():
    clear_window()

    tk.Label(root, text="Impressions:").pack()
    global entry_impressions
    entry_impressions = tk.Entry(root)
    entry_impressions.pack()

    tk.Label(root, text="Unique views:").pack()
    global entry_unique_views
    entry_unique_views = tk.Entry(root)
    entry_unique_views.pack()

    tk.Label(root, text="Clicks:").pack()
    global entry_clicks
    entry_clicks = tk.Entry(root)
    entry_clicks.pack()

    tk.Label(root, text="CPM ($ per 1000 impressions):").pack()
    global entry_cpm_metrics
    entry_cpm_metrics = tk.Entry(root)
    entry_cpm_metrics.pack()

    tk.Button(root, text="Calculate", command=calculate_metrics).pack()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Button(root, text="Best variant", command=show_best_option_menu).pack()
    tk.Button(root, text="Metrics", command=show_metrics_menu).pack()

root = tk.Tk()
root.title("Ad optimizer")
root.geometry("400x400")

clear_window()
root.mainloop()
