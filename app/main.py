"""
Módulo para calcular média e verficar aprovação!
"""


def calcular_media(valores):
    """
    Calcula a média de uma lista de valores.
    
    Args:
        valores: Lista de números para calcular a média.
        
    Returns:
        float: A média dos valores.
        
    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not valores:
        raise ValueError("A lista não pode estar vazia.")
    return sum(valores) / len(valores)


def verificar_aprovacao(valores):
    """
    Verifica se um aluno foi aprovado com base em suas notas.
    
    Args:
        valores: Lista de notas do aluno.
        
    Returns:
        str: "Aprovado" se a média for >= 7, "Reprovado" caso contrário.
    """
    media = calcular_media(valores)
    return "Aprovado" if media >= 7 else "Reprovado"


if __name__ == "__main__":
    notas = [float(x) for x in input("Digite as notas separadas por espaço: ").split()]
    print(verificar_aprovacao(notas))
