from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных SQLite (вам может потребоваться другая база данных в зависимости от ваших потребностей)
engine = create_engine('sqlite:///tasks.db', echo=True)

# Создаем базовый класс для объявления моделей
Base = declarative_base()

# Определяем модель Task
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String)
    completed = Column(String(100), default='Not Completed')
    created = Column(DateTime, default=func.current_timestamp())

# Создаем таблицу в базе данных
Base.metadata.create_all(engine)

# Пример использования модели
Session = sessionmaker(bind=engine)
session = Session()

# Создаем новую задачу
new_task = Task(title='Sample Task', description='This is a sample task description.')
session.add(new_task)
session.commit()

# Получаем все задачи из базы данных
tasks = session.query(Task).all()

# Выводим информацию о задачах
for task in tasks:
    print(f"Task ID: {task.id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}, Created: {task.created}")
