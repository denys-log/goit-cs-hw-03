select * 
from tasks 
where user_id = 1;

select * 
from tasks 
where status_id = (
  select id from status where name = 'new'
);

update tasks 
set status_id = 3 
where id = 1;

SELECT * 
FROM users 
WHERE id NOT IN (
  SELECT DISTINCT user_id FROM tasks
);

insert into tasks (title, description, user_id, status_id)
values ('new task', 'new task description', 1, 2);

SELECT * 
FROM tasks 
WHERE status_id != (
  SELECT id FROM status WHERE name = 'completed'
);

delete from tasks 
where id = 7;

select * 
from users 
where email like('%@example.com%');

update users 
set fullname = 'John Rick' 
where id = 1;

select count(status_id) as total_status, status_id 
from tasks 
group by status_id;

select t.id, t.title, t.description, t.status_id, t.user_id, u.email
from tasks t 
join users u on u.id = t.user_id 
where u.email like('%@example.com');

select * 
from tasks 
where description is null OR description = '';

SELECT u.*, t.*
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;

