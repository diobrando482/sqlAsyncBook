import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from db.config import engine, get_session
from db.models import Base, Book, Author, Genre


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_author(session: AsyncSession, name: str):
    author = Author(name=name)
    session.add(author)
    await session.commit()
    return author


async def add_genre(session: AsyncSession, name: str):
    genre = Genre(name=name)
    session.add(genre)
    await session.commit()
    return genre


async def add_book(session: AsyncSession, title: str, author_id: int, genre_id: int):
    book = Book(title=title, author_id=author_id, genre_id=genre_id)
    session.add(book)
    await session.commit()
    return book


async def get_books(session: AsyncSession):
    result = await session.execute(select(Book).options(joinedload(Book.author), joinedload(Book.genre)))
    return result.scalars().all()


async def get_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).where(Book.id == book_id).options(joinedload(Book.author), joinedload(Book.genre)))
    return result.scalar()


async def delete_book(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).where(Book.id == book_id))
    book = result.scalar()
    if book:
        await session.delete(book)
        await session.commit()
        return True
    return False


async def main_menu():
    async with get_session() as session:
        while True:
            print("\nМеню:")
            print("1. Добавить автора")
            print("2. Добавить жанр")
            print("3. Добавить книгу")
            print("4. Получить список книг")
            print("5. Получить книгу по ID")
            print("6. Удалить книгу")
            print("0. Выйти")

            choice = input("Выберите действие: ")

            match choice:
                case "1":
                    name = input("Введите имя автора: ")
                    author = await add_author(session, name)
                    print(f"Автор добавлен: {author.name} (ID: {author.id})")
                case "2":
                    name = input("Введите название жанра: ")
                    genre = await add_genre(session, name)
                    print(f"Жанр добавлен: {genre.name} (ID: {genre.id})")
                case "3":
                    title = input("Введите название книги: ")
                    author_id = int(input("Введите ID автора: "))
                    genre_id = int(input("Введите ID жанра: "))
                    try:
                        book = await add_book(session, title, author_id, genre_id)
                        print(f"Книга добавлена: {book.title} (ID: {book.id})")
                    except Exception as e:
                        print(f"Ошибка: {e}")
                case "4":
                    books = await get_books(session)
                    for book in books:
                        print(f"Книга: {book.title}, Автор: {book.author.name}, Жанр: {book.genre.name}")
                case "5":
                    book_id = int(input("Введите ID книги: "))
                    book = await get_book_by_id(session, book_id)
                    if book:
                        print(f"Книга: {book.title}, Автор: {book.author.name}, Жанр: {book.genre.name}")
                    else:
                        print("Книга не найдена.")
                case "6":
                    book_id = int(input("Введите ID книги: "))
                    success = await delete_book(session, book_id)
                    if success:
                        print("Книга удалена.")
                    else:
                        print("Книга не найдена.")
                case "0":
                    print("Выход из программы.")
                    break
                case _:
                    print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    asyncio.run(init_db())
    asyncio.run(main_menu())
