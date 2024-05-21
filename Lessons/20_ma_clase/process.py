import multiprocessing
import time
import random

class Procesamiento:
    def __init__(self, num_procesos=5):
        self.num_procesos = num_procesos

    def procesamiento_secuencial(self):
        print("Ejecutando procesamiento secuencial:")
        for i in range(self.num_procesos):
            self.task(i)
        print("Procesamiento secuencial completado")

    def procesamiento_paralelo(self):
        print("Ejecutando prosesamiento paralelo:")
        processes = []
        for i in range(self.num_procesos):
            p = multiprocessing.Process(target=self.task, args=(i,))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        print("Prosesamiento paralelo finalizado")

    def task(self, process_id):
        wait_time = random.randint(1, 5)
        print(f"Proceso {process_id}: Iniciando tarea. Esperando {wait_time} segundos")
        # print(f"Proceso con {self.num_procesos} procesos: Esperando {wait_time} segundos")
        time.sleep(wait_time)
        print(f"Proceso {process_id}: Tarea completada")
