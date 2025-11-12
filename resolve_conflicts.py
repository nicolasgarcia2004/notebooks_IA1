#!/usr/bin/env python3
"""
Script para resolver conflictos de merge en notebooks de Jupyter
"""
import json
import sys
import re

def resolve_conflicts(input_file, output_file):
    """
    Resuelve conflictos de merge tomando siempre la versión de 'Stashed changes'
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Detectar inicio de conflicto
        if line.startswith('<<<<<<< Updated upstream'):
            # Contar cuántos niveles de conflicto hay
            conflict_level = 1
            i += 1
            
            # Saltar hasta encontrar el separador =======
            while i < len(lines) and not (lines[i].strip() == '=======' and conflict_level == 1):
                if lines[i].startswith('<<<<<<< Updated upstream'):
                    conflict_level += 1
                i += 1
            
            # Saltar el separador =======
            if i < len(lines):
                i += 1
            
            # Ahora guardamos el contenido hasta >>>>>>> Stashed changes
            stashed_content = []
            while i < len(lines):
                if lines[i].startswith('>>>>>>> Stashed changes'):
                    conflict_level -= 1
                    i += 1
                    # Si hay más separadores ======= después, los saltamos
                    while i < len(lines) and lines[i].strip() == '=======':
                        i += 1
                    if conflict_level == 0:
                        break
                elif lines[i].strip() == '=======' and conflict_level > 1:
                    # Separador intermedio
                    i += 1
                else:
                    stashed_content.append(lines[i])
                    i += 1
            
            # Agregar el contenido stashed
            cleaned_lines.extend(stashed_content)
        else:
            cleaned_lines.append(line)
            i += 1
    
    result = ''.join(cleaned_lines)
    
    # Intentar validar y arreglar JSON
    try:
        data = json.loads(result)
        # Si llegamos aquí, el JSON es válido
        print("✓ El archivo JSON es válido")
        result = json.dumps(data, indent=1, ensure_ascii=False)
    except json.JSONDecodeError as e:
        print(f"⚠ Advertencia: Error de JSON en línea {e.lineno}, columna {e.colno}: {e.msg}")
        print(f"   Guardando archivo con conflictos resueltos, pero puede requerir edición manual")
    
    with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(result)
    
    print(f"✓ Conflictos resueltos. Archivo guardado en: {output_file}")
    
    # Verificar si quedan conflictos
    remaining = result.count('<<<<<<<')
    if remaining > 0:
        print(f"⚠ Advertencia: Todavía quedan {remaining} marcadores de conflicto")
    else:
        print("✓ No quedan marcadores de conflicto")
    
    return result

if __name__ == '__main__':
    input_file = 'Taller_std_04_20252_statistics.ipynb'
    output_file = 'Taller_std_04_20252_statistics_fixed.ipynb'
    resolve_conflicts(input_file, output_file)
