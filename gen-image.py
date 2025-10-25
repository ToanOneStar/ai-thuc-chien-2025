from openai import OpenAI
import base64
import os
from datetime import datetime


# --- Cấu hình ---
client = OpenAI(
    api_key="sk-iDourIEUAlwjyNfoMQm3DA",
    base_url="https://api.thucchien.ai"
)


# --- Tạo thư mục "image" nếu chưa có ---
os.makedirs("image", exist_ok=True)
with open("prompt.txt", "r", encoding="utf-8") as f:
    user_prompt = f.read().strip()

# --- Gửi yêu cầu tạo hình ảnh ---
response = client.chat.completions.create(
    model="gemini-2.5-flash-image-preview",
    messages=[{"role": "user", "content": user_prompt}],
    modalities=["image"]
)


# --- Lấy dữ liệu ảnh base64 ---
image_info = response.choices[0].message.images[0]
base64_string = image_info.get("b64_json") or image_info.get("image_url", {}).get("url", "")


if not base64_string:
    raise ValueError("❌ Không nhận được dữ liệu hình ảnh từ API.")


# --- Giải mã và lưu ---
# Nếu chuỗi có dạng "data:image/png;base64,...." thì cắt bỏ phần đầu
if ',' in base64_string:
    _, encoded = base64_string.split(',', 1)
else:
    encoded = base64_string


image_data = base64.b64decode(encoded)


# Tạo tên file theo thời gian
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
save_path = f"image/generated_{timestamp}.png"


with open(save_path, "wb") as f:
    f.write(image_data)


print(f"✅ Image saved to {save_path}")



