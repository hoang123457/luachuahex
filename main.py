import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import shutil
import os

# Đường dẫn đến các tệp assets
ASSETS_DIR = "assets"
FILES = {
    "aimlock": os.path.join(ASSETS_DIR, "data2.hex"),
    "aimbot": os.path.join(ASSETS_DIR, "dat3.hex"),
    "bypass": os.path.join(ASSETS_DIR, "data.hex"),
}

class MainApp(App):
    def build(self):
        # Tạo giao diện chính
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Thêm nhãn tiêu đề
        title = Label(text='MENU VO HUY HOANG NO.1', font_size=24, size_hint=(1, 0.2))
        layout.add_widget(title)

        # Tạo các nút và liên kết sự kiện
        button1 = Button(text='Aimlock - On', on_press=self.copy_aimlock, size_hint=(1, 0.2))
        button2 = Button(text='Aimbot - On', on_press=self.copy_aimbot, size_hint=(1, 0.2))
        button3 = Button(text='Sensitivity - On', on_press=self.copy_bypass, size_hint=(1, 0.2))

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        return layout

    def show_message(self, title, message):
        # Hiển thị thông báo
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

    def copy_file(self, src, dst):
        try:
            # Kiểm tra xem đường dẫn đích có tồn tại không, nếu không thì tạo
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            
            # Sao chép tệp từ assets sang đích
            shutil.copy(src, dst)
            self.show_message("Success", f"Copied {os.path.basename(src)} to {dst}")
        except Exception as e:
            self.show_message("Error", str(e))

    def copy_aimlock(self, instance):
        self.copy_file(FILES["aimlock"], "/storage/emulated/0/Android/data/com.dts.freefireth/files/ilecpp/Metadata")

    def copy_aimbot(self, instance):
        self.copy_file(FILES["aimbot"], "/storage/emulated/0/Android/data/com.dts.freefireth/files/ilecpp/Metadata")

    def copy_bypass(self, instance):
        self.copy_file(FILES["bypass"], "//storage/emulated/0/Android/data/com.dts.freefireth/files/ilecpp/Metadata")

if __name__ == '__main__':
    MainApp().run()
