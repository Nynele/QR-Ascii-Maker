import qrcode

banner = """
  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄    ▄▄▄▄▄▄▄  
  █ ▄▄▄ █ ▀   ▄█ ▄   █ ▄▄▄ █  
  █ ███ █ ▀▀  █ ▀▄   █ ███ █  
  █▄▄▄▄▄█ █▀█ █ ▀ █ █▄▄▄▄▄█  
  ▄▄ ▄  ▄▄█▀█▄█▄▀▀█▄  ▄▄▄ ▄  
   ▄  ▀▄▄▄█▀ ▀▄█ ▄▄▄█▄▄▀ ▄   
  ▀▄▄▄▄▄▄▄ █▄▄█   █ ▄ ▄ █    
==========================================
     Generador de QR - Hecho por nynele
==========================================
"""

print(banner)
data = input("¿Qué contenido quieres en el QR?: ")
print("\nGenerando código QR...")

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)
qr.add_data(data)
qr.make(fit=True)

# Hecho por nynele

matrix = qr.get_matrix()
rows = len(matrix)
cols = len(matrix[0])

ascii_lines = []
for row in range(0, rows, 2):
    line = ""
    for col in range(cols):
        top = matrix[row][col]
        bottom = matrix[row+1][col] if (row + 1) < rows else False
        if top and bottom:
            char = "█"
        elif top and not bottom:
            char = "▀"
        elif not top and bottom:
            char = "▄"
        else:
            char = " "
        line += char
    ascii_lines.append("+ " + line)

for ascii_line in ascii_lines:
    print(ascii_line)
