import numpy as np
import cv2
from tqdm import trange
from imageio import mimwrite

# windows
#  FOURCC = 'DIVX'
# linux
FOURCC = 'XVID'

file = input('File name (default "input.mp4"):')
file = file if file else 'input.mp4'
cap = cv2.VideoCapture(file)
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
N = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
FPS = int(cap.get(cv2.CAP_PROP_FPS))
print(f'The input video has size of {W}x{H}, {N} frames and fps of {FPS}')
sec = input('During time (default 20s):')
sec = int(sec) if sec else 20
fps = input('Output fps (default 25):')
fps = int(fps) if fps else 25
mode = input('Mode ("mp4" or "gif", default "mp4"):')
mode = mode if mode else "mp4"
sep = int(N / (sec * fps))


if mode == "mp4":
    fourcc = cv2.VideoWriter_fourcc(*FOURCC)

    if W > H:
        out = cv2.VideoWriter('out.mp4', fourcc, fps, (W, H))
    else:
        out = cv2.VideoWriter('out.mp4', fourcc, fps, (H, W))
#      out = cv2.VideoWriter('out.mp4', fourcc, fps, (W, H))

    for i in trange(1, N, sep):
        cap.set(1, i)
        ret, frame = cap.read()
        if W < H:
            frame = np.rot90(frame, 1, (0, 1))
        out.write(frame)
    out.release()
elif mode == 'gif':
    v = []
    print('Reading...')
    for i in trange(1, N, sep):
        cap.set(1, i)
        ret, frame = cap.read()
        if W < H:
            frame = np.rot90(frame, 1, (0, 1))
#              frame.swapaxes(0, 1)
        v.append(frame[..., ::-1])
    mimwrite('out.gif', v, 'GIF', fps = fps)

cap.release()
