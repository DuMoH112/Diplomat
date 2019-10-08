import cv2


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)  # 0 это стандартная камера
    while True:
        return_value, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
            cv2.imshow('Webcam', img)
            if cv2.waitKey(1) == 27:
                break  # нажмите esc для выхода

    def main():
        show_webcam(mirror=True)

    if __name__ == '__main__':
        main()
