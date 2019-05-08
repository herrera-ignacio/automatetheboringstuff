#! python
# logging module demo
import logging

# filename='myProgramLog.txt'
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
logging.info('Logging module is working')
logging.warning('This is only for demostration')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))

    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))

logging.error('An error would be shown heres')
logging.critical('Critical message!')

# Disable log
# logging.disable(logging.CRITICAL)
# if you dont use arg, disable all

logging.debug('End of program')
