# 🧪 NamsoGen Clone – Trình tạo thẻ tín dụng ảo (BIN Generator)

NamsoGen Clone là một ứng dụng web viết bằng **Flask + HTML/CSS/JS**, cho phép người dùng sinh ngẫu nhiên **danh sách số thẻ tín dụng ảo** theo chuẩn Luhn, từ một BIN cụ thể.

> ✅ **Dùng để test và phát triển phần mềm – không dùng để giao dịch thật.**

---

## 🚀 Tính năng nổi bật

- ✅ Nhập **BIN** đầu vào (6–12 chữ số)
- ✅ Tùy chọn số lượng (1–1000)
- ✅ Tùy chọn thêm **ngày hết hạn (EXP)** và **mã bảo mật (CVV)**
- ✅ Giao diện đẹp, hỗ trợ **chế độ tối / sáng**
- ✅ Hiệu ứng **mưa rơi + cầu vồng cong khi tải trang**
- ✅ Kết quả có thể **sao chép hoặc tải về file TXT**
- ✅ Lưu lại lựa chọn chế độ nền bằng `localStorage`

---

## 🎥 Trải nghiệm giao diện

![Preview](https://user-images.githubusercontent.com/your-screenshot.png)

---
## 🖼 Cấu trúc dự án
namsogen-clone/
├── app.py              # Flask backend
├── luhn.py             # Thuật toán kiểm tra Luhn
├── templates/
│   └── index.html      # Giao diện HTML chính
├── static/
│   └── style.css       # (Tùy chọn) nếu tách CSS riêng
└── README.md


