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

select * 
from users 
where id not in (
  select user_id from tasks
);

insert into tasks (title, description, user_id, status_id)
values ('new task', 'new task description', 1, 2);

select * 
from tasks 
where status_id != 3;

delete from tasks 
where id = 7;

select * 
from users 
where email like('%hnelson@example.net%');

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
where description is not null;

select * 
from users u
inner join tasks t on t.user_id = u.id
where t.status_id = 2;

select count(t) as total_tasks, u.id, u.email, u.fullname
from users u
left join tasks t on t.user_id = u.id
group by u.id;
