
FROM  ghcr.io/rachelos/py3.13.1:latest
# 安装系统依赖
WORKDIR /app

# ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
ENV PIP_INDEX_URL=https://mirrors.huaweicloud.com/repository/pypi/simple

# 复制Python依赖文件
# 复制后端代码
COPY . .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN rm -rf ./web_ui
RUN rm -rf db.db
COPY ./config.example.yaml  ./config.yaml
RUN chmod +x ./start.sh
# 安装 Firefox 及运行依赖，并为内置 geckodriver 添加执行权限
RUN apt-get update && apt-get install --no-install-recommends -y \
    firefox dbus-x11 libgtk-3-0 libx11-xcb1 libdbus-glib-1-2 libxt6 libxss1 libnss3 libasound2 fonts-liberation \
    || (apt-get install --no-install-recommends -y firefox-esr)
RUN chmod +x /app/driver/driver/geckodriver
# 暴露端口
EXPOSE 8001
# 启动命令
# CMD ["uvicorn", "web:app", "--host", "0.0.0.0", "--port", "8001"]
# CMD ["python", "main.py"]
CMD ["./start.sh"]