
lighting_modes = {
    "work": {"brightness": 80, "human_detect": True},
    "night": {"brightness": 10, "human_detect": True},
    "energy_saving": {"brightness": 50, "human_detect": True}
}


class LightingModes:
    def __init__(self):
        self.current_mode = "work"
        self.brightness = 80

    def set_mode(self, mode):
        if mode in lighting_modes:
            self.current_mode = mode
            self.apply_mode()
        else:
            raise ValueError(f"Режим {mode} не найден.")

    def apply_mode(self):
        mode_settings = lighting_modes[self.current_mode]
        self.brightness = mode_settings["brightness"]
        print(f"Режим {self.current_mode} установлен. Яркость: {self.brightness}%")

    def set_custom_mode(self, brightness: int, human_detect: bool):
        lighting_modes["custom"] = {"brightness": brightness, "human_detect": human_detect}
        self.set_mode("custom")

    def adjust_brightness_on_detection(self, human_detected: bool):
        if lighting_modes[self.current_mode]["human_detect"] and human_detected:
            # Повышаем яркость на 20
            self.brightness = min(self.brightness + 20, 100)
            print(f"Человек обнаружен. Яркость: {self.brightness}%")
        elif not human_detected:
            # Возвращаем яркость к стандартной
            self.brightness = lighting_modes[self.current_mode]["brightness"]
            print(f"Человек не обнаружен. Яркость: {self.brightness}%")


lighting_system = LightingModes()

# Устанавливаем рабочий режим
lighting_system.set_mode("work")

# Обнаружен человек
lighting_system.adjust_brightness_on_detection(human_detected=True)

# Человек ушел
lighting_system.adjust_brightness_on_detection(human_detected=False)

# Устанавливаем кастомный режим
lighting_system.set_custom_mode(25, True)

# Кастомный режим
lighting_system.adjust_brightness_on_detection(human_detected=True)

