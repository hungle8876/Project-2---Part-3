CREATE TABLE IF NOT EXISTS Publisher (
    Publisher_name VARCHAR(100) PRIMARY KEY,
    Phone CHAR(12),
    Address VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Library_branch (
    Branch_Id INTEGER AUTO_INCREMENT PRIMARY KEY,
    Branch_name VARCHAR(100),
    Branch_address VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Borrower (
    Card_no INTEGER AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(100),
    Phone CHAR(12)
);

CREATE TABLE IF NOT EXISTS Book (
    Book_id INTEGER AUTO_INCREMENT,
    Title VARCHAR(100) NOT NULL,
    Publisher_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (Book_id),
    FOREIGN KEY (Publisher_name) REFERENCES Publisher(Publisher_name)
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Book_loans (
    Book_id INTEGER AUTO_INCREMENT,
    Branch_id INTEGER NOT NULL,
    Card_no INTEGER NOT NULL,
    Date_out DATE NOT NULL,
    Due_date DATE NOT NULL,
    Returned_date DATE,
    PRIMARY KEY (Book_id, Branch_id, Card_no),
    FOREIGN KEY (Book_id) REFERENCES Book(Book_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (Branch_id) REFERENCES Library_branch(Branch_Id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (Card_no) REFERENCES Borrower(Card_no)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Book_copies (
    Book_id INTEGER AUTO_INCREMENT,
    Branch_id INTEGER NOT NULL,
    No_of_copies INTEGER NOT NULL,
    PRIMARY KEY (Book_id, Branch_id),
    FOREIGN KEY (Book_id) REFERENCES Book(Book_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (Branch_id) REFERENCES Library_branch(Branch_Id)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Book_authors (
    Book_id INTEGER AUTO_INCREMENT,
    Author_name VARCHAR(100),
    PRIMARY KEY (Book_id, Author_name),
    FOREIGN KEY (Book_id) REFERENCES Book(Book_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);


.mode csv
.import Publisher.csv Publisher
.import Library_Branch.csv Library_branch
.import Borrower.csv Borrower
.import Book.csv Book
.import Book_Loans.csv Book_loans
.import Book_Copies.csv Book_copies
.import Book_Authors.csv Book_authors

.mode column 
.header on
---Query 1
ALTER TABLE Book_Loans
ADD COLUMN Late TINYINT DEFAULT 0;

SET SQL_SAFE_UPDATES = 0;

UPDATE Book_Loans
SET Late = 1
WHERE Returned_date > Due_date;	

UPDATE Book_Loans
SET Late = 0
WHERE Returned_date <= Due_date OR Returned_date IS NULL;

---Query 2
ALTER TABLE Library_Branch
ADD COLUMN LateFee DECIMAL(5,2);

SET SQL_SAFE_UPDATES = 0;

UPDATE Library_Branch
SET LateFee = 2.00;


---Query 3
CREATE VIEW vBookLoanInfo AS
SELECT bl.Card_no,
       b.Name AS 'Borrower Name',
       bl.Date_out,
       bl.Due_date,
       bl.Returned_date,
       DATEDIFF(IFNULL(bl.Returned_date, CURDATE()), bl.Date_out) AS 'TotalDays',
       bk.Title AS 'Book Title',
       IFNULL(DATEDIFF(bl.Returned_date, bl.Due_date), 0) AS 'LateDays',
       bl.Branch_id,
       IF(bl.Late = 1, DATEDIFF(bl.Returned_date, bl.Due_date) * lb.LateFee, 0) AS 'LateFeeBalance'
FROM Book_Loans bl
JOIN Borrower b ON bl.Card_no = b.Card_no
JOIN Book bk ON bl.Book_id = bk.Book_id
JOIN Library_Branch lb ON bl.Branch_id = lb.Branch_Id;



---Create Trigger for BOOK_COPIES
CREATE TRIGGER update_book_copies
AFTER UPDATE ON book_loans
FOR EACH ROW
WHEN NEW.Book_id IS NOT NULL AND NEW.Branch_id IS NOT NULL
BEGIN
    UPDATE book_copies
    SET No_of_copies = No_of_copies - 1
    WHERE Book_copies.Book_id = NEW.Book_id AND Book_copies.Branch_id = NEW.Branch_id;
END;

