from pwn import *

# Leer el archivo original byte por byte
with open('57FD6325.VBN', 'rb') as file:
    bytes_data = file.read()

# Función para verificar si la secuencia This está presente
def contains_this(byte_data):
    # La secuencia This en ASCII es [0x54, 0x68, 0x69, 0x73]
    return b'This' in byte_data  # Verifica si la secuencia b'This' está en los bytes

# Función para convertir los bytes en ASCII (solo caracteres imprimibles)
def to_ascii(byte_data)
    return ''.join([chr(b) if 32 = b = 126 else '.' for b in byte_data])

# Función para generar los archivos XOR y filtrar los que contienen This
def generate_xor_files(byte_data)
    for i in range(256)  # Para cada valor de XOR desde 0x00 hasta 0xFF
        xor_result = bytearray()

        # Aplicar XOR byte por byte con el valor `i`
        for byte in byte_data
            xor_result.append(byte ^ i)  # XOR con el valor i y añadir al resultado

        # Comprobar si la secuencia This está presente
        if contains_this(xor_result)
            # Convertir el resultado XOR a ASCII
            ascii_result = to_ascii(xor_result)

            # Guardar el archivo con el nombre `xor_{i}.txt` (formato ASCII)
            filename = f'xor_{i02X}.txt'
            with open(filename, 'w') as xor_file
                xor_file.write(ascii_result)  # Escribimos el resultado en formato ASCII
            print(fArchivo ASCII generado {filename})

# Llamar a la función para generar los archivos con XOR y verificar This
generate_xor_files(bytes_data)
