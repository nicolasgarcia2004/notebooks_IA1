#!/usr/bin/env python3
import sys

def main():
    input_file = 'Taller_std_04_20252_statistics.ipynb'
    output_file = 'Taller_std_04_20252_statistics_clean.ipynb'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result = []
    i = 0
    conflicts_resolved = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Si encontramos un bloque de conflicto
        if line.startswith('<<<<<<< Updated upstream'):
            conflicts_resolved += 1
            # Contar niveles de anidación
            upstream_count = 1
            i += 1
            
            # Saltar la parte "upstream" (vieja)
            while i < len(lines):
                if lines[i].startswith('<<<<<<< Updated upstream'):
                    upstream_count += 1
                    i += 1
                elif lines[i].strip() == '=======' and upstream_count > 0:
                    upstream_count -= 1
                    i += 1
                    if upstream_count == 0:
                        break
                else:
                    i += 1
            
            # Ahora estamos en la sección "stashed" (nueva) - guardar esta parte
            stashed_lines = []
            stashed_count = 0
            
            while i < len(lines):
                if lines[i].startswith('>>>>>>> Stashed changes'):
                    stashed_count += 1
                    i += 1
                    # Si hay separadores ======= después, son parte del cierre anidado
                    while i < len(lines) and lines[i].strip() == '=======':
                        stashed_count += 1
                        i += 1
                    # Cuando tengamos todos los cierres, terminamos
                    if stashed_count >= conflicts_resolved or (i < len(lines) and not lines[i].startswith('<<<<<<< Updated upstream')):
                        conflicts_resolved = max(0, conflicts_resolved - 1)
                        break
                else:
                    stashed_lines.append(lines[i])
                    i += 1
            
            # Agregar las líneas stashed al resultado
            result.extend(stashed_lines)
        else:
            result.append(line)
            i += 1
    
    # Escribir resultado
    with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
        f.writelines(result)
    
    print(f"✓ Archivo limpio guardado en: {output_file}")
    print(f"✓ Total de líneas: {len(result)}")
    
    # Verificar JSON
    import json
    with open(output_file, 'r', encoding='utf-8') as f:
        try:
            json.load(f)
            print("✓ El archivo JSON es válido")
        except Exception as e:
            print(f"⚠ Error de JSON: {e}")

if __name__ == '__main__':
    main()
