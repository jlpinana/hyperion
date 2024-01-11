:: Task 1 --> Script with IF statements

if exist new_folder mkdir if_folder
if exist if_folder (mkdir hyperionDev) else (mkdir new-projects)
dir
cmd.exe