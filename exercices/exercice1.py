def rechercheMinMax(tab):
  dico = {}
  if tab != []:
    min = tab[0]
    max = tab[0]
    for element in tab:
      if element < min:
        min = element
      elif element > max:
        max = element
    dico["min"] = min
    dico["max"] = max
  else :
    dico["min"] = None
    dico["max"] = None
  return dico
