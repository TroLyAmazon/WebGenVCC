# 🧪 NamsoGen Clone – Trình tạo thẻ tín dụng ảo (BIN Generator)

NamsoGen Clone là một ứng dụng web viết bằng **Flask + HTML/CSS/JS**, cho phép người dùng sinh ngẫu nhiên **danh sách số thẻ tín dụng ảo** theo chuẩn **Luhn**, từ một **BIN** cụ thể.

> ✅ **Chỉ sử dụng để kiểm thử phần mềm hoặc mục đích giáo dục – không dùng trong giao dịch thật.**

---

## 🚀 Tính năng nổi bật

* ✅ Nhập **BIN** đầu vào (6–12 chữ số)
* ✅ Tùy chọn số lượng sinh thẻ (1–1000)
* ✅ Tùy chọn kèm:
  * **Ngày hết hạn (EXP)** – tự chọn hoặc random
  * **Mã bảo mật (CVV)** – 3 chữ số
* ✅ Giao diện đẹp, hỗ trợ **chế độ tối / sáng**
* ✅ Hiệu ứng **mưa rơi** sinh động khi tải trang
* ✅ Giao tiếp bằng AJAX – logic sinh thẻ thực hiện hoàn toàn phía backend Flask
* ✅ Kết quả có thể sao chép hoặc tải về TXT
* ✅ Tự động ghi nhớ chế độ nền (dark/light) bằng `localStorage`

---

## 🆕 Cập nhật mới nhất (2025-08-31)

> ⚙️ **Bổ sung tính năng nhập ngày hết hạn tùy chỉnh (EXP):**

* Người dùng có thể nhập trực tiếp:
  * **MM** – Tháng (01–12)
  * **YY** – Năm (ví dụ: 25 cho 2025)
* Nếu để trống ➜ hệ thống tự random như trước
* Nếu chỉ nhập 1 phần (chỉ MM hoặc chỉ YY) ➜ phần còn lại sẽ random
* Năm luôn được ép **≥ năm hiện tại**

---

## 🎥 Trải nghiệm giao diện

> Giao diện đơn giản, dễ dùng – nhập thông tin, chọn tùy chọn và nhấn "Tạo thẻ".

![demo](https://i.imgur.com/placeholder.png) *(Thay ảnh nếu có)*

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

## 🛡️ Cảnh báo pháp lý

**❗ Tuyên bố miễn trừ trách nhiệm:**  
Toàn bộ dữ liệu thẻ sinh ra bởi công cụ này đều là **giả lập** – không liên kết với bất kỳ tài khoản thật nào.  
**Tuyệt đối không sử dụng vào các mục đích vi phạm pháp luật.**

---

## 📬 Liên hệ

📬 Telegram: [@IntermediaryTransactions](https://t.me/IntermediaryTransactions)

---

## 📄 License

MIT License – Dự án mở vì mục đích học tập.
