import re
def name_normalize(name):
  name = name.lower()
  name = re.sub(r'[^a-z0-9]', '', name)
  return name

def file_processing(input_file, output_file):
  with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for line in f_in:
      name = line.strip()
      if name:
        final_name = name_normalize(name)
        f_out.write(final_name + '\n')

file_processing("pokemon.txt", "pokemon_normalizado.txt")