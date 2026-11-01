# Ma Điện Hắc Diệm — Satan Dark Fantasy

Bản riêng dùng asset và nội dung Satan/dark fantasy, không ghi đè phiên bản Công giáo.

## Chạy
Node.js 20+: `npm ci`, sau đó `npm start`. Mở http://localhost:3000 và http://localhost:3000/admin. OBS Browser Source: http://localhost:3000/?obs=1, khung 1080×1920.

Bấm nút bật âm thanh trong trang để mở khóa audio. TTS dùng Web Speech API và giọng tiếng Việt có sẵn trong trình duyệt; không cần Python, model hoặc dịch vụ tổng hợp giọng trên server. Giọng cụ thể phụ thuộc trình duyệt và hệ điều hành.

Kết nối TikTok LIVE bằng username, link LIVE hoặc Room ID dạng số. Nếu link LIVE có `room_id`, ứng dụng dùng trực tiếp; nếu TikTok không phân giải được Room ID từ username, hãy nhập Room ID trực tiếp. Ứng dụng chỉ tự kết nối khi người vận hành nhập tài khoản hoặc đặt `TIKTOK_USER`.

Link LIVE mặc định là `https://www.tiktok.com/@locdo.vibes/live?enter_from_merge=share&enter_method=share_copy_link`. Trên màn hình chính, bấm **Phóng to khung hình** để phóng vừa toàn bộ sân khấu 9:16 vào cửa sổ; bấm lại hoặc nhấn `Esc` để thu nhỏ. Nút không hiện trong chế độ OBS (`?obs=1`).

## Bộ hình và chuyển đổi
- Nền ma điện obsidian với tượng Satan hư cấu, kính đỏ, ngai đá, lửa và thảm đỏ.
- Năm pose acolyte PNG trong suốt: đi trái/phải, hạ gối, quỳ và cúi đầu; dùng lại pose cúi đầu cho các key animation cũ để tương thích. Không phải tám frame chuyển động riêng.
- Toàn bộ hình Phật giáo/Công giáo đã được thay khỏi public/assets. Nhạc nền là pad tối tổng hợp mới, không có lời niệm hoặc bản thu đi mượn.
- Nút và nội dung: hắc nến, hắc chuông, khắc ấn, thẻ Hắc Ấn, hồng đen và sự kiện Hắc Hội. Thẻ là nội dung thế giới game, không phải bói toán dự đoán tương lai.
- Namespace RPC `temple.*`, event type, field `merit`, `fortune`, `woodenFish` được giữ để không làm đứt tích hợp. `merit` là điểm tương tác; coins là metadata quà TikTok.
- Nội dung TTS mặc định và ví dụ đã đổi theo chủ đề mới. Giọng đọc dùng Web Speech API; chất lượng và lựa chọn giọng phụ thuộc các giọng tiếng Việt được cài trên thiết bị.

Hình được tạo bằng công cụ tạo ảnh tích hợp. Prompt và danh mục trong docs/asset-manifest.json; asset-audit.json ghi kích thước và alpha. Hình là tài sản hư cấu dùng cho bối cảnh game/livestream. Tệp `tts_worker.py` cũ không còn được server sử dụng.

## Kiểm tra
`npm test`: asset HTTP, RPC, định tuyến bình luận, thẻ và WebSocket.
`node tests/browser.cjs`: desktop, mobile, OBS, 40 nhân vật, nút tương tác và admin. Cài bằng `npm install --no-save playwright` và `npx playwright install chromium` cho lệnh trình duyệt; có thể chỉ định CHROMIUM_PATH nếu có executable riêng. Script tự mở server test tại cổng 3144 rồi dừng.
Kết quả kiểm tra trình duyệt gần nhất trong docs/verification.json. Kết nối TikTok LIVE thật cần tài khoản đang phát công khai để xác minh trong môi trường tương ứng. Không chứa node_modules, cache, state người xem hoặc ảnh chụp kiểm thử.

Tạo lại nhạc nền: `python scripts/generate_ambience.py`.
