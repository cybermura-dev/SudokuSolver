from PyQt6.QtWidgets import QPushButton


class ThemeToggle(QPushButton):
    """Custom Toggle Button for Theme Switching."""

    def __init__(self, parent_window, initial_theme="light"):
        super().__init__(parent_window)
        self.parent_window = parent_window
        self.current_theme = initial_theme
        self.update_style()
        self.setFixedSize(100, 40)
        self.clicked.connect(self.toggle_theme)

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.update_style()
        self.parent_window.switch_theme(self.current_theme)

    def update_style(self):
        """Update the button style based on the current theme."""
        if self.current_theme == "light":
            self.setText("🌞 Light")
            self.setStyleSheet("background-color: #FFD700; color: #000; font-size: 18px; font-family: Inter; border-radius: 10px;")
        else:
            self.setText("🌙 Dark")
            self.setStyleSheet("background-color: #2F4F4F; color: #FFF; font-size: 18px; font-family: Inter; border-radius: 10px;")
            
