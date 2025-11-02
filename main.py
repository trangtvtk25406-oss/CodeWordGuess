import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtWidgets import QMainWindow
from mainwindow import Ui_MainWindow
import game_logic as gl  # Import file logic dưới dạng module

# Các hàm xử lý:

def start_game():
    """Bắt đầu trò chơi mới"""
    hint = gl.new_game()
    ui.ogoiy.setText(hint)
    ui.onhapdapan.setText("")
    ui.label.setText(f"Điểm: {gl.score}")

def check_answer():
    """Kiểm tra câu trả lời của người chơi"""
    ans = ui.onhapdapan.text()
    if gl.check_answer(ans):
        QMessageBox.information(window, "Kết quả", "Đúng rồi!")
        start_game()
    else:
        hint = gl.get_hint()
        ui.ogoiy.setText(hint)
        if hint == "Hết gợi ý rồi!":
            QMessageBox.warning(window, "Kết quả", "Bạn đã hết lượt! Nhấn Chơi lại để thử lại.")
        ui.label.setText(f"Điểm: {gl.score}")

def thoat_game():
    window.close()

#Chạy chương trình:
app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

# Gắn sự kiện cho các nút:
ui.batdau.clicked.connect(start_game)
ui.choilai.clicked.connect(start_game)
ui.ok.clicked.connect(check_answer)
ui.thoat.clicked.connect(thoat_game)

# Cập nhật điểm ban đầu:
ui.label.setText(f"Điểm: {gl.score}")

window.show()
sys.exit(app.exec())
