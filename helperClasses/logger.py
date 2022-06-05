class Logger:
    def __init__(self, logging_level=5, console=True, file=False):
        self.level = logging_level
        self.console = console
        self.file = file

        if file:
            try:
                self.filename = "./logs/velo.log"
                self.log_file = open(self.filename, "a+")
            except Exception:
                print("something went wrong")

    def set_logging_level(self, logging_level):
        self.level = logging_level

    def get_logging_level(self):
        return self.level

    def __printer(self, message):
        if self.console:
            print(message)
        if self.file:
            self.log_file.write(f"\n{message}\n")

    def fatal(self, message):
        if self.level >= 1:
            self.__printer(f"FATAL: {message}")
    
    def error(self, message):
        if self.level >= 2:
            self.__printer(f"ERROR: {message}")
    
    def warn(self, message):
        if self.level >= 3:
            self.__printer(f"WARN: {message}")
    
    def info(self, message):
        if self.level >= 4:
            self.__printer(f"INFO: {message}")
    
    def debug(self, message):
        if self.level == 5:
            self.__printer(f"DEBUG: {message}")
    
    def relocation(self, message):
        print(f"\nRELOCATION: {message}\n")

    def __new__(cls, logging_level = 5, console = True, file = False):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance