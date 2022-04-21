import numpy as np
import cv2

from widgets import VideoWidget

base = np.full((512, 512, 3), 255, dtype=np.uint8)

app = VideoWidget()
while True:
    app.ShowFrame(base)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break