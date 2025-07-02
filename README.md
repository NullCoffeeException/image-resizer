# Image Resizer

&nbsp;이미지를 올린 후 사이즈를 변경하여 다운로드할 수 있는 간단한 윈도우 GUI 프로그램입니다.
&nbsp;Python 기반으로, CustomTkinter와 Pillow를 사용하여 제작되었습니다.

<br>

---

## 사용 방법

1. 화면 우측 상단의 '찾기' 버튼을 클릭한 후, 이미지 파일을 선택합니다.
2. 사이즈를 선택합니다.
3. 우측 하단의 '다운로드' 버튼을 클릭하고, 파일 이름을 입력한 후 저장합니다.

<br>

---

## 설치 방법

1. release 폴더 안에 있는 image-resizer.exe 파일을 실행하여 바로 사용이 가능합니다.
2. 또는 pyinstaller로 직접 빌드하여 사용이 가능합니다. 아래 코드를 참조해 주세요.

```bash
# 의존성 설치
pip install -r requirements.txt
pip install pyinstaller

# 선택 1
pyinstaller image-resizer.spec

# 선택 2
pyinstaller main.py
```
