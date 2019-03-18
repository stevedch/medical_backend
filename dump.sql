-- INSERT TABLE ROLE

INSERT INTO public.role (id, name, is_active, date_created, date_update) VALUES (1, 'standard', true, '2019-03-17 22:01:04.102255', '2019-03-17 22:01:04.106197');
INSERT INTO public.role (id, name, is_active, date_created, date_update) VALUES (2, 'administrator', true, '2019-03-17 22:01:43.629258', '2019-03-17 22:01:43.630388');

-- INSERT TABLE USER

INSERT INTO public."user" (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, second_surname, avatar, role_id) VALUES (3, 'pbkdf2_sha256$36000$fdbSNhaS4v9z$zkYCTQPNLBkLfcUkZkJQSnohyGOVyu0WwxennL9vTnY=', '2019-03-18 01:08:43.945670', true, 'root.2', 'test', 'test test', 'rt2@gmail.com', true, true, '2019-03-17 22:06:41.741243', '', 'images/avatars/profile.png', 1);
INSERT INTO public."user" (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, second_surname, avatar, role_id) VALUES (1, 'pbkdf2_sha256$36000$4wvMkYBkCgTL$LTSqZQaZ5v0vzozKZsQgbTdkLRjKc5dNstbFqvWFmps=', '2019-03-18 01:17:11.414722', true, 'root', '', '', 'root.2018@gmail.com', true, true, '2019-03-16 18:22:19.511076', '', 'images/avatars/profile.png', 2);

-- INSERT TABLE TICKET

INSERT INTO public.ticket (id, title, description, status, date_created, date_update, user_id) VALUES (47, 'Norma', 'Las normas son documentos técnico-legales con las siguientes características: Contienen especificaciones técnicas de aplicación voluntaria. Son elaborados por consenso de las partes interesadas: Fabricantes', 2, '2019-03-18 01:03:44.152051', null, 1);
INSERT INTO public.ticket (id, title, description, status, date_created, date_update, user_id) VALUES (49, 'Tecnología', 'La tecnología es la ciencia aplicada a la resolución de problemas concretos. Constituye un conjunto de conocimientos científicamente ordenados, que permiten diseñar y crear bienes', 2, '2019-03-18 01:06:32.443405', null, 1);
INSERT INTO public.ticket (id, title, description, status, date_created, date_update, user_id) VALUES (50, 'Python', 'Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible. Se trata de un lenguaje de programación multiparadigma', 2, '2019-03-18 01:07:34.409591', null, 1);
INSERT INTO public.ticket (id, title, description, status, date_created, date_update, user_id) VALUES (51, 'Angular', 'Angular, es un framework para aplicaciones web desarrollado en TypeScript, de código abierto, mantenido por Google, que se utiliza para crear y mantener aplicaciones web de una sola página', 2, '2019-03-18 01:12:08.764913', null, 1);