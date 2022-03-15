class ColorRecognition:
    @staticmethod
    def detectColor(red, green, blue):
        if red < 270 and red >= 220 and green < 40 and green >= 20 and blue < 30 and blue >= 10:
            return "Red"
        elif red < 35 and red >= 20 and green < 135 and green >= 110 and blue < 35 and blue >= 15:
            return "Green"
        elif red < 45 and red >= 15 and green < 60 and green >= 40 and blue < 55 and blue >= 40:
            return "Blue"
        else:
            return "None"