import os
from PIL import Image

def convert_png_to_webp(folder_path):
    # 지정된 폴더와 모든 하위 폴더를 순회
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".png"):
                # png 파일의 전체 경로
                png_path = os.path.join(root, filename)
                
                # 새로운 webp 파일의 이름 (확장자만 변경)
                webp_filename = os.path.splitext(filename)[0] + ".webp"
                webp_path = os.path.join(root, webp_filename)
                
                try:
                    # 이미지 열기
                    with Image.open(png_path) as img:
                        # RGBA 모드인 경우 RGB로 변환
                        if img.mode == 'RGBA':
                            img = img.convert('RGB')
                        # webp로 저장 (품질 100으로 설정, 0-100 사이 값)
                        img.save(webp_path, "WEBP", quality=100)
                    print(f"변환 완료: {png_path} -> {webp_path}")
                    
                    # 변환 성공 후 원본 PNG 파일 삭제
                    os.remove(png_path)
                    print(f"원본 파일 삭제됨: {png_path}")
                    
                except Exception as e:
                    print(f"변환 실패 {png_path}: {str(e)}")

# 현재 스크립트 파일의 경로를 가져옵니다
current_path = os.path.dirname(os.path.abspath(__file__))
convert_png_to_webp(current_path)