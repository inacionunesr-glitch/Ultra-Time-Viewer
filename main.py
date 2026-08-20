from MainWindow import App
from pathlib import Path
import sys

base_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
icon_path = base_dir / "icon.ico"

window = App()
window.set_icon(icon_path)
window.run()