#!/usr/bin/env python3
"""
Calculate bets to scale in for mean reversion strategy.

Usage:
./bet-scale-in.py
"""


def calculate_values(x):
    a = 0.99 * x
    b = 0.99 * a
    c = 0.99 * b
    d = 0.99 * c

    # Calculate 1% of each value and the value after subtraction
    # Format subtracted_values to 2 decimal places
    values = [x, a, b, c, d]
    one_percent_values = [0.01 * value for value in values]
    subtracted_values = [
        round(value - one_percent, 2) for value, one_percent in zip(values, one_percent_values)
    ]

    return values, one_percent_values, subtracted_values


def print_table(x):
    values, one_percent_values, subtracted_values = calculate_values(x)
    rows = [
        f"Buy {subtracted_values[0]} for 0.1 per point",
        f"Buy {subtracted_values[1]} for 0.2 per point",
        f"Buy {subtracted_values[2]} for 0.4 per point",
        f"Buy {subtracted_values[3]} for 0.8 per point",
        f"Buy {subtracted_values[4]} for 1 per point",
    ]
    for row in rows:
        print(row)


if __name__ == "__main__":
    try:
        x = float(input("Please enter the value to start position: "))
        print_table(x)
    except ValueError:
        print("Please enter a valid number for x.")
