SELECT * FROM whims.users;

SET SQL_SAFE_UPDATES=0;
DELETE FROM whims.users WHERE (username='123' AND password='123');
SET SQL_SAFE_UPDATES=1;