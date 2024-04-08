from win10toast import ToastNotifier

# inicializa
toaster = ToastNotifier()

# Passa parâmetros e mostra a notificação 
toaster.show_toast(
    "Notificação",
    "Olá Remaldo",
    threaded=True,
    icon_path=None,
    duration=5 # 5 segundos
) 