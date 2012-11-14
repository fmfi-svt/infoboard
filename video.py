import os.path
import logging
from datetime import date

class Video:
    """Parses line containing description of a video.

    Line must contain filename (string) followed by duration (six numbers):
    test.avi 2012 1 12 2012 2 7

    This video would be played from 12th january 2012 to 7th february 2012.

    ValueError is thrown in case that specified file does not exists
    in 'videos' subfolder or there are not enough arguments.
    Possible reason is logged in 'infoboard.video' logger.
    """
    def __init__(self, line):
        try:
            filename, y1, m1, d1, y2, m2, d2 = line.split(' ')
            filename = 'videos/' + filename
            if not os.path.isfile(filename):
                raise ValueError('Video "{0}" does not exist'.format(filename))
            self.filename = filename
            self.start_date = date(int(y1), int(m1), int(d1))
            self.end_date = date(int(y2), int(m2), int(d2))
            if (self.end_date - self.start_date).total_seconds() < 0:
                message = 'Video "{0}" has start date after end date.'.format(
                    filename)
                logging.getLogger('infoboard.video').warning(message)
        except ValueError as e:
            message = "Error:\n    " + str(e) + "\n"
            message += "in configuration on line:\n    " + line + "\n"
            logging.getLogger('infoboard.video').error(message)
            raise e
