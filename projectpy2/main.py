import random
import time
import sys

def sequencial_search(vector, target):
    for i in range(len(vector)):
        if target == vector[i]:
            return i
    return -1

def generate_sorted_vector(x):
    vector = [random.randint(1, 10 * x) for _ in range(x)]
    vector.sort()
    return vector

def binary_search(vector, target):
    left, right = 0, len(vector) - 1
    while left <= right:
        mid = (left + right) // 2
        if vector[mid] == target:
            return mid
        elif vector[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    try:
        x = int(input("Digite um valor para o tamanho do vetor (1-10000): "))
        if x <= 0:
            raise ValueError("O valor deve ser maior que 0.")
        elif x > 10000:
            print(f"O valor {x} é muito alto e pode ocasionar em excesso do uso de memória e outros problemas.")
            continuar = input("Deseja continuar (s/n): ").strip().lower()
            if continuar == "n":
                print("Saindo do programa.")
                sys.exit()

        target = int(input("Digite um valor para procurar no vetor (target > 0): "))
        if target <= 0:
            raise ValueError("O valor deve ser maior que 0.")
        
    except ValueError as e:
        print(e)
        sys.exit()
    except Exception as e:
        print("Erro inesperado:", e)
        sys.exit()

    vector = generate_sorted_vector(x)
    print("Vetor gerado e ordenado:", vector)

    start_time = time.time()
    result = binary_search(vector, target)
    end_time = time.time()
    execution_time = end_time - start_time

    if result != -1:
        print(f"Elemento {target} encontrado no índice {result} (Busca Binária).")
    else:
        print(f"Elemento {target} não encontrado no vetor (Busca Binária).")
    print(f"Tempo de execução (Busca Binária): {execution_time:.6f} segundos")


    start_time = time.time()
    result = sequencial_search(vector, target)
    end_time = time.time()
    execution_time = end_time - start_time

    if result != -1:
        print(f"Elemento {target} encontrado no índice {result} (Busca Sequencial).")
    else:
        print(f"Elemento {target} não encontrado no vetor (Busca Sequencial).")
    print(f"Tempo de execução (Busca Sequencial): {execution_time:.6f} segundos")
