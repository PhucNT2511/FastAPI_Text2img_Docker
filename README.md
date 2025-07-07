# 🚀 FastAPI Docker README

🐳 Cách build Docker image:
Từ thư mục gốc (nơi chứa thư mục FastAPI_Docker), mở terminal hoặc PowerShell và chạy:
```
docker build -t fastapi-docker .\FastAPI_Docker\ 
```
Ghi chú:
- -t fastapi-docker: đặt tên image là fastapi-docker
- .\FastAPI_Docker\: trỏ đến thư mục chứa Dockerfile

🚀 Cách chạy container:
```
docker run --gpus all -p 7860:7860 fastapi-docker 
```
Trong đó:
- -p 7860:7860: ánh xạ cổng 7860 giữa máy host và container
- -it: bật chế độ interactive, hiện log

🌐 Truy cập API:
Mở trình duyệt truy cập:
- Swagger UI: http://localhost:7860/docs
- Redoc UI:   http://localhost:7860
