import pandas as pd
from sklearn.ensemble import IsolationForest
import os
from dotenv import load_dotenv

# Load cấu hình từ file .env
load_dotenv()
MY_API_KEY = os.getenv("API_KEY")

class BaiTapLon:
    def __init__(self):
        print("--- CHƯƠNG TRÌNH BÀI TẬP LỚN KHDLAI ---")
        
    # --- PHẦN 1: CODE CƠ BẢN ---
    def tinh_giai_thua(self, n):
        return 1 if (n == 1 or n == 0) else n * self.tinh_giai_thua(n - 1)

    def tinh_loi_nhuan(self, P, r, n=12):
        # Công thức lãi kép: $A = P \times (1 + r)^n$
        A = P * (1 + r)**n
        return A - P

    # --- PHẦN 2: PHÁT HIỆN BẤT THƯỜNG ---
    def thuc_hien_anomaly_detection(self, file_path):
        print(f"\n[Đang phân tích dữ liệu: {file_path}]")
        df = pd.read_csv(file_path)
        
        # Dùng Isolation Forest
        model = IsolationForest(contamination=0.05, random_state=42)
        df['anomaly'] = model.fit_predict(df[['Amount']])
        
        # Đánh giá: Lọc ra các giao dịch bị nghi ngờ (-1)
        anomalies = df[df['anomaly'] == -1]
        print(f"-> Phát hiện {len(anomalies)} giao dịch bất thường!")
        print(anomalies[['TransactionID', 'Amount', 'Merchant']].head())
        return df

# --- CHƯƠNG TRÌNH CHÍNH ---
if __name__ == "__main__":
    app = BaiTapLon()
    
    while True:
        print("\nMENU THỰC THI:")
        print("1. Chạy các bài Python cơ bản (Giai thừa, Lợi nhuận)")
        print("2. Chạy Mô hình Phát hiện giao dịch bất thường")
        print("3. Thoát")
        
        chon = input("Chọn số (1-3): ")
        
        if chon == '1':
            n = int(input("Nhập số tính giai thừa: "))
            print(f"Giai thừa {n} là: {app.tinh_giai_thua(n)}")
            print(f"Lợi nhuận sau 12 tháng (vốn 10tr, lãi 1%/tháng): {app.tinh_loi_nhuan(10000000, 0.01):,.0f} VNĐ")
            
        elif chon == '2':
            # Đường dẫn file CSV của bạn
            path = "financial_anomaly_data.csv" 
            app.thuc_hien_anomaly_detection(path)
            
        elif chon == '3':
            break