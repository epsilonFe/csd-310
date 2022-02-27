DROP USER IF EXISTS 'quebook_user'@'localhost';
CREATE USER 'quebook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'XkuELbuck0';
GRANT ALL PRIVILEGES ON quebook.* TO'quebook_user'@'localhost';

USE quebook;

SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

SELECT store_id, locale from store;

SELECT book_id, book_name, author, book_year from book;

SELECT book_id, book_name, author, book_year
FROM book
WHERE book_id IN (SELECT book_id FROM wishlist WHERE user_id = 1);

INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9)

DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;