from captcha.image import ImageCaptcha

# Configura a imagem 
image = ImageCaptcha(width=280, height=90)

# texto escolhido para o captcha 
captcha_text = 'PycodeBR'

# Gera a imagem do captcha
data = image.generate(captcha_text)

# Salva a imagem no caminho escolhido 
image.write(captcha_text, 'captcha.png')