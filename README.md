# 🚀 FastAPI Docker README

🐳 Tạo Docker image:
Từ thư mục gốc (nơi chứa thư mục FastAPI_Text2img_Docker), mở terminal và chạy:
```
docker build -t fastapi_text2img_docker .\FastAPI_Text2img_Docker\ 
```
Ghi chú:
- -t fastapi_text2img_docker: đặt tên image là fastapi_text2img_docker
- .\FastAPI_Text2img_Docker\: trỏ đến thư mục chứa Dockerfile

🚀 Chạy container:
```
docker run --gpus all -p 7860:7860 fastapi_text2img_docker
```
Trong đó:
- -p 7860:7860: ánh xạ cổng 7860 giữa máy host và container
- -it: bật chế độ interactive, hiện log

🌐 Truy cập API:
Mở trình duyệt truy cập:
- Swagger UI: http://localhost:7860/docs
- Redoc UI:   http://localhost:7860
