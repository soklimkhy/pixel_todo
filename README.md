# Pixel Todo List

A simple, stylish, **pixel-art inspired** ToDo list desktop app built with Python and PyQt6.

![demo](https://github.com/soklimkhy/pixel_todo/raw/main/asset/gif/GIF.gif)
---
[![Download](https://img.shields.io/badge/Download-Pixel--Todo--v1.0.0-blue)](https://github.com/soklimkhy/pixel_todo/releases/tag/v1.0.0)

## Features

- 📝 Add, edit, and delete tasks
- 💾 Tasks are saved to a local `config.json` file
- 🎨 Custom pixel-art UI with retro font and icons
- 🖱️ Drag the custom title bar to move the window
- 🗔 Frameless window for a clean look
- 🛠️ Easy to package as a standalone `.exe` with PyInstaller

---

## Installation

1. **Clone this repository:**
    ```sh
    git clone https://github.com/yourusername/pixel-todo-list.git
    cd pixel-todo-list
    ```

2. **Install dependencies:**
    ```sh
    pip install PyQt6
    ```

3. **Run the app:**
    ```sh
    python main.py
    ```

---

## Packaging as an EXE

You can build a standalone executable using [PyInstaller](https://pyinstaller.org/):

### One-file mode

```sh
pyinstaller main.py --onefile --windowed --icon=asset/logo/icon.ico --add-data "asset/img;asset/img" --add-data "asset/font;asset/font" --add-data "asset/logo;asset/logo"
```

### One-dir mode

```sh
pyinstaller main.py --onedir --windowed --icon=asset/logo/icon.ico --add-data "asset/img;asset/img" --add-data "asset/font;asset/font" --add-data "asset/logo;asset/logo"
```

---

## Project Structure

```
todolist-py/
│
├── asset/
│   ├── font/      # Pixel font (e.g. pressstart2p.ttf)
│   ├── img/       # Screenshots, button images
│   └── logo/      # App icon
│
├── controller/
│   └── main_controller.py
├── gui/
│   └── main_gui.py
├── util/
│   └── path_utils.py
├── config.json    # Saved tasks
├── main.py
└── README.md
```

---

## How It Works

- **All tasks** are stored in `config.json` in the app directory.
- **UI** is built with PyQt6, using a custom pixel font and icons.
- **Add/Edit/Delete** tasks using the buttons or by selecting a task and editing.
---
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Enjoy your retro productivity! 🚀
