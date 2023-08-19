"""
Estimate time: 1hour
Actual time: 2hours
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KILOMETER_TO_MILES = 1.609344


class ConvertMilesKmApp(App):
    result = StringProperty()

    def build(self):
        """build the Kivy app from the kv file"""
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_miles_to_km(self):
        km = self.validate_miles() * 1.609344
        self.result = str(km)

    def validate_miles(self):
        try:
            miles = float(self.root.ids.input_number.text)
        except ValueError:
            miles = 0.0
        return miles

    def handle_increment(self, change):
        miles = int(self.validate_miles() + change)
        self.root.ids.input_number.text = str(miles)
        self.handle_miles_to_km()


ConvertMilesKmApp().run()
