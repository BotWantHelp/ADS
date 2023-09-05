import multiprocessing
from datetime import datetime, timedelta

def worker():
    valor_inicial = datetime.now()
    print(valor_inicial)
    
    i = 0

    for i in range(10):
        i = i + 1

        valor_final = datetime.now()
        print(valor_final)

        tempo_decorrido = valor_final - valor_inicial
        print("Demorou:", tempo_decorrido)
        print("Valor:", i)

    if __name__ == '__main__':
        num_processes = multiprocessing.cpu_count()
        processes = [multiprocessing.Process(target=worker) for _ in range(num_processes)]       
        for process in processes:
            process.start()
        for process in processes:
            process.join()
            
worker()