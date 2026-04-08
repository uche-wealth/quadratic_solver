import logging 


logging.basicConfig(level=logging.INFO)


try:
    from .solve_and_graph import SolveAndGraphQuadratics
except Exception as exc:
    logging.error('An error occured: %s' % exc)
else:
    logging.info('Successfully imported module')



def main():
    sgq = SolveAndGraphQuadratics(a='', b='', c='')
    sgq.main_loop()


print(main())
