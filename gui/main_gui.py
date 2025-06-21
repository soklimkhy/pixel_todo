from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QLabel
)
from PyQt6.QtGui import QIcon, QFontDatabase, QFont, QMouseEvent
from PyQt6.QtCore import Qt, QPoint
from controller.main_controller import add_task, delete_task, load_tasks, save_tasks
from util.path_utils import resource_path

# ...existing imports...

class PixelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(400, 500)
        self.setStyleSheet("background: #111; border: none; border-radius: 0px;")

        # Load pixel font
        font_id = QFontDatabase.addApplicationFont(resource_path("asset/font/pressstart2p.ttf"))
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        pixel_font = QFont(font_families[0], 8) if font_families else QFont("Arial", 8)

        # --- Custom Toolbar ---
        titlebar = QWidget()
        titlebar.setFixedHeight(30)
        titlebar.setStyleSheet("background: #222; border-buttom: 1px solid #fff;")
        title_layout = QHBoxLayout(titlebar)
        title_layout.setContentsMargins(5, 0, 0, 0)
        

        # icon = QLabel()
        # icon.setPixmap(QIcon(resource_path("asset/logo/icon.ico")).pixmap(30, 30))
        # icon.setStyleSheet("background: none; border: none; padding: 0; margin: 0;")

        title = QLabel("PIXELTODO")
        title.setFont(pixel_font)
        title.setStyleSheet("color: #fff; background: none; border: none; padding: 0; margin: 0; font-size: 14px;")
        #title_layout.addWidget(icon)
        title.setContentsMargins(5, 0, 0, 0)
        title_layout.addWidget(title)
        title_layout.addStretch()

        close_btn = QPushButton("X")
        close_btn.setFont(pixel_font)
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet(
            "QPushButton { background: #e74c3c; color: #fff; border: none; border-radius: 0px; }"
            "QPushButton:hover { background: #c0392b; }"
        )
        close_btn.clicked.connect(self.close)
        title_layout.addWidget(close_btn)

        # Drag support
        self._drag_pos = None
        def mousePressEvent(event: QMouseEvent):
            if event.button() == Qt.MouseButton.LeftButton:
                self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                event.accept()
        def mouseMoveEvent(event: QMouseEvent):
            if self._drag_pos and event.buttons() == Qt.MouseButton.LeftButton:
                self.move(event.globalPosition().toPoint() - self._drag_pos)
                event.accept()
        def mouseReleaseEvent(event: QMouseEvent):
            self._drag_pos = None
            event.accept()
        titlebar.mousePressEvent = mousePressEvent
        titlebar.mouseMoveEvent = mouseMoveEvent
        titlebar.mouseReleaseEvent = mouseReleaseEvent

        # --- Input Area ---
        input_area_widget = QWidget()
        input_area_widget.setStyleSheet("background: #111; border: none; border-radius: 0px;")

        input_area_layout = QHBoxLayout(input_area_widget)
        input_area_layout.setContentsMargins(8, 8, 8, 8)
        input_area_layout.setSpacing(8)
        

        input_field = QLineEdit()
        input_field.setPlaceholderText("Enter task...")
        input_field.setFont(pixel_font)
        input_field.setStyleSheet(
            "QLineEdit { background: #111; color: #fff; border: 1px solid #fff; border-radius: 0px; padding: 5px;}"
        )

        add_btn = QPushButton("A")
        add_btn.setFont(pixel_font)
        add_btn.setFixedSize(30, 30)
        add_btn.setStyleSheet(
            "QPushButton { background: #27ae60; color: #fff; border: none; border-radius: 0px; }"
            "QPushButton:hover { background: #219150; }"
        )

        edit_btn = QPushButton("E")
        edit_btn.setFont(pixel_font)
        edit_btn.setFixedSize(30, 30)
        edit_btn.setStyleSheet(
            "QPushButton { background: #2980b9; color: #fff; border: none; border-radius: 0px; }"
            "QPushButton:hover { background: #1c5a86; }"
        )

        del_btn = QPushButton("D")
        del_btn.setFont(pixel_font)
        del_btn.setFixedSize(30, 30)
        del_btn.setStyleSheet(
            "QPushButton { background: #e67e22; color: #fff; border: none; border-radius: 0px; }"
            "QPushButton:hover { background: #ca6b17; }"
        )

        input_area_layout.addWidget(input_field)
        input_area_layout.addWidget(add_btn)
        input_area_layout.addWidget(edit_btn) 
        input_area_layout.addWidget(del_btn)

        # --- Task List ---
        task_list_widget = QListWidget()
        task_list_widget.setFont(pixel_font)
        task_list_widget.setStyleSheet(
            "QListWidget { background: #111; color: #fff; border: 1px solid #fff; border-radius: 0px; }"
            "QListWidget::item { border-bottom: 1px solid #fff; padding: 6px; }"
            "QListWidget::item:selected { background: #3498db; color: #fff; }"
        )
        task_list_layout = QVBoxLayout()
        task_list_layout.setContentsMargins(8, 0, 8, 8)
        task_list_layout.addWidget(task_list_widget)

        # --- Main Layout ---
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add sections to main layout
        toolbar_layout = QVBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.addWidget(titlebar)

        main_layout.addLayout(toolbar_layout)
        main_layout.addWidget(input_area_widget)
        main_layout.addLayout(task_list_layout)

        # Load tasks
        self.tasks = load_tasks()
        for task in self.tasks:
            task_list_widget.addItem(task)
        
        self.editing_index = None

        def add_task_to_ui():
            task_text = input_field.text()
            if task_text:
                if self.editing_index is not None:
                    # Update existing task
                    self.tasks[self.editing_index] = task_text
                    task_list_widget.item(self.editing_index).setText(task_text)
                    
                    save_tasks(self.tasks)
                    self.editing_index = None
                    add_btn.setText("A")
                else:
                    self.tasks = add_task(self.tasks, task_text)
                    task_list_widget.addItem(task_text)
                input_field.clear()

        def edit_selected_task():
            row = task_list_widget.currentRow()
            if row >= 0:
                input_field.setText(self.tasks[row])
                self.editing_index = row
                add_btn.setText("✓") 
        def delete_selected_task():
            row = task_list_widget.currentRow()
            if row >= 0:
                self.tasks = delete_task(self.tasks, row)
                task_list_widget.takeItem(row)
                # Reset edit mode if the deleted task was being edited
                if self.editing_index == row:
                    self.editing_index = None
                    add_btn.setText("A")

        add_btn.clicked.connect(add_task_to_ui)
        del_btn.clicked.connect(delete_selected_task)
        edit_btn.clicked.connect(edit_selected_task)

def create_main_window():
    return PixelWindow()