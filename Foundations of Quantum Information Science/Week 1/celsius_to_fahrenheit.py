#!/usr/bin/env python3
"""celsius_ti_fahrenheit.py"""

def main() -> None:
    for celsius in range(-44, 105, 4):
        fahrenheit: float = 32 + (celsius) * 9 / 5
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")


if __name__ == "__main__":
    main()