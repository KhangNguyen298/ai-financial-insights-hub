import os
import psycopg2
from dotenv import load_dotenv

# 1. Nạp các biến môi trường từ file .env vào bộ nhớ RAM
load_dotenv()

def test_db_connection():
    try:
        # 2. Thiết lập đường truyền kết nối xuống PostgreSQL bằng Socket TCP/IP
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
        # 3. Tạo một con trỏ (Cursor) để ra lệnh cho DB
        cursor = connection.cursor()
        
        # 4. Chạy thử một câu lệnh SQL hỏi phiên bản hệ thống
        cursor.execute("SELECT version();")
        
        # 5. Hốt hàng dữ liệu đầu tiên trả về từ DB
        db_version = cursor.fetchone()
        
        print("\n==========================================")
        print("🎉 KẾT NỐI POSTGRESQL THÀNH CÔNG RỰC RỠ!")
        print(f"🤖 Phiên bản DB: {db_version[0]}")
        print("==========================================\n")
        
        # 6. Đóng kết nối giải phóng tài nguyên bộ nhớ RAM
        cursor.close()
        connection.close()
        
    except Exception as error:
        print("\n==========================================")
        print(f"❌ LỖI KẾT NỐI DATABASE RỒI BẠN ƠI: {error}")
        print("==========================================\n")

if __name__ == "__main__":
    test_db_connection()