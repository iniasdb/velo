class Logger:
    def __init__(self, logging_level=5, out=None):
        self.level = logging_level
        self.out = out

        if out == "File":
            try:
                self.filename = "./logs/velo.log"
                self.log_file = open(self.filename, "a+")
            except Exception as e:
                print("something went wrong")

    def set_logging_level(self, logging_level):
        self.level = logging_level

    def get_logging_level(self):
        return self.level
    
    def set_out(self, out):
        self.out = out

    def get_out(self):
        return self.out

    def printer(self, message):
        if self.out == None:
            print(message)
        elif self.out == "File":
            self.log_file.write(message + "\n")

    def fatal(self, message):
        if self.level >= 1:
            self.printer("FATAL: " + message)
    
    def error(self, message):
        if self.level >= 2:
            self.printer("ERROR: " + message)
    
    def warn(self, message):
        if self.level >= 3:
            self.printer("WARN: " + message)   
    
    def info(self, message):
        if self.level >= 4:
            self.printer("INFO: " + message)
    
    def debug(self, message):
        if self.level == 5:
            self.printer("DEBUG: " + message)