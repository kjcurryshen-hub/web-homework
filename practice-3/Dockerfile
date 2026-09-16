FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir "notebook>=7,<8"
COPY hello.ipynb .
EXPOSE 8888
CMD ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
