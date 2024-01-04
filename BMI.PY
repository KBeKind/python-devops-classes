# Write a class that calculates and stores the height and weight of a person in metric. The BMI is calculated using this formula:
#     Weight/Height ^ 2 - weight is in kilograms and height is in meters.

# The class should have two properties named:
#     Weight
#     Height

# The class should have one method that returns a decimal named (no arguments should be accepted):
#     BMI_Value


class BMI:
    __weight = 0
    __height = 0

    # def __init__(self, weight, height):
    #     self.__weight = weight
    #     self.__height = height

    def get_weight(self):
        return self.__weight
    def set_weight(self, inWeight):
        self.__weight = inWeight

    def get_height(self):
        return self.__height
    def set_height(self, inHeight):
        self.__height = inHeight

    Weight = property(get_weight, set_weight)
    Height = property(get_height, set_height)

    def BMI_Value(self):
        return self.__weight / (self.__height ** 2)