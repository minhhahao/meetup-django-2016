CREATE DATABASE djangoblog;
CREATE USER 'minhha' @'localhost' IDENTIFIED BY 'haminh';
SELECT
  host,
  user,
  password,
  Grant_priv,
  Super_priv
FROM mysql.user;
UPDATE mysql.user
SET Grant_priv = 'Y', Super_priv = 'Y'
WHERE User = 'root';
FLUSH PRIVILEGES;