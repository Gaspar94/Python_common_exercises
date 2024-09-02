import re

def find_range(text, word1, word2):
  """
  Encuentra un rango de texto en el que aparecen dos palabras en particular, delimitados por un paréntesis al finalizar la primera palabra clave y un paréntesis al finalizar todo el texto a analizar.

  Args:
    text: El texto a analizar.
    word1: La primera palabra clave.
    word2: La segunda palabra clave.

  Returns:
    La segunda palabra clave, o None si no se encuentra.
  """

  match = re.search(r"(.*?)(\b{}\b)(.*?)\b{}".format(word1, word2), text)
  if match:
    return match.group(2)
  else:
    return None


def main():
  word1 = "cc_binary"
  word2 = "[FUSA]"
  # Abre el archivo con texto a analizar.
  with open(r"C:\Users\Gaspar Serra\hello-world\ejemplo.txt", "r") as f:
    text = f.read()

  # Encuentra la segunda palabra clave.
  second_word = find_range(text, "palabra1", "palabra2")

  # Imprime el resultado.
  if second_word is not None:
    print("palabra1 - palabra2:", word1 + "-" + second_word)
  else:
    print("palabra1 - nf:", word1 + "-" + "nf")


if __name__ == "__main__":
  main()
