# 🧪 NamsoGen Clone – Trình tạo thẻ tín dụng ảo (BIN Generator)

NamsoGen Clone là một ứng dụng web viết bằng **Flask + HTML/CSS/JS**, cho phép người dùng sinh ngẫu nhiên **danh sách số thẻ tín dụng ảo** theo chuẩn Luhn, từ một BIN cụ thể.

> ✅ **Dùng để test và phát triển phần mềm – không dùng để giao dịch thật.**

---

## 🚀 Tính năng nổi bật

* ✅ Nhập **BIN** đầu vào (6–12 chữ số)
* ✅ Tùy chọn số lượng (1–1000)
* ✅ Tùy chọn thêm **ngày hết hạn (EXP)** và **mã bảo mật (CVV)**
* ✅ Giao diện đẹp, hỗ trợ **chế độ tối / sáng**
* ✅ Hiệu ứng **mưa rơi + cầu vồng cong khi tải trang**
* ✅ Kết quả được sinh từ backend Flask (ẩn hoàn toàn logic)
* ✅ Có thể sao chép hoặc tải TXT danh sách thẻ
* ✅ Lưu lại chế độ nền bằng `localStorage`

---

## 🎥 Trải nghiệm giao diện

> Giao diện gửi dữ liệu qua AJAX và nhận JSON từ Flask – không hề lộ thuật toán sinh thẻ.

---

## 🖼 Cấu trúc dự án

```
WebGenVCC/
├── app.py
├── luhn.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css      
│   ├── script.js
│   └── duck.png
└── README.md

```

---

## 🛡️ Cảnh báo

**❗ Lưu ý:** Tất cả dữ liệu thẻ sinh ra là giả lập – **không liên kết với bất kỳ tài khoản thật nào**. Công cụ này chỉ dành cho mục đích **kiểm thử phần mềm, giáo dục, hoặc phát triển API thanh toán**.

---

## 📬 Liên hệ

📬 Telegram: [@IntermediaryTransactions](https://t.me/IntermediaryTransactions)

---

## 📄 License

MIT License – Đéo bt viết j
