# Função de busca binaria interativa
# Ele retorna o índice de x em determinado array arr, se presente 
# se não ele retorna -1

def binarySearch(arr, x):
    low = mid = 0
    high = len(arr) - 1

    while low <= high:
        
        mid = (low + high) // 2
        
        # Se x for maior, ignore a metade esquerda
        if arr[mid] < x:
            low = mid + 1
            
        # Se x for menor, ignore a metade direita
        elif arr[mid] > x:
            high = mid - 1
        
        # Significa que x esta no meio
        else:
            return mid
    # se chegarmos ate aqui, significa que x nao esta presente no array
    return -1

# Crição das variaveis arr e x
arr = [1,2,3,4,5,6,10,20,30,40,50,60,70,80,90,100]
x = 100

# Chamando a função
result = binarySearch(arr,x)


if result != -1:
    print(f'O elemento foi encontrado no index {str(result)}')
else:
    print('O elemento nao foi encontrado no array')