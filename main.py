import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainwindow import Ui_MainWindow
from game_logic import GameLogic

class MainGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Khởi tạo logic
        self.logic = GameLogic()

        # Kết nối nút
        self.ui.ok.clicked.connect(self.check_answer)
        self.ui.batdau.clicked.connect(self.start_game)
        self.ui.choilai.clicked.connect(self.start_game)  # chơi lại
        self.ui.thoat.clicked.connect(self.close)

        # Cập nhật điểm ban đầu
        self.ui.label.setText(f"Điểm: {self.logic.score}")

    def start_game(self):
        hint = self.logic.new_game()
        self.ui.ogoiy.setText(hint)
        self.ui.onhapdapan.setText("")
        self.ui.label.setText(f"Điểm: {self.logic.score}")

    def check_answer(self):
        ans = self.ui.onhapdapan.text()
        if self.logic.check_answer(ans):
            QMessageBox.information(self, "Kết quả", "Đúng rồi!")
            self.start_game()  # sang câu mới
        else:
            hint = self.logic.get_hint()
            self.ui.ogoiy.setText(hint)
            if hint == "Hết gợi ý rồi!":
                QMessageBox.warning(self, "Kết quả", "Bạn đã hết lượt! Nhấn Chơi lại để thử lại.")
            self.ui.label.setText(f"Điểm: {self.logic.score}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGame()
    window.show()
    sys.exit(app.exec())
