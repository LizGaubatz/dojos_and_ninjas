-- INSERT INTO dojos (id, name, created_at, updated_at)VALUES(1, 'Seattle', Now(), Now()),(2, 'Boise', Now(), Now()),(3, 'New Orleans', Now(), Now()), (4, 'Chicago', Now(), Now()),(5, 'San Antonio', Now(), Now()),(6, 'Denver', Now(), Now());
-- INSERT INTO ninjas (id, first_name, last_name, age, created_at, updated_at, dojos_id)VALUES(1, 'Tony','Stars',15,Now(), Now(),1),(2, 'Bobby','Earth',20,Now(), Now(),1),(3, 'George','Liff',18,Now(), Now(),1);
-- INSERT INTO ninjas (id, first_name, last_name, age, created_at, updated_at,dojos_id)VALUES(4, 'Kyle','Mann',15,Now(), Now(),2),(5, 'Bobo','Skye',22,Now(), Now(),2),(6, 'Harry','Mate',14,Now(), Now(),2);
-- INSERT INTO ninjas (id, first_name, last_name, age, created_at, updated_at,dojos_id)VALUES(7, 'Cloone','Bare',19,Now(), Now(),3),(8, 'Liz','Mountana',23,Now(), Now(),3),(9, 'Jenny','Lo',19,Now(), Now(),3);
-- -- SELECT *from ninjas where dojo_i

SELECT * FROM dojos;
SELECT * FROM ninjas;

SELECT * FROM dojos JOIN ninjas ON dojos.id = dojos_id WHERE dojos_id = 3;