# 🎮 Tetris Game

## 📝 Description

This is a classic **Tetris game** built using **Python** and the **Pygame** library. Players control falling tetrominoes (shapes made of 4 blocks) by rotating and moving them horizontally as they descend. The goal is to fill complete horizontal rows, which will then disappear, making room for more blocks. The game speeds up over time, increasing the difficulty. The game ends when there is no more space for new tetrominoes at the top of the screen. 🟦🟧🟨🟩

## 🌟 Key Features

- **Classic Tetris gameplay** with intuitive controls 🕹️
- **Increasing difficulty** as the game progresses ⏩
- **Score tracking** based on the number of rows cleared 📊
- **Responsive controls** for moving and rotating pieces 🔄

## 🖥️ Technologies Used

- **Python**: The primary programming language used to develop the game 🐍
- **Pygame**: A Python library for game development, used for handling graphics, input, and game logic 🎮
- **Git**: Version control system to manage code changes and collaboration 🔄

## 📦 Installation Requirements

### 🔧 Prerequisites

1. **Python 3.12.9**: Ensure that you have Python 3.12.9 installed. You can download it from [python.org](https://www.python.org/). 🐍
2. **Pygame**: The game relies on the Pygame library for graphics and game logic. You can install it via pip:
   ```bash
   pip install pygame
   ```

### 🛠️ Setup Instructions

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Eleazarovich/Tetris-Game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd tetris-game
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:
   ```bash
   python main.py
   ```

## 🎮 Basic Usage

Once the game is running, you'll be able to control the falling tetrominoes using the following keyboard inputs:

- **⬅️ Arrow Left**: Move the current piece left.
- **➡️ Arrow Right**: Move the current piece right.
- **⬆️ Arrow Up**: Rotate the current piece.
- **⬇️ Arrow Down**: Speed up the fall of the current piece.

Press **any key** to start the game from the main menu. 🚀

## 💡 Features Overview

- **Classic Tetris Gameplay**: Play the iconic game with rotating and moving shapes 🧩
- **Score Tracking**: Points are awarded based on the number of rows you clear 💯
- **Increasing Speed**: As you progress, the game will become faster ⏩
- **Game Over**: The game ends when no space is available for new pieces at the top 🛑

## ⚙️ Configuration Options

- The game speed increases every few seconds, but the speed can be adjusted by modifying the `fall_speed` variable in `main.py`. 🕹️
- You can customize the screen size, piece colors, and other game settings by adjusting variables in `main.py`. 🎨

## 🚧 Troubleshooting

- **Pygame Not Installed**: If you encounter an error indicating that `pygame` is missing, make sure you run the following command:
  ```bash
  pip install pygame
  ```
- **Game Does Not Run**: Ensure that you have Python 3.12.9 installed and that you are using the correct Python version. You can verify this by running:
  ```bash
  python --version
  ```
- **Game Crashes or Freezes**: Try restarting the game. If the issue persists, check for any errors in the console output and feel free to submit an issue in the GitHub repository. 🐞

## 🗂️ Code Structure Overview

The project is organized as follows:

```
Tetris-Game/
│
├── .gitpod.yml           # Gitpod configuration file for cloud-based development 🌐
├── README.md             # Project documentation (this file) 📄
├── main.py               # The main Python script that contains the game logic and functions 🎮
├── requirements.txt      # Lists the required Python libraries (e.g., pygame) 📋
```

- **`.gitpod.yml`**: Configuration file for Gitpod, an online development environment. 🌐
- **`README.md`**: Project documentation, including setup instructions, features, and usage. 📚
- **`main.py`**: The core script containing all the game functionality, including the game loop, input handling, and rendering. 🕹️
- **`requirements.txt`**: A file that specifies the Python dependencies (like Pygame) required to run the game. 📋

## 🤝 Contributing Guidelines

We welcome contributions to improve the Tetris game. Here's how you can help:

1. Fork the repository and create a new branch. 🍴
2. Make your changes and add tests if applicable. 🧪
3. Ensure that the game still works by running the script. ✅
4. Submit a pull request with a detailed description of your changes. 📥

Please ensure that your code follows the PEP8 style guide for Python. 🧑‍💻