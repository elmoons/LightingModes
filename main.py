lighting_modes = {
    "day": {"brightness": 10, "human_detect": True},
    "night": {"brightness": 20, "human_detect": True},
    "energy_saving": {"brightness": 5, "human_detect": True}
}


class LightingModes:
    def __init__(self):
        self.current_mode = None
        self.brightness = None

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

    def adjust_brightness_on_detection(self, human_detected: bool, is_day: bool, cloudly: int):
        base_brightness = lighting_modes[self.current_mode]["brightness"]

        if is_day:
            if human_detected:
                # День + облачность с человеком
                self.brightness = base_brightness + (cloudly * 0.7) if cloudly > 0 else base_brightness + (cloudly * 0.4)
            else:
                # День + облачность без человека
                self.brightness = base_brightness + (cloudly * 0.7) if cloudly > 0 else 0
        else:
            if human_detected:
                # Ночь с человеком
                self.brightness = 100
            else:
                # Ночь без человека
                self.brightness = base_brightness

        # Ограничение яркости в диапазоне [0, 100]
        self.brightness = max(0, min(self.brightness, 100))

        print(f"Человек обнаружен: {human_detected}. День: {is_day}. Облачность: {cloudly}%. Яркость: {self.brightness}%.")


# Пример использования
lighting_system = LightingModes()

# Устанавливаем ночной режим
lighting_system.set_mode("night")

# Ночь + человек
lighting_system.adjust_brightness_on_detection(human_detected=True, cloudly=50, is_day=False)

# Ночь без человека
lighting_system.adjust_brightness_on_detection(human_detected=False, cloudly=50, is_day=False)

# День + облачно + человек
lighting_system.adjust_brightness_on_detection(human_detected=True, cloudly=50, is_day=True)

# День + ясно + человек
lighting_system.adjust_brightness_on_detection(human_detected=True, cloudly=0, is_day=True)

# День + облачно без человека
lighting_system.adjust_brightness_on_detection(human_detected=False, cloudly=50, is_day=True)

lighting_system.set_custom_mode(40, False)

lighting_system.apply_mode()
