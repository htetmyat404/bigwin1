#!/usr/bin/env python3
# Hacker-style ASCII banner: "M A Loe"
# Works with or without pyfiglet.

import os
import sys
import time
import shutil
import random

TEXT = "M A Loe"   # <- စကားလုံးပြောင်းချင်ရင် ဒီလို ပြောင်းနိုင်

GREEN  = "\033[32m"
DIM    = "\033[2m"
RESET  = "\033[0m"
BOLD   = "\033[1m"
BG     = "\033[40m"  # black background

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def center_lines(lines, width=None):
    if width is None:
        width = shutil.get_terminal_size((80, 24)).columns
    return [line.center(width) for line in lines]

def matrix_rain(duration=2.5):
    cols = shutil.get_terminal_size((80, 24)).columns
    rows = shutil.get_terminal_size((80, 24)).lines
    symbols = "01░▒▓#@$%&*+=-"
    start = time.time()
    # prepare columns with random speeds
    speed = [random.uniform(0.01, 0.05) for _ in range(cols)]
    last = [0.0] * cols
    while time.time() - start < duration:
        out = []
        for r in range(rows - 1):
            row_chars = []
            for c in range(cols):
                if random.random() < 0.02:
                    ch = random.choice(symbols)
                else:
                    ch = " "
                row_chars.append(ch)
            out.append("".join(row_chars))
        clear()
        print(BG + GREEN + "\n".join(out) + RESET)
        # tiny per-frame sleep
        time.sleep(0.03)

def try_pyfiglet(text):
    try:
        from pyfiglet import Figlet
    except Exception:
        return None
    fonts = ["ANSI Shadow", "Big", "Banner3-D", "Chunky", "DOS Rebel", "Cyberlarge"]
    f = Figlet(font=random.choice(fonts))
    art = f.renderText(text)
    return art.splitlines()

# Fallback big block letters for A, E, L, M, O, space
FALLBACK_FONT = {
    "A": [
        "    ██     ",
        "   ████    ",
        "  ██  ██   ",
        " ████████  ",
        " ██    ██  ",
        " ██    ██  ",
    ],
    "E": [
        " ████████  ",
        " ██        ",
        " ██████    ",
        " ██        ",
        " ██        ",
        " ████████  ",
    ],
    "L": [
        " ██        ",
        " ██        ",
        " ██        ",
        " ██        ",
        " ██        ",
        " ████████  ",
    ],
    "M": [
        " ██    ██  ",
        " ███  ███  ",
        " ██ ██ ██  ",
        " ██ ██ ██  ",
        " ██    ██  ",
        " ██    ██  ",
    ],
    "O": [
        "  ██████   ",
        " ██    ██  ",
        " ██    ██  ",
        " ██    ██  ",
        " ██    ██  ",
        "  ██████   ",
    ],
    " ": [
        "    ",
        "    ",
        "    ",
        "    ",
        "    ",
        "    ",
    ],
}

def fallback_render(text):
    text = text.upper()
    # map unknown chars to space
    blocks = [FALLBACK_FONT.get(ch, FALLBACK_FONT[" "]) for ch in text]
    lines = []
    for row in range(len(FALLBACK_FONT["A"])):
        line = " ".join(block[row] for block in blocks)
        lines.append(line.rstrip())
    return lines

def main():
    clear()
    # Hacker intro rain
    matrix_rain(duration=2.8)

    # Build banner
    lines = try_pyfiglet(TEXT)
    if lines is None:
        lines = fallback_render(TEXT)

    # Center & colorize
    width = shutil.get_terminal_size((80, 24)).columns
    centered = center_lines(lines, width)

    clear()
    print(BG + GREEN + BOLD)
    print("\n".join(centered))
    print(RESET)

    # little blinking cursor vibe
    sys.stdout.write(GREEN + DIM + center_lines(["[ press Ctrl+C to exit ]"], width)[0] + RESET + "\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clear()

if __name__ == "__main__":
    main()
