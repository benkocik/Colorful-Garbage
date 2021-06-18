# Colorful-Garbage
IME-211 Project

How to install required modules:
pip install -r requirements.txt

How to run the program (Images can be replaced accordingly, image must be a png or bitmap)
Hide message in image:
python main.py -n 1 -o kyle_embedded_file.png -v 50 -i "file:kyle.png" -m "str:Have a great summer! Thanks for a great class- Kyle Heestand and Ben Kocik"

Hide file in image:
python main.py -n 1 -o ben_embedded_file.png -v 50 -i "file:ben.png" -m "file:kyle_resized.png"

Unhide message from kyle_embedded_file.png:
python main.py -n 1 -v 50 -i "file:kyle_embedded_file.png"
Output- MESSAGE: Have a great summer! Thanks for a great class- Kyle Heestand and Ben Kocik

Uhide file from ben_embedded_file.png and write to file embedded_img.png:
python main.py -n 1 -o embedded_img.png -v 50 -i "file:ben_embedded_file.png"       
Resulting image should be kyle.png but a smaller size
