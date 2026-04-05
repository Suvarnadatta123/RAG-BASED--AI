from importlib.resources import files
import os
import subprocess

videos = r"C:\Users\sumit\Rag-based-AI\videos" 

files = os.listdir(videos)
print(files)
    
for file in files: 
    tutorial_number = file.split(" [")[0].split(" #")[1]
    file_name = file.split(" ｜ ")[0]
    print( tutorial_number,  file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])