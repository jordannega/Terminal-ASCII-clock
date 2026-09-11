#!/usr/bin/env python3
"""A tiny terminal clock that also shows how much of the day has passed."""

import time
import os
from datetime import datetime

BAR_WIDTH = 40

def render():
    now = datetime.now()
    seconds_today = now.hour * 3600 + now.minute * 60 + now.second
    total = 86400
    ratio = seconds_today / total

    filled = int(BAR_WIDTH * ratio)
    bar = "█" * filled + "░" * (BAR_WIDTH - filled)

    os.system("cls" if os.name == "nt" else "clear")
    print()
    print(f"   ⏰  {now.strftime('%H:%M:%S')}   {now.strftime('%A, %B %d, %Y')}")
    print()
    print(f"   [{bar}]  {ratio*100:5.2f}%")
    print()
    print(f"   {seconds_today:,} / {total:,} seconds today")
    print()

if __name__ == "__main__":
    try:
        while True:
            render()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n   bye 👋\n")
