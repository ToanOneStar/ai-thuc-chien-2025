from openai import OpenAI
import os


# --- Cấu hình API ---
client = OpenAI(
    api_key="sk-iDourIEUAlwjyNfoMQm3DA",   # Thay bằng API key của bạn
    base_url="https://api.thucchien.ai"
)


# --- Đọc nội dung prompt từ file ---
with open("prompt.txt", "r", encoding="utf-8") as f:
    user_prompt = f.read().strip()


# --- Gửi prompt tới AI ---
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {"role": "user", "content": user_prompt}
    ]
)


# --- Lấy nội dung phản hồi ---
output_text = response.choices[0].message.content


# --- Ghi kết quả vào file ---
with open("responses.md", "w", encoding="utf-8") as f:
    f.write(output_text)


print("✅ Đã đọc prompt từ prompt.txt và lưu kết quả vào response.txt")

