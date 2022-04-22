import datetime as d_t
import os


def logger(function):
    def _logger(*args, **kwargs):
        with open('log_file.txt', 'w') as file:
            today = d_t.date.today()
            now = d_t.datetime.now().strftime('%H:%M:%S')
            file.write(f'{today} | {now} | {function.__name__} | {args}, {kwargs} ')
        result = function(*args, **kwargs)
        return result

    return _logger


def path_to_logs(path):
    saved_file = os.path.join(path, 'log_file.txt')

    def fixed_logger(function):
        def _fixed_logger(*args, **kwargs):
            today = d_t.date.today()
            now = d_t.datetime.now().strftime('%H:%M:%S')
            result = function(*args, **kwargs)
            with open(saved_file, 'w') as file:
                file.write(f'{today} | {now} | {function.__name__} | {args}, {kwargs} | {result}')
            return result

        return _fixed_logger

    return fixed_logger
