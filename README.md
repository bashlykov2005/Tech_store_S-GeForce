### 🗺️ Описание:
<u>**TechStore S-GeForce**</u> -  Интернет-магазин компьютерных комплектующих с возможностью:  
- Управление контентом через админ-панель (CRUD для товаров, категорий)  
- Регистрация, авторизация и управление пользователями (включая создание/удаление аккаунта)  
- Личный кабинет пользователя (история заказов, избранное)  
- Корзина товаров (добавление/удаление, сохранение состояния, оформление заказа)  
- Система скидок на товары  
- Поиск и фильтрация товаров  
- Обратная связь с администратором (форма обратной связи)  
- Адаптивная верстка (до 320px, мобильная оптимизация)  
- Просмотр товаров (каталог, карточки товаров, пагинация)

### 🚀 Демо  
   [Главная страница](https://github.com/bashlykov2005/Tech_store_S-GeForce/blob/main/screenshots/127.0.0.1_8000_main.png)  
   [Каталог товаров](https://github.com/bashlykov2005/Tech_store_S-GeForce/blob/main/screenshots/127.0.0.1_8000_catalog_all__page=2.png)  
   [Профиль пользователя и корзина товаров](https://github.com/bashlykov2005/Tech_store_S-GeForce/blob/main/screenshots/127.0.0.1_8000_user_profile_.png)  
   [Обратная связь](https://github.com/bashlykov2005/Tech_store_S-GeForce/blob/main/screenshots/127.0.0.1_8000-feedback.png)  
   [Поиск товарв на сайте](https://github.com/bashlykov2005/Tech_store_S-GeForce/blob/main/screenshots/127.0.0.1_8000search__q=intel.png)
   
### 🔧 Технологии  
Backend: <u>**Django 4.2**</u>  
Frontend: <u>**HTML5, CSS3, Bootstrap 5. JavaScript**</u>  
База данных: <u>**SQLite3**</u>  
Дополнительно: <u>**Django Debug Toolbar**</u>  

### ⚙️ Установка и запуск

Клонируйте репозиторий:  
git clone https://github.com/bashlykov2005/Tech_store_S-GeForce.git  
cd Tech_store_S-GeForce 

Создайте и активируйте виртуальное окружение:  
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate    # Windows

Установите зависимости:  
pip install -r requirements.txt 

Примените миграции:  
python manage.py migrate  

Загрузите фикстуры:  
python manage.py loaddata fixtures/*.json 

Создайте суперпользователя:  
python manage.py createsuperuser  

Запустите сервер:  
python manage.py runserver  
http://127.0.0.1:8000/ 

### 📂 Структура проекта  
S-GeForce  
├─ app # корневая папка  
├─ carts          # карты товаров и др  
├─ feedback      # обратная связь  
├─ fixtures     # Исходные данные в формате JSON  
├─ goods             # файлы товаров  
├─ main             # главная страница  
├─ media             # Загружаемые файлы (изображения товаров  
├─ orders           # файлы заказов пользователя  
├─ static           # Статические файлы  
├─ templates        # Базовый шаблон  
└─ users            # файлы пользователя  
├─ db.sqlite3         # БД  
├─ manage.py          # Управление проектом  
├─ requirements.txt  # Зависимости   

### 🛠️ Особенности настройки 

Для работы с медиафайлами в settings.py добавьте:  
MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

Для статических файлов в режиме разработки:  
STATIC_URL = '/static/'  
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  


🤝 Как помочь проекту  
Форкните репозиторий  
Создайте ветку с новым функционалом (git checkout -b feature/AmazingFeature)  
Сделайте коммит изменений (git commit -m 'Add some AmazingFeature')  
Запушите изменения (git push origin feature/AmazingFeature)  
Откройте Pull Request
