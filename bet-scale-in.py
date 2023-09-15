#!/usr/bin/env python3
"""
Calculate bets to scale in for mean reversion strategy.

Usage:
./bet-scale-in.py
"""


def calculate_values(x):
    """
    Calculate a series of values by repeatedly multiplying x by 0.99.
    Also calculate 1% of each value and the value after subtracting 1%.
    Format subtracted_values to 2 decimal places.
    """
    values = [x]
    for _ in range(4):
        values.append(0.99 * values[-1])

    one_percent_values = [0.01 * value for value in values]
    subtracted_values = [
        round(value - one_percent, 2) for value, one_percent in zip(values, one_percent_values)
    ]

    return values, one_percent_values, subtracted_values


def print_table(x):
    """
    Print a table of buy orders, with each row representing a different order.
    The number of points for each order is calculated by the calculate_values function.
    """
    values, one_percent_values, subtracted_values = calculate_values(x)
    points = [0.1, 0.2, 0.4, 0.8, 1]
    rows = [
        f"Buy {subtracted_value} for {point} per point"
        for subtracted_value, point in zip(subtracted_values, points)
    ]
    for row in rows:
        print(row)


if __name__ == "__main__":
    try:
        x = float(input("Please enter the value to start position: "))
        print_table(x)
    except ValueError:
        print("Please enter a valid number for x.")
