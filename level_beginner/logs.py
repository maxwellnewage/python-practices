"""
Implementación del módulo logging
"""
import logging
import time

if __name__ == '__main__':
    logging.basicConfig(
        filename='level_beginner/resources/generated/log.txt',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # logging.disable(logging.CRITICAL) # disable all msgs

    for i in range(5):
        logging.debug(f'Testing debug log! Num: {i}')
        time.sleep(0.5)
        logging.info(f'Testing debug log! Num: {i}')
        time.sleep(0.5)
        logging.error(f'Testing debug log! Num: {i}')