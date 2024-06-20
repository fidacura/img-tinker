import logging

def setup_logger(name, level=logging.INFO):
    """
    A basic logger that outputs to the console.
    
    Args:
        name (str): Name of the logger.
        level: Logging level, e.g. logging.INFO, logging.DEBUG
        
    Returns:
        A configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    return logger
