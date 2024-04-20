drop table if exists users;
create table users (
	id SERIAL primary key,
	fullname VARCHAR(100) not NULL,
	email VARCHAR(100) UNIQUE
);

drop table if exists status;
create table status (
	id SERIAL primary key,
	name VARCHAR(50) UNIQUE
);

drop table if exists tasks;
create table tasks (
	id SERIAL primary key,
	title VARCHAR(100) not null,
	description TEXT not null,
	status_id INTEGER references status(id)
		on delete cascade,
	user_id INTEGER references users(id)
		on delete cascade
);