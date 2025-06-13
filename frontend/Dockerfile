# Используем официальный Node-образ
FROM node:20

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем оставшиеся исходники
COPY . .

# Экспонируем порт, который использует Vite (по умолчанию 5173)
EXPOSE 5173

# Запускаем dev-сервер Vite
CMD ["npx", "vite", "--host"]
