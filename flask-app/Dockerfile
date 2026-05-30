FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Remove unnecessary packages that carry HIGH/CRITICAL vulns
RUN apt-get purge -y --allow-remove-essential --auto-remove perl-base ncurses-bin ncurses-base \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5000
CMD ["python", "app.py"]