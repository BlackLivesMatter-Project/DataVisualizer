"""Used to handle custom errors in the DataParser class."""

class DataParserError(Exception):
    """main error handler"""
    def __init__(self, message="There was an issue"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class DataParserFileNotExist(DataParserError):
    """Used to handle file errors where a file does not exist"""
    def __init__(self, file, message="Specified file does not exist"):
        self.file = file
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: '{self.file}'"

class DataParserNotAFile(DataParserError):
    """Used to handle file errors where a file is not a file"""
    def __init__(self, file, message="Specified path is not a file"):
        self.file = file
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: '{self.file}'"

class DataParserFileNotReadable(DataParserError):
    """Used to handle file errors where a file is not readable"""
    def __init__(self, file, message="Specified file is not a readable"):
        self.file = file
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: '{self.file}'"

class DataParserNotAnInteger(DataParserError):
    """Used to handle file errors where a file is not readable"""
    def __init__(self, number, message="The following is not an integer"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: '{self.number}'"
