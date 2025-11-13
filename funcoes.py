import time
import os
import platform

def contar_tempo(minutos):
    """
    Conta o tempo decrescente a partir do número de minutos fornecido.

    Parâmetros:
    minutos (int): Número de minutos para contar.
    """
    total_segundos = minutos * 60
    while total_segundos >= 0:
        mins, secs = divmod(total_segundos, 60)
        yield mins, secs
        time.sleep(1)
        total_segundos -= 1

def tocar_som():
    """
    Toca um som de notificação para indicar o fim do timer.
    """
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)  # Frequência de 1000Hz por 500ms
    else:
        os.system('printf "\a"')