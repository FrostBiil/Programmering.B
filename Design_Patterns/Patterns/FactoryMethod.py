
# Create logger interface - This interface should have a method log_message that takes a message as input.
class Logger():
    def log_message(self, message):
        raise NotImplementedError('log_message() must be implemented')

# Implement Concrete Loggers - Create at least three different logger classes that implement the Logger interface, each capable of logging messages in a different format (JSONLogger, TextLogger, XMLLogger).
class JSONLogger(Logger):
    def __init__(self, path):
        self.path = path

    def log_message(self, message):
        print('Logging to JSON file: {}'.format(self.path))
        print('Message: {}'.format(message))

class TextLogger(Logger):
    def __init__(self, path):
        self.path = path

    def log_message(self, message):
        print('Logging to text file: {}'.format(self.path))
        print('Message: {}'.format(message))

class XMLLogger(Logger):
    def __init__(self, path):
        self.path = path

    def log_message(self, message):
        print('Logging to XML file: {}'.format(self.path))
        print('Message: {}'.format(message))

# Create a LoggerFactory Class - This class should have a method that returns an instance of the logger. The type of logger returned (JSON, text, XML) should be based on an input parameter.

class LoggerFactory():
    def get_logger(self, logger_type, path):
        if logger_type == 'json':
            return JSONLogger(path)
        elif logger_type == 'text':
            return TextLogger(path)
        elif logger_type == 'xml':
            return XMLLogger(path)
        else:
            raise Exception('Logger type not found')
        
# Demonstrate the Usage - Write a small script where you use the LoggerFactory to get different types of loggers and log messages in different formats.
logger_factory = LoggerFactory()
json_logger = logger_factory.get_logger('json', 'log.json')
json_logger.log_message('This is a JSON log message')