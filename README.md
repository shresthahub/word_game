# 🎮 Word Games: Scrabble & Ghost
This repository contains two interactive word games built with Python:
- Scrabble-like Game (Single Player)
- Ghost Game (Two Player)

Both games rely on a common ```words.txt``` file for word validation.

## Files
- ```scrabble_game.py```- One-player word game inspired by Scrabble.
- ```ghost_game.py```- Two-player Ghost word game.
- ```Instructions.pdf```- Original assignment and game specifications.
- ```words.txt```- Word list used by both games (1 word per line, all lowercase).

---
## 1. Scrabble-like Word Game
A one-player game inspired by Scrabble. You receive a random set of 7 letters and must create valid words to score points.

### Feature
- Points assigned like real Scrabble.
- Bonus 50 points if you use all 7 letters in one word.
- Input validation for valid words.
- Option to replay hands or start new games.

### How to Run
```

python scrabble_game.py

```
### Game Options
- ```n```: Start a new game with a new hand.
- ```r```: Replay the previous hand.
- ```e```: Exit the game.
---
## 2. Ghost Word Game (Two Players)
A classic two-player word-building game where players take turns adding letters. Don’t complete a word, and don’t get stuck!

### Feature
- Players take turns typing one letter at a time.
- If a player finishes a valid word (4+ letters), they lose.
- If a fragment is not a prefix to any word, they lose.
- Only letters are accepted; invalid inputs are rejected.

### How to Run
```

python ghost_game.py

```
The game will guide both players through each turn with prompts and fragment updates.

---

## 📌 Future Work

- **Timed Gameplay**: Introduce time limits for each turn to add challenge and urgency.
- **GUI Integration**: Build a graphical interface using Tkinter or PyGame for a more interactive experience.
- **Multiplayer Online**: Implement real-time multiplayer mode for Ghost using sockets or a web framework like Flask.
- **Score Tracking & Leaderboards**: Add persistent high score tracking using a local database (like SQLite) or a cloud-based leaderboard.
- **AI Opponent (for Scrabble)**: Create an AI that can suggest or play optimal words from a given hand.
- **Enhanced Input Validatio**n: Improve handling of special characters, numbers, and uppercase letters to make the game more robust.

## License
This project is licensed under the MIT License.

