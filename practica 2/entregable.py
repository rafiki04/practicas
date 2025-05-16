def hex_to_ascii(hex_str):
    
    try:
        bytes_data = bytes.fromhex(hex_str)
        ascii_str = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in bytes_data])
        return ascii_str
    except:
        return ""

def multi_xor_with_ascii(main_hex, xor_hexes):

    
    results = {}
    
    try:
        main_bytes = bytes.fromhex(main_hex)
    except ValueError:
        raise ValueError("La cadena principal no es un hexadecimal válido")
    
    for i, xor_hex in enumerate(xor_hexes, 1):
        try:
            xor_bytes = bytes.fromhex(xor_hex)
        except ValueError:
            results[f"XOR {i}"] = {
                'hex': "ERROR: Cadena no válida",
                'ascii': ""
            }
            continue
        
        # Aplicar XOR hasta la longitud más corta
        min_len = min(len(main_bytes), len(xor_bytes))
        result_bytes = bytes(a ^ b for a, b in zip(main_bytes[:min_len], xor_bytes[:min_len]))
        
        # Convertir resultados
        hex_result = result_bytes.hex()
        ascii_result = hex_to_ascii(hex_result)
        
        results[f"XOR con cadena {i}"] = {
            'hex': hex_result,
            'ascii': ascii_result
        }
    
    return results

# Ejemplo de uso
if __name__ == "__main__":
    print("XOR con visualización ASCII\n")
    
    main_str = input("Introduce la cadena hexadecimal principal: ").strip()
    xor_strs = []
    
    print("\nIntroduce las cadenas para hacer XOR (deja vacío para terminar):")
    while True:
        s = input(f"Cadena XOR {len(xor_strs)+1}: ").strip()
        if not s:
            break
        xor_strs.append(s)
    
    try:
        resultados = multi_xor_with_ascii(main_str, xor_strs)
        
        print("\nResultados:")
        for key, val in resultados.items():
            print(f"\n{key}:")
            print(f"Hex: {val['hex']}")
            print(f"ASCII: {val['ascii']}")
            print("-" * 40)
            
    except ValueError as e:
        print(f"\nError: {e}")