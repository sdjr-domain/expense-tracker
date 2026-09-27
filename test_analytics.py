import sqlite3
from datetime import datetime
from database.db import get_db, get_analytics_summary, get_budget_adherence, get_spending_velocity, get_baseline_split

def test():
    user_id = 1

    test_cases = [
        ("1 Month", "2026-09-01", "2026-09-30"),
        ("3 Months", "2026-07-01", "2026-09-30"),
        ("1 Year", "2026-01-01", "2026-12-31"),
    ]

    print("Testing Analytics Data Layer...")
    for label, start_date, end_date in test_cases:
        print(f"\n--- {label} ({start_date} to {end_date}) ---")
        try:
            print("Budget Adherence:")
            print(get_budget_adherence(user_id, start_date, end_date))

            print("Summary:")
            print(get_analytics_summary(user_id, start_date, end_date))

            print("Baseline Split:")
            print(get_baseline_split(user_id, start_date, end_date))
        except Exception as e:
            print(f"❌ Error during {label}: {e}")
            import traceback
            traceback.print_exc()

    print("\n✅ All database functions executed.")

if __name__ == "__main__":
    test()
