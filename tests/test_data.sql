INSERT INTO tasks (title, task_enable, check_interval, notes) VALUES
('Test Task 1', true, 120, 'Test Task 1 Notes'),
('Test Task 2', true, 300, 'Test Task 2 Notes'),
('Test Task 3', false, 900, 'Test Task 3 Notes'),
('Test Task 4', true, 60, 'Test Task 4 Notes');

INSERT INTO from_dirs (task_id, path_from_dir, del_after_copy, del_not_copy_files, backup_not_copy_files, backup_dir_not_copy_files, create_dir_day_not_copy_files, create_dir_hour_not_copy_files, create_dir_extension_not_copy_files) VALUES
(1, '/home/alex/project/file_transfer_test_folder/from_folder_1', true, false, false, false, false, false, false),
(2, '/home/alex/project/file_transfer_test_folder/from_folder_2', true, false, false, false, false, false, false),
(3, '/home/alex/project/file_transfer_test_folder/from_folder_3', true, false, false, false, false, false, false),
(4, '/home/alex/project/file_transfer_test_folder/from_folder_4', true, false, false, false, false, false, false);

INSERT INTO to_dirs (task_id, path_to_dir, create_dir_day, create_dir_hour, create_dir_extension) VALUES
(1, '/home/alex/project/file_transfer_test_folder/to_folder_1', false, false, false),
(2, '/home/alex/project/file_transfer_test_folder/to_folder_2', false, false, false),
(3, '/home/alex/project/file_transfer_test_folder/to_folder_3', false, false, false),
(4, '/home/alex/project/file_transfer_test_folder/to_folder_4', false, false, false);

INSERT INTO file_extensions (from_dir_id, extension, min_size_file, max_size_file) VALUES
(1, 'txt', 0, 104857600),
(2, 'txt', 0, 104857600),
(3, 'txt', 0, 104857600),
(4, 'txt', 0, 104857600);