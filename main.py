import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkImage
from tkinter import filedialog
from PIL import Image

# 테마 세팅
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# 창 설정
root = ctk.CTk()
root.title("Image Resizer")
root.geometry("900x600")


# 전역변수
loaded_image = None
loaded_image_path = tk.StringVar()
loaded_image_width = None
loaded_image_height = None
image_preview = None
scale_var = tk.StringVar(value="0.5")
original_size_var = tk.StringVar(value="원본 사이즈 : - x -")
resized_size_var = tk.StringVar(value="변경 후 사이즈 : - x -")


# 변경 후 사이즈 계산 함수
def update_resized_label(*args):
    if loaded_image_width is None or loaded_image_height is None:
        resized_size_var.set("변경 후 사이즈 : - x -")
        return

    try:
        scale = float(scale_var.get())
        resized_width = int(loaded_image_width * scale)
        resized_height = int(loaded_image_height * scale)
        resized_size_var.set(f"변경 후 사이즈 : {resized_width} x {resized_height} px")
    except:
        resized_size_var.set("변경 후 사이즈 : - x -")

scale_var.trace_add("write", update_resized_label)


# 이미지 파일 선택 함수
def select_file():
    global loaded_image, loaded_image_width, loaded_image_height

    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    if file_path:
        # 파일명 추출
        filename = file_path.split("/")[-1]
        label_file_display.configure(text=filename)

        # 이미지 로딩
        try:
            loaded_image = Image.open(file_path)
            loaded_image_path.set(filename)
            loaded_image_width = loaded_image.size[0]
            loaded_image_height = loaded_image.size[1]
            original_size_var.set(f"원본 사이즈 : {loaded_image_width} x {loaded_image_height} px")
            update_resized_label()
            pre_img = loaded_image.copy()
            image_preview = CTkImage(dark_image=pre_img, size=(min(500, loaded_image_width), min(500, loaded_image_height)))
            label_image.configure(image=image_preview)

        except:
            label_file_display.configure(text="이미지 로딩 실패")


# 변경 이미지 다운로드 함수
def download_resized_image():
    global loaded_image

    if loaded_image is None:
        return
    
    try:
        scale = float(scale_var.get())
        resized_width = int(loaded_image_width * scale)
        resized_height = int(loaded_image_height * scale)
        resized_image = loaded_image.resize((resized_width, resized_height), Image.LANCZOS)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG 이미지", "*.png"), ("JPEG 이미지", "*.jpg"), ("모든 파일", "*.*")]
        )

        if save_path:
            resized_image.save(save_path)
    except:
        print()



# grid
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)


# 레이아웃
left_frame = ctk.CTkFrame(root)
left_frame.grid(row=0, column=0, sticky="nsew")

right_frame = ctk.CTkFrame(root, fg_color="#222222")
right_frame.grid(row=0, column=1, sticky="nsew")


# 좌측 프레임

label_image = ctk.CTkLabel(left_frame, text="")
label_image.pack(expand=True)


# 우측 프레임 grid
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)
right_frame.rowconfigure(1, weight=2)
right_frame.rowconfigure(2, weight=5)
right_frame.rowconfigure(3, weight=1)
right_frame.rowconfigure(4, weight=1)
right_frame.rowconfigure(5, weight=1)
right_frame.rowconfigure(6, weight=1)
right_frame.rowconfigure(7, weight=1)
right_frame.rowconfigure(8, weight=3)
right_frame.rowconfigure(9, weight=1)
right_frame.rowconfigure(10, weight=1)
right_frame.rowconfigure(11, weight=10)


# 우측 프레임
label_file_selection = ctk.CTkLabel(right_frame, text="파일 선택")
label_file_selection.grid(row=0, column=0, sticky="sw", padx=30, pady = 10)

label_file_display = ctk.CTkLabel(right_frame, text="", text_color="black", fg_color="white")
label_file_display.grid(row=1, column=0, sticky="new", padx=30, pady = 10)

button_file_selection = ctk.CTkButton(right_frame, text="찾기", command=select_file)
button_file_selection.grid(row=2, column=0, sticky="ne", padx = 20)

label_size_selection = ctk.CTkLabel(right_frame, text="사이즈 선택")
label_size_selection.grid(row=3, column=0, sticky="sw", padx=30, pady=20)

# 라디오 버튼
radio1 = ctk.CTkRadioButton(right_frame, text="0.5x", variable=scale_var, value="0.5")
radio1.grid(row=4, column=0, sticky="w", padx=40, pady=5)

radio2 = ctk.CTkRadioButton(right_frame, text="1.5x", variable=scale_var, value="1.5")
radio2.grid(row=5, column=0, sticky="w", padx=40, pady=5)

radio3 = ctk.CTkRadioButton(right_frame, text="2.0x", variable=scale_var, value="2.0")
radio3.grid(row=6, column=0, sticky="w", padx=40, pady=5)

radio4 = ctk.CTkRadioButton(right_frame, text="3.0x", variable=scale_var, value="3.0")
radio4.grid(row=7, column=0, sticky="w", padx=40, pady=5)

label_original_size = ctk.CTkLabel(right_frame, textvariable=original_size_var)
label_original_size.grid(row=9, column=0, sticky="sw", padx=40, pady=10)

label_resized_size = ctk.CTkLabel(right_frame, textvariable=resized_size_var)
label_resized_size.grid(row=10, column=0, sticky="nw", padx=40)

# 다운로드
button_download = ctk.CTkButton(right_frame, text="다운로드", command=download_resized_image)
button_download.grid(row=11, column=0, sticky="ne", padx = 20, pady=40)

root.mainloop()