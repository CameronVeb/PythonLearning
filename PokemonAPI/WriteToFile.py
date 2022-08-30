from operator import concat
from pathlib import Path

File_Path = 'C:\Repo_PythonLearning\PythonLearning\PokemonAPI'
File_Name = '\Pokemon_Types.txt'
File_Path_Name = concat(File_Path,File_Name)

with open(File_Path_Name,'a') as f: ##context manager
    pass
    # f_contents = f.readline()
    # print(f_contents, end = '')

    # f_contents = f.readline()
    # print(f_contents, end = '')
    f.write('\nDragon')
  

    with open(File_Path_Name,'r') as rf:
        f_contents = rf.readlines()
        print(f_contents)
