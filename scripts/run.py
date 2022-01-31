import subprocess
import multiprocessing as mp

def run_vite():
    subprocess.run(["yarn", "dev"], check=True)

def run_django():
    subprocess.run(["python3", "manage.py", "runserver"], check=True)

vite = mp.Process(target=run_vite)
django = mp.Process(target=run_django)
vite.start()
django.start()
vite.join()
django.join()