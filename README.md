# 🔐 Pin Generator

A colorful and customizable PIN generator with support for varying complexity levels and visual flair using ANSI escape codes.

## ✨ Features

- Generate PINs with 3 levels of complexity:
  1. **Basic** – Includes digits, uppercase, lowercase, and symbols (1 of each).
  2. **Moderate** – Includes 2 of each type.
  3. **Advanced** – Fully random characters from a large pool.
- Colored output for each PIN character.
- Custom PIN length selection (for complexity level 3).
- Regenerate or restart with easy prompts.

## 🧠 Complexity Levels

| Level | Content                                    | Use Case          |
|-------|--------------------------------------------|-------------------|
| 1     | 1 digit, 1 uppercase, 1 lowercase, 1 symbol | Simple PINs       |
| 2     | 2 of each category                         | Moderate security |
| 3     | Fully randomized from pool                 | Maximum entropy   |

## 🖥️ How to Use

1. Run the script.
2. Select a complexity level.
3. If using level 3, choose a custom length.
4. View and regenerate colorful PINs on demand.

## 📦 Dependencies

- Python standard library only (no external packages).
- Custom module: `screen_manager.py` (handles terminal visuals).

## ⚙️ Example

```text
Enter pin complexity type: (1), (2), or (3): 3  
How many digit pin: 12  

PIN: ░▐█a#R7k(2&Z
