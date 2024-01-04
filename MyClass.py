class MyClass:

    __myString = ""

    # STANDARD CONSTRUCTOR WITH NO PARAMS
    def __init__(self):
        self.__myString = "Hello World"
    
    # CONSTRUCTOR WITH PARAMS
    def __init__(self, inMyString):
        self.__myString = inMyString

    def get_myString(self):
        return self.__myString
    def set_myString(self, value):
        self.__myString = value

    
    # THIS aString CONNECTS THE GETTER AND SETTER SO WHEN IT IS CALLED THESE METHODS ARE USED TO GET OR SET THE VALUE FOR __myString.
    # aString IS A PROPERTY THAT PROVIDES A CONTROLLED INTERFACE TO THE PRIVATE ATTRIBUTE '__myString'.
    # IT UTILIZES THE property FUNCTION TO LINK THE GETTER (get_myString) AND SETTER (set_myString) METHODS.
    # THIS ENCAPSULATION TECHNIQUE ENSURES THAT '__myString' CAN BE ACCESSED AND MODIFIED SAFELY THROUGH THESE METHODS,
    # AND THIS ALLOWS FOR ADDITIONAL LOGIC OR VALIDATION IN THE GETTER AND SETTER IF NEEDED.
    aString = property(get_myString, set_myString)

    def reverseAString(self):
        return self.__myString[::-1]
    
    def appendAString(self, inSuffix):
        self.__myString = self.__myString + inSuffix
        