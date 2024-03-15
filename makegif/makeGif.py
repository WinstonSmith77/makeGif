import glob
import pathlib
from PIL import Image

def make_gif(frame_folder : pathlib.Path):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.JPG")]
    frame_one = frames[0]

    dest = frame_folder.joinpath("my_awesome.gif")

    append = frames + frames[-2:-len(frames):-1]

    frame_one.save(dest, format="GIF", append_images=frames, save_all=True, duration=300, loop=0)

if __name__ == "__main__":
    path = pathlib.Path(r'C:\Users\matze\Desktop\export\Kinder\gif')
    
    make_gif(path)