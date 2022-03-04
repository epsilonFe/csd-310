SELECT patrons.patron_id, patrons.first_name, patrons.last_name, book.book_id, book.book_name, book.author

FROM wishlist
    INNER JOIN patrons ON wishlist.patron_id = patrons.patron_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE patrons.patron_id = 1;

SELECT store_id, locale from store;

SELECT book_id, book_name, author, book_year from book;

SELECT book_id, book_name, author, book_year
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE patron_id = 1);

INSERT INTO wishlist(patron_id, book_id)
    VALUES(1, 9);

DELETE FROM wishlist WHERE patron_id = 1 AND book_id = 9;
