import logging

# Создаем логгер
logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)  # Уровень логирования (можно изменить на INFO или ERROR)

# Создаем обработчик, который будет выводить логи в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Уровень логирования для консоли

# Создаем форматтер для вывода логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(console_handler)