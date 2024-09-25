import mss
import pyautogui

# Список объектов для проверки
objects = [
    {"id": 1, "key": "q", "points": [{"coords": (291, 471), "expected_color": (172, 211, 114)}]},
    {"id": 2, "key": "a", "points": [{"coords": (294, 559), "expected_color": (105, 66, 39)}]},
    {"id": 3, "key": "p", "points": [{"coords": (527, 478), "expected_color": (124, 180, 115)}]},
    {"id": 4, "key": "l", "points": [{"coords": (526, 564), "expected_color": (111, 65, 39)}]}
]


# Получаем цвет пикселя по координате
def get_pixel_color(x, y):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(monitor)
        # Возвращаем только RGB
        return img.pixel(0, 0)[:3]


while True:
    for obj in objects:
        obj_id = obj["id"]
        obj_key = obj["key"]

        for point in obj["points"]:
            x, y = point["coords"]
            expected_color = point["expected_color"]

            # Получаем фактический цвет пикселя через mss
            actual_color = get_pixel_color(x, y)

            # Сравниваем только RGB
            if actual_color != expected_color:
                print(f"{obj_id}: ({x}, {y}) -> {actual_color}")
                pyautogui.press(obj_key)
