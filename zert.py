import time
import sys
import random

RED = "\033[91m"
RESET = "\033[0m"

def slow_typing(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_heart_slowly():
    heart_lines = [
        "        *****       *****  ",
        "      *******     *******  ",
        "     *********   *********  ",
        "     *********   *********  ",
        "      ********   ********  ",
        "        ****************  ",
        f"        ❤ 𝒥𝑜𝓎 𝒜𝓊𝓂𝒶 ❤  ",
        "          ************  ",
        "            ******  ",
        "              **  "
    ]
    
    for line in heart_lines:
        slow_typing(RED + line + RESET, 0.1)
        time.sleep(0.3)

roses = [
    "     🌹       🌹       🌹       🌹",
    "        🌹       🌹       🌹",
    "           🌹       🌹",
    "              🌹"
]

for i in range(3, 0, -1):
    slow_typing(f"🔥 Naughty thoughts loading in {i}... ")
    time.sleep(1)

for _ in range(3):
    draw_heart_slowly()
    slow_typing(f"💋 You make my mind wander into deliciously wicked places... 💋", 0.1)
    time.sleep(1)

for rose in roses:
    slow_typing(RED + rose + RESET, 0.1)
    time.sleep(0.5)

naughty_lines = [
    "If my words could touch you... where would you want them the most? 😏",
    "I don't just talk... I make you feel every. single. word. 🔥",
    "You can try to resist, but we both know how this ends... 😈",
    "I could whisper my fantasies to you... but wouldn't you rather experience them? 😏",
    "Would you rather hear my voice in your ear... or feel my breath on your skin? 🔥",
    "Tell me... how long can you handle being teased? 😈",
    "Imagine me right behind you... close your eyes. Feel that? 😏",
    "Every time you read this... I want you to shiver just a little. 🔥",
    "The way your name rolls off my tongue... I wonder how you'd sound saying mine. 😏",
    "Do you like being in control... or do you secretly crave being handled? 🔥",
]

slow_typing("\nTell me... should I keep teasing, or should I make you beg? 😏\n", 0.07)
time.sleep(1)

for line in naughty_lines:
    slow_typing(f"💋 {line}")
    time.sleep(random.uniform(1, 2))

slow_typing("\n😈 Enough for now... unless you want more. And I know you do. 😏🔥")