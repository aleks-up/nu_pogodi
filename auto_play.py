import mss
import pyautogui
from pynput import keyboard

# Список объектов для проверки
objects = [
    {"id": 1, "key": "q", "points": [{"coords": (302, 476), "expected_color": (166, 174, 162)}]},
    {"id": 2, "key": "a", "points": [{"coords": (300, 528), "expected_color": (155, 162, 150)}]},
    {"id": 3, "key": "e", "points": [{"coords": (468, 472), "expected_color": (159, 165, 153)}]},
    {"id": 4, "key": "d", "points": [{"coords": (471, 528), "expected_color": (148, 154, 142)}]}
]


def on_press(key):
    if key == keyboard.Key.esc:
        print("Выход из программы...")
        exit(0)


def get_pixel_color(x, y):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(monitor)
        return img.pixel(0, 0)[:3]


def start_key_listener():
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()
    return keyboard_listener


def main():
    start_key_listener()

    while True:
        for obj in objects:
            obj_id = obj["id"]
            obj_key = obj["key"]

            for point in obj["points"]:
                x, y = point["coords"]
                expected_color = point["expected_color"]

                actual_color = get_pixel_color(x, y)

                expected_sum = sum(expected_color)
                actual_sum = sum(actual_color)
                if expected_sum == 0:
                    continue
                diff_percent = abs(actual_sum - expected_sum) / expected_sum * 100

                if diff_percent > 10:
                    print(f"{obj_id}: ({x}, {y}) -> {actual_color} (diff: {diff_percent:.2f}%)")
                    pyautogui.press(obj_key)


if __name__ == "__main__":
    main()
