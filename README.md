<h2>Описание</h2>
<p>Приложение для управления библиотекой с использованием асинхронного Python и SQLAlchemy. Вы можете добавлять авторов, жанры и книги, а также просматривать и удалять книги через терминал.</p>

<hr>

<h2>Установка и запуск проекта</h2>

<h3>1. Склонируйте репозиторий</h3>
<pre><code>$ git clone &lt;URL репозитория&gt;



<h3>2. Создайте виртуальное окружение</h3>
<pre><code>$ python -m venv venv</code></pre>

<h3>3. Активируйте виртуальное окружение</h3>
<ul>
    <li><strong>Windows:</strong>
        <pre><code>$ venv\Scripts\activate</code></pre>
    </li>
    <li><strong>macOS/Linux:</strong>
        <pre><code>$ source venv/bin/activate</code></pre>
    </li>
</ul>

<h3>4. Установите зависимости</h3>
<pre><code>$ pip install -r requirements.txt</code></pre>

<h3>5. Запустите проект</h3>
<p>Для запуска выполните следующую команду в терминале:</p>
<pre><code>$ python main.py</code></pre>

<hr>

<h2>Функциональность</h2>
<p>После запуска программы вы увидите меню, где можно выбрать действия:</p>
<ol>
    <li><strong>Добавить автора</strong>
        <ul>
            <li>Введите имя автора.</li>
        </ul>
    </li>
    <li><strong>Добавить жанр</strong>
        <ul>
            <li>Введите название жанра.</li>
        </ul>
    </li>
    <li><strong>Добавить книгу</strong>
        <ul>
            <li>Введите название книги.</li>
            <li>Укажите ID автора.</li>
            <li>Укажите ID жанра.</li>
        </ul>
    </li>
    <li><strong>Получить список книг</strong>
        <ul>
            <li>Выводит все книги с их авторами и жанрами.</li>
        </ul>
    </li>
    <li><strong>Получить книгу по ID</strong>
        <ul>
            <li>Введите ID книги, чтобы получить подробную информацию.</li>
        </ul>
    </li>
    <li><strong>Удалить книгу</strong>
        <ul>
            <li>Укажите ID книги для удаления.</li>
        </ul>
    </li>
    <li><strong>Выйти</strong>
        <ul>
            <li>Завершить программу.</li>
        </ul>
    </li>
</ol>

<hr>

<h2>Структура проекта</h2>
<ul>
    <li><code>main.py</code> - основной файл для запуска программы.</li>
    <li><code>db/config.py</code> - конфигурация базы данных и подключение.</li>
    <li><code>db/models.py</code> - описание таблиц базы данных (Author, Genre, Book).</li>
</ul>

<hr>
