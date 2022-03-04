DROP USER IF EXISTS 'quebook_user'@'localhost';
CREATE USER 'quebook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'XkuELbuck0';
GRANT ALL PRIVILEGES ON quebook.* TO'quebook_user'@'localhost';

USE quebook;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS patrons;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    book_year   INT				NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE patrons (
    patron_id	INT				NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(patron_id)
);

CREATE TABLE wishlist (
    wishlist_id INT             NOT NULL    AUTO_INCREMENT,
    book_id     INT             NOT NULL,
    patron_id   INT             NOT NULL,
    PRIMARY KEY (wishlist_id),
	CONSTRAINT fk_book_id
    FOREIGN KEY (book_id)
		REFERENCES book(book_id),
    CONSTRAINT fk_patron_id
    FOREIGN KEY (patron_id)
        REFERENCES patrons(patron_id)
);

INSERT INTO store(locale)
    VALUES('5400 Queso Court, Zephyrhills, FL 33540');

INSERT INTO book(book_name, author, book_year)
    VALUES('Smart policies for workplace technologies', 'Lisa Guerin', '1964');
INSERT INTO book(book_name, author, book_year)
    VALUES('The Tangle Web', 'Michal Zalewski', '2012');
INSERT INTO book(book_name, author, book_year)
    VALUES('Security patterns in practice', 'Eduardo Fernandez', '2013');
INSERT INTO book(book_name, author, book_year)
    VALUES('Practical malware analysis', 'Michael Sikorski', '2012');
INSERT INTO book(book_name, author, book_year)
    VALUES('National security intelligence', 'Loch Johnson', '1942');
INSERT INTO book(book_name, author, book_year)
    VALUES('Managing information security', 'John Vacca', '2014');
INSERT INTO book(book_name, author, book_year)
    VALUES('Counterterrorism and cybersecurity', 'Newton Lee', '2015');
INSERT INTO book(book_name, author, book_year)
    VALUES('Certified Ethical Hacker', 'Matthew Walker', '2012');
INSERT INTO book(book_name, author, book_year)
    VALUES('Adaptive security management architecture', 'James Tiller', '2011');
INSERT INTO patrons(first_name, last_name)
    VALUES('John', 'Draper');
INSERT INTO patrons(first_name, last_name)
    VALUES('Kevin', 'Mitnick');
INSERT INTO patrons(first_name, last_name)
    VALUES('Gary', 'McKinnon');