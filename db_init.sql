alter table if exists employees
drop constraint if exists fk_supervisor;

alter table if exists departments
drop constraint if exists fk_head;

drop table if exists reimbursements;
drop table if exists employees;
drop table if exists courses;
drop table if exists roles;
drop table if exists grading_formats;
drop table if exists reimbursement_status;
drop table if exists course_types;
drop table if exists departments;


create table employees(id serial primary key,
					   first_name varchar(50) not null,
					   last_name varchar(50) not null,
					   login_id varchar(50) unique not null,
					   department_id int not null,
					   role_id int not null,
					   supervisor_id int);
create table course_types(id serial primary key,
						  "name" varchar(50) not null,
						  reimbursement_percent decimal not null);
create table courses(id serial primary key,
					 "name" varchar(100) not null,
					 "type_id" int not null,
					 start_date date not null,
					 end_date date not null,
					 grading_format_id int not null,
					 "cost" decimal not null);
create table roles(id serial primary key,
				   "name" varchar(50) not null);
create table departments(id serial primary key,
						 "name" varchar(50) not null,
						 head_employee_id int);
create table reimbursements(id serial primary key,
							employee_id int not null,
							status_id int not null,
							date_submitted date not null,
							course_id int not null,
							amount decimal not null,
							message varchar(250) not null default '');
create table grading_formats(id serial primary key,
							 "type" varchar(50) not null,
							 requires_presentation bool not null);
create table reimbursement_status (id serial primary key,
								   "name" varchar(50) not null);


insert into roles ("name") values
				  ('Professor'),
				  ('Assistant Professor'),
				  ('Custodian'),
				  ('Benifits Coordinator'),
				  ('Unassigned');
insert into reimbursement_status("name") values
								('Unfinished'),
								('Pending Supervisor Approval'),
								('Pending Department Approval'),
								('Pending BenCo Approval'),
								('Awaiting Grade/Presentation Submission'),
								('Approved'),
								('Denied'),
								('More info needed');
insert into course_types("name", reimbursement_percent) values
				  		('University', 0.8),
				  		('Seminar', 0.6),
				  		('Certification Preparation', 0.75),
				  		('Certification', 1),
				  		('Technical Training', 0.9),
				  		('Other', 0.3);
insert into courses  (type_id, grading_format_id, end_date, start_date, "name", "cost") values
					 (1, 1, now(), now(), 'Cooking 101', 1000),
					 (1, 1, now(), now(), 'Ball Chasing 101', 1000),
					 (1, 1, now(), now(), 'Database Design: 7th Normal Form', 1000),
					 (1, 1, now(), now(), 'Music Theory: Why is is not Music Law?', 1000);
insert into departments ("name", head_employee_id) values
						('Science', null),
						('Math', null),
						('History', null),
						('Information Technology', null),
						('Art', null),
						('Administration', null);
insert into grading_formats ("type", requires_presentation) values
						  	('Percentage', false),
						  	('Letter', false),
						  	('Norm-Reference', false),
						  	('Pass/Fail', false),
						  	('Mastery', false),
						  	('Standards', true),
						  	('Narrative', true),
						  	('Other', true);
insert into employees (first_name, last_name, login_id, department_id, role_id, supervisor_id) values
					  ('Jim', 'Jimmy', '100000', 1, 1, null),
					  ('Sam', 'Sammy', '100001', 2, 1, null),
					  ('Tom', 'Tommy', '100002', 3, 1, null),
					  ('Beth', 'Bethany', '100003', 4, 1, null),
					  ('Jeff', 'Jefferson', '100004', 1, 2, 1),
					  ('Wash', 'Washington', '100005', 2, 2, 2),
					  ('Carp', 'Carpenter', '100006', 3, 2, 3),
					  ('Zach', 'Zachary', '100007', 2, 2, 4);
insert into reimbursements (employee_id, status_id, course_id, date_submitted, amount) values
								  (1, 1, 1, now(), 0),
								  (1, 1, 1, now(), 0),
								  (1, 1, 1, now(), 0);

update departments set head_employee_id = 1 where id=1;


alter table employees
add constraint fk_department
foreign key (department_id)
references departments(id)
on delete set null;

alter table employees
add constraint fk_role
foreign key (role_id)
references roles(id);

alter table employees
add constraint fk_supervisor
foreign key (supervisor_id)
references employees(id)
on delete set null;

alter table courses
add constraint fk_type
foreign key (type_id)
references course_types(id);

alter table courses
add constraint fk_grading
foreign key (grading_format_id)
references grading_formats(id);

alter table departments
add constraint fk_head
foreign key (head_employee_id)
references employees(id)
on delete set null;

alter table reimbursements
add constraint fk_employee
foreign key (employee_id)
references employees(id);

alter table reimbursements
add constraint fk_status
foreign key (status_id)
references reimbursement_status(id);

alter table reimbursements
add constraint fk_course
foreign key (course_id)
references courses(id);
