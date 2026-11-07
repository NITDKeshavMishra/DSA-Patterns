class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        
        kel=float(celsius)+273.15
        fahren=float((celsius*1.80)+32.00)

        return [kel,fahren]