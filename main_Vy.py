import sys
from PyQt6 import QtWidgets
from giaodien import *   # import giao diện.py đã dịch

# game data
secret_word = "Titanic" # Từ khóa
hints = [
    "Hint 1: The director is James Cameron",
    "Hint 2: The OST is 'The Heart Will Go On'",
    "Hint 3: It's a movie about a big ship that sank in 1912"
] # List hint để gợi ý từ khóa
current_hint = 0 #hint đầu tiên hiện trong giao diện ở vị trí 0 trong list

def main():
    # kết nối các button ở trong giao diện Qt designer
    form.ok.clicked.connect(kiem_tra) # Nút ok sẽ được kích hoạt bằng cú click và kết nối với hàm kiem_tra
    form.next.clicked.connect(hint_tiep) # Nút next được kích hoạt bằng cú click và kết nối với hàm hint_tiep
    form.end.clicked.connect(ket_thuc)# Nút end được kích hoạt bằng cú click và kết nối với hàm ket_thuc
    # Hiện được hiển thị đầu tiên
    form.hint.setPlainText(hints[0])
    #Gán cho trạng thái kết quả lúc chưa bắt đầu trò chơi là " Let's start guessing"
    form.textBrowser_2.setPlainText("Let's start guessing!")

def kiem_tra():
    global current_hint # thông báo cho python là mình đang dùng biến ngoài hàm, ko cần phải khởi tại lại trong hàm hiện tại
    ans = form.answer.text() # nhập answer vào
    if ans.lower() == secret_word.lower(): # Biến đầu vào thành chữa thường hết

        form.textBrowser_2.setPlainText("Correct!") #nếu người chơi đoán đúng thì gán vào ô TextBrowser_ là "Correct"
        tat_nut() # sau khi chiến thắng các nút sẽ bị vô hiệu hóa
    else: # nếu answer != secret_word
        if current_hint == len(hints) - 1: # thứ tự current_word bằng với thứ tự hint cuối cùng
            form.textBrowser_2.setPlainText("Fail! The answer is Titanic.")# Ô kết quả hiện thị "Fail! The answer is Titanic."
            tat_nut() # sau 3 lần đoán, các nút bị vô hiệu hóa
        else:# Nếu thứ tự của current_word bé hơn thứ tự của hint cuối cùng
            form.textBrowser_2.setPlainText("Incorrect! Try again or get another hint.") # Người chơi được đoán tiếp

def hint_tiep():
    global current_hint # thông báo cho python là mình đang dùng biến ngoài hàm, ko cần phải khởi tại lại trong hàm hiện tại
    if current_hint < len(hints) - 1: # thứ tự current_word bằng với thứ tự hint cuối cùng
        current_hint += 1 # Tăng thứ tự
        # Thêm new hint nhưng vẫn giữ hint cũ
        old = form.hint.toPlainText()
        form.hint.setPlainText(old + "\n" + hints[current_hint])
        form.answer.clear() # Xóa từ vừa điền
        form.textBrowser_2.clear() # Xóa trạng thái vừa điền
    else:
        form.next.setEnabled(False)
        form.textBrowser_2.setPlainText("No more hints!")

def tat_nut():
    form.ok.setEnabled(False)
    form.next.setEnabled(False)
    form.answer.setEnabled(False)

def ket_thuc():
    QtWidgets.QApplication.quit()

# ---- start app ----
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    form = Ui_MainWindow()            # class come from  giaodien.py
    form.setupUi(window)
    window.show()
    main()
    app.exec())
