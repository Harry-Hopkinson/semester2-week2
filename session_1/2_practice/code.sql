-- Enable readable output format
.mode columns
.headers on

-- List all loans (book title, member name and loan date)
SELECT Books.Title AS BookTitle, Members.Name AS MemberName, Loans.Loan_Date
FROM
Loans JOIN Books
ON Loans.Book_ID = Books.ID
JOIN Members
ON Loans.Member_ID = Members.ID
ORDER BY Loans.Loan_Date;

-- List all books and any loans associated with them
SELECT Books.Title AS BookTitle, Members.Name AS MemberName, Loans.Loan_Date
FROM
Books LEFT JOIN Loans
ON Books.ID = Loans.Book_ID
LEFT JOIN Members
ON Loans.Member_ID = Members.ID
ORDER BY Books.Title;

-- List all library branches and the books that they hold
SELECT LibraryBranch.Name AS BranchName, Books.Title AS BookTitle
FROM
LibraryBranch LEFT JOIN Books
ON LibraryBranch.ID = Books.Branch_ID
LEFT JOIN Books
ON Books.Book_ID = Books.ID
ORDER BY LibraryBranch.Name;