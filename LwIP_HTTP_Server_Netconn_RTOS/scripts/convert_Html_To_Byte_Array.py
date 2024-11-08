import sys

def convert_html_to_byte_array(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        byte_array = ', '.join(f'0x{ord(c):02X}' for c in html_content)
        
        array_name = "data_index_html"
        c_array = f"const unsigned char {array_name}[] = {{\n    {byte_array}\n}};\n"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(c_array)
        
        print(f"Conversion réussie. Le tableau C a été sauvegardé dans {output_file}.")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_html_to_byte_array.py <input_file.html> <output_file.c>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_html_to_byte_array(input_file, output_file)