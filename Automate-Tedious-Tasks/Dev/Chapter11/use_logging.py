import logging
logging.basicConfig(
    filename='mylog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# logging.disable(logging.CRITICAL)
logging.debug('Start of program')


def factorial(n):
    """计算阶层"""
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ',  total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')