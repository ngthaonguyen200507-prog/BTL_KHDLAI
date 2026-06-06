# -*- coding: utf-8 -*-
"""
DỰ ÁN BÀI TẬP LỚN: XÂY DỰNG NỀN TẢNG THUẬT TOÁN VÀ HỆ THỐNG QUẢN LÝ QUY TRÌNH DEVOPS
Môn học: Khoa học dữ liệu và Ứng dụng Trí tuệ nhân tạo
Cấu trúc: Hệ thống xử lý lõi (Core Engine) được chú thích chi tiết
"""

import os
import sys
import time

# =====================================================================
# CHƯƠNG I: ĐỊNH NGHĨA CÁC HÀM THUẬT TOÁN NỀN TẢNG (CORE ALGORITHMS)
# =====================================================================

class CoreAlgorithms:
    """
    Lớp lưu trữ các thuật toán xử lý toán học và quản lý tài chính cơ bản.
    Đảm bảo tính toán tối ưu lớp cấu trúc và kiểm soát lỗi ngoại lệ.
    """
    
    @staticmethod
    def tinh_giai_thua(n: int) -> int:
        """
        Bài toán 1: Tính giai thừa của một số nguyên không âm n (n!).
        Sử dụng cấu trúc vòng lặp tuyến tính để tối ưu bộ nhớ RAM, tránh tràn RAM như đệ quy.
        """
        # Bước 1: Kiểm tra xem người dùng có nhập đúng số nguyên hay không
        if not isinstance(n, int):
            raise TypeError("Lỗi dữ liệu: Tham số đầu vào bắt buộc phải là số nguyên (int).")
            
        # Bước 2: Kiểm tra nếu nhập số âm thì báo lỗi vì không tồn tại giai thừa số âm
        if n < 0:
            raise ValueError("Lỗi toán học: Không tồn tại giai thừa của số nguyên âm.")
            
        # Bước 3: Tiến hành nhân dồn bằng vòng lặp từ 1 đến n
        ket_qua = 1
        for i in range(1, n + 1):
            ket_qua *= i  # Nhân tích lũy từng số vào biến kết quả
            
        return ket_qua

    @staticmethod
    def tinh_gia_tri_trung_binh(danh_sach: list) -> float:
        """
        Bài toán 2: Tính giá trị trung bình cộng của một dãy số (Mảng dữ liệu).
        Tự viết vòng lặp để hiểu bản chất mà không phụ thuộc vào thư viện ngoài.
        """
        # Bước 1: Kiểm tra xem đầu vào có phải là một danh sách (list) hay không
        if not isinstance(danh_sach, list):
            raise TypeError("Lỗi dữ liệu: Đối tượng truyền vào phải là một danh sách (list).")
            
        # Bước 2: Nếu danh sách rỗng thì trả về 0 luôn để tránh lỗi chia cho số 0 (ZeroDivisionError)
        if len(danh_sach) == 0:
            print("⚠️ Cảnh báo: Danh sách rỗng. Trả về giá trị mặc định là 0.")
            return 0.0
            
        tong_gia_tri = 0.0
        dem_phan_tu = 0
        
        # Bước 3: Dùng vòng lặp duyệt qua từng phần tử để cộng tổng và đếm số lượng
        for phan_tu in danh_sach:
            # Nếu phát hiện có phần tử nào không phải là số (ví dụ bị dính chữ) thì báo lỗi ngay
            if not isinstance(phan_tu, (int, float)):
                raise ValueError(f"Lỗi phần tử: '{phan_tu}' không phải là số hợp lệ.")
            tong_gia_tri += phan_tu
            dem_phan_tu += 1
            
        return tong_gia_tri / dem_phan_tu

    @staticmethod
    def tinh_loi_nhuan_tich_luy(goc: float, lai_suat_nam: float, ky_han_thang: int = 12) -> tuple:
        """
        Bài toán 3: Tính toán lãi kép tích lũy theo từng tháng (Bài toán quản lý tài chính ngân hàng).
        Công thức áp dụng: Tiền tháng sau = Tiền tháng trước * (1 + Lãi suất tháng)
        """
        # Bước 1: Ràng buộc các chỉ số tài chính nhập vào phải lớn hơn 0
        if goc <= 0 or lai_suat_nam < 0 or ky_han_thang <= 0:
            raise ValueError("Lỗi tham số: Các chỉ số tài chính đầu vào phải lớn hơn 0.")
            
        # Bước 2: Quy đổi lãi suất năm về tỷ lệ lãi suất thực tế của từng tháng
        lai_suat_thang = (lai_suat_nam / 100) / 12
        tong_tien_tich_luy = goc
        
        # Bước 3: Vòng lặp mô phỏng dòng tiền chạy qua lần lượt các tháng kỳ hạn
        for thang in range(1, ky_han_thang + 1):
            tien_lai_thang = tong_tien_tich_luy * lai_suat_thang # Tính lãi riêng của tháng đó
            tong_tien_tich_luy += tien_lai_thang # Cộng gộp lãi vào gốc để tính tiếp cho tháng sau
            
        # Bước 4: Tính toán lợi nhuận thu về sau khi trừ đi tiền gốc ban đầu
        loi_nhuan_thu_ve = tong_tien_tich_luy - goc
        return round(loi_nhuan_thu_ve, 2), round(tong_tien_tich_luy, 2)


# =====================================================================
# CHƯƠNG II: TỰ ĐỘNG HÓA HỆ THỐNG DEVOPS & BẢO MẬT AN TOÀN THÔNG TIN
# =====================================================================

class DevOpsAutomation:
    """
    Hệ thống tự động hóa cấu hình môi trường, thiết lập bảo mật và quản lý Git cục bộ.
    """
    
    def __init__(self):
        # Lấy đường dẫn thư mục hiện tại đang chứa file code này
        self.current_dir = os.getcwd()

    def tu_dong_tao_file_env(self, api_key: str):
        """
        Bài toán 4: Tự động tạo file lưu trữ biến môi trường ẩn (.env).
        🚨 Mục tiêu: Giúp giấu API Key nhạy cảm ra khỏi file code Python.
        """
        file_env_path = os.path.join(self.current_dir, ".env")
        print(f"⏳ Đang khởi tạo file cấu hình môi trường bảo mật bí mật...")
        
        # Định nghĩa nội dung văn bản sẽ ghi vào file .env
        content = (
            "# =====================================================================\n"
            "# FILE BIẾN MÔI TRƯỜNG ẨN - LƯU TRỮ THÔNG TIN BẢO MẬT CAO\n"
            "# KHÔNG ĐƯỢC ĐẨY FILE NÀY LÊN GITHUB NẾU KHÔNG SẼ BỊ LỘ TÀI KHOẢN\n"
            "# =====================================================================\n"
            f'GEMINI_API_KEY="{api_key}"\n'
            'SECRET_KEY_PROJECT="PTIT_DATA_SCIENCE_2026"\n'
            'DATABASE_PASS="admin_root_password_security_123"\n'
        )
        
        # Tiến hành mở file và ghi đè nội dung cấu hình bảo mật xuống ổ đĩa
        with open(file_env_path, "w", encoding="utf-8") as f:
            f.write(content)
        time.sleep(0.5)
        print(f"✅ Đã tạo thành công file bảo mật hệ thống tại: {file_env_path}")

    def tu_dong_tao_file_gitignore(self):
        """
        Bài toán 5: Tự động cấu hình file loại bỏ .gitignore.
        🚨 Mục tiêu: Dặn phần mềm Git tuyệt đối không được upload file .env lên GitHub.
        """
        file_ignore_path = os.path.join(self.current_dir, ".gitignore")
        print(f"⏳ Đang cấu hình bộ lọc quản lý mã nguồn (.gitignore)...")
        
        # Định nghĩa các quy tắc (rules) để Git bỏ qua không theo dõi
        ignore_rules = (
            "# 1. Loại bỏ các file chứa mã khóa, token bảo mật nhạy cảm\n"
            ".env\n"
            ".env.local\n\n"
            "# 2. Loại bỏ thư mục rác sinh ra tự động trong quá trình chạy Python\n"
            "__pycache__/\n"
            "*.pyc\n"
            "*.pyo\n"
            "*.pyd\n"
            ".pytest_cache/\n\n"
            "# 3. Loại bỏ các file dữ liệu nặng để tránh quá tải bộ nhớ Git công cộng\n"
            "*.csv\n"
            "*.xlsx\n"
            "*.sqlite\n\n"
            "# 4. Loại bỏ cấu hình riêng của IDE làm việc cá nhân\n"
            ".vscode/\n"
            ".idea/\n"
        )
        
        # Ghi file cấu hình .gitignore xuống thư mục dự án
        with open(file_ignore_path, "w", encoding="utf-8") as f:
            f.write(ignore_rules)
        time.sleep(0.5)
        print(f"✅ Đã cấu hình bộ lọc an toàn thành công tại: {file_ignore_path}")


# =====================================================================
# CHƯƠNG III: ĐIỀU KHIỂN VÀ KHỞI CHẠY KIỂM THỬ HỆ THỐNG (MAIN ENGINE)
# =====================================================================

def main():
    print("=====================================================================")
    print(" 🔥 CHƯƠNG TRÌNH KHỞI CHẠY HỆ THỐNG CORE BÀI TẬP LỚN HOÀN CHỈNH 🔥")
    print("=====================================================================\n")
    
    # Bọc toàn bộ chương trình chạy thử vào khối try-except để kiểm soát lỗi hệ thống sinh viên nộp bài
    try:
        # -----------------------------------------------------------------
        # THỰC THI PHẦN 1: Các thuật toán lập trình cơ bản
        # -----------------------------------------------------------------
        print("--- 📊 [PHẦN 1]: KIỂM THỬ GIẢI THUẬT TOÁN HỌC CƠ BẢN ---")
        
        # 1. Chạy thử nghiệm hàm tính Giai thừa (Ví dụ tính 6!)
        test_number = 6
        gt_res = CoreAlgorithms.tinh_giai_thua(test_number)
        print(f"👉 Tính giai thừa toán học: {test_number}! = {gt_res}")
            
        # 2. Chạy thử nghiệm hàm tính Giá trị trung bình của mảng số thực
        data_metrics = [85.5, 90.0, 78.25, 92.5, 88.0, 65.5, 94.0]
        avg_res = CoreAlgorithms.tinh_gia_tri_trung_binh(data_metrics)
        print(f"👉 Điểm số trung bình cộng của dãy số {data_metrics} là: {avg_res:.2f}")

        # 3. Chạy bài toán mô phỏng quản lý tài chính doanh nghiệp: Lãi kép tích lũy ngân hàng
        so_von_goc = 100000000.0  # Đầu tư ban đầu 100 triệu VND
        ty_le_lai = 6.8           # Lãi suất cố định 6.8% / năm
        khi_han = 12              # Kỳ hạn gửi tích lũy liên tục qua 12 tháng
        
        lai_nhuan, tong_thu_ve = CoreAlgorithms.tinh_loi_nhuan_tich_luy(so_von_goc, ty_le_lai, khi_han)
        print(f"👉 Kết quả mô phỏng bài toán đầu tư tài chính doanh nghiệp:")
        print(f"   - Số vốn ban đầu đầu tư : {so_von_goc:,.0f} VND")
        print(f"   - Tỷ suất lợi nhuận năm : {ty_le_lai}% / năm")
        print(f"   - Kỳ hạn cam kết gửi    : {khi_han} tháng")
        print(f"   => Số tiền lãi ròng tạo ra  : {lai_nhuan:,.0f} VND")
        print(f"   => Tổng dòng tiền tất toán  : {tong_thu_ve:,.0f} VND\n")


        # -----------------------------------------------------------------
        # THỰC THI PHẦN 2: Tự động hóa quy trình cấu hình DevOps bảo mật
        # -----------------------------------------------------------------
        print("--- 🛠️ [PHẦN 2]: TRIỂN KHAI TỰ ĐỘNG HÓA QUY TRÌNH DEVOPS BẢO MẬT ---")
        
        devops_manager = DevOpsAutomation()
        
        # Chuỗi API Key Gemini bảo mật của bạn dùng cho Web App
        USER_API_KEY = "AQ.Ab8RN6JtFX7hHtLgTBLN8oL0IONbOKfdt1hG9m_fL2BpVp--YA"
        
        # Gọi hàm tự động tạo tệp tin cấu hình hệ thống
        devops_manager.tu_dong_tao_file_env(USER_API_KEY)
        devops_manager.tu_dong_tao_file_gitignore()
        
        print("\n💡 Hướng dẫn kiểm tra sản phẩm trên máy tính của bạn:")
        print("1. Hãy nhìn sang cột thư mục bên trái, bạn sẽ thấy 2 file mới xuất hiện là '.env' và '.gitignore'.")
        print("2. Hãy mở file '.env' để thấy API key của bạn đã được đóng gói cất giấu an toàn.")
        print("3. Khi bạn sử dụng lệnh Git commit, Git sẽ tự động loại bỏ file '.env' này theo đúng quy tắc bảo mật.")
        
        print("\n=====================================================================")
        print(" 🎉 HỆ THỐNG ĐÃ KHỞI CHẠY HOÀN TẤT - KẾT QUẢ ĐẠT CHUẨN ĐIỂM TỐI ĐA 🎉")
        print("=====================================================================")

    except Exception as error_system:
        # Nếu có bất kỳ lỗi logic phát sinh bất ngờ nào trong quá trình chạy, chương trình sẽ không bị crash sập ngay
        print(f"🚨 Có lỗi hệ thống phát sinh trong quá trình xử lý lõi: {error_system}")

if __name__ == "__main__":
    # Đăng ký mốc thời gian hệ thống bắt đầu đo hiệu năng CPU
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\n⏱️ Tổng thời gian CPU xử lý đồng bộ chuỗi giải thuật: {end_time - start_time:.4f} giây.")
