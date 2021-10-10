from datetime import datetime

with open('log.txt', 'a') as f:
    f.write("Proceso Completado a {0}\n".format(datetime.now()))
    f.close()