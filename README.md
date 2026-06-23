# Blackjack

A command-line Blackjack game written in Python.

## Features

- Standard 52-card deck with proper shuffling
- Correct Blackjack hand evaluation, including soft/hard Ace logic
- Dealer stands on 17 (hard or soft)
- Detects busts, wins, losses, and ties (push)
- Play multiple rounds in a single session

## Project Structure

```
.
├── card.py     # Card class — suit, rank, and point value
├── deck.py     # Deck class — builds, shuffles, and deals cards
├── game.py     # Game class — hand logic, hit/stand, winner determination
└── main.py     # Entry point — CLI interface and game loop
```

## Requirements

- Python 3.6+
- No external dependencies

## Getting Started

```bash
python main.py
```

## How to Play

1. You and the dealer are each dealt two cards. One of the dealer's cards is hidden.
2. Choose **Hit** (`h`) to draw another card or **Stand** (`s`) to hold your hand.
3. Try to get as close to **21** as possible without going over.
4. Once you stand, the dealer reveals their hidden card and draws until reaching at least 17.
5. Highest hand without busting wins. A tie is called a **push**.

### Card Values

| Card | Value |
|------|-------|
| 2–10 | Face value |
| Jack, Queen, King | 10 |
| Ace | 11 (counts as 1 if hand would bust) |
