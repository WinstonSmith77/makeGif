import glob
import pathlib
from PIL import Image

def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.JPG")]
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames, save_all=True, duration=100, loop=0)

if __name__ == "__main__":
    path = pathlib.Path(r'C:\Users\matze\Desktop\export\Kinder\gif')
    make_gif(path)