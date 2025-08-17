USE alx_book_store;

SELECT
    book_id ,
    title ,
    author_id ,
    price DOUBLE ,
    publication_date  
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'Books';
    B
