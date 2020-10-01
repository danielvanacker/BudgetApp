INSERT INTO active_user (id) VALUES (0);
INSERT INTO category (name, is_income, user_id) VALUES ('Groceries', false, 0), ('Travel', false, 0), ('Work Income', true, 0);
INSERT INTO budget (month, year, amount, comment, category_id, user_id) VALUES (8, 2020, 500, 'mock data', 2, 0), (7, 2020, 100, 'mock data 2', 1, 0), (8, 2020, 2000, 'work income', 3, 0);
INSERT INTO people (name, user_id) VALUES ('John Doe', 0), ('Foo Bar', 0), ('Tony Stark', 0);