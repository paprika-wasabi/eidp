def color(i: int, max_i: int) -> tuple[int, int, int]:
    # Farbton in AbhÃ¤ngigkeit der benÃ¶tigten SchleifendurchlÃ¤ufe.
    hue = int(255 * (i / max_i))

    # Volle Helligkeit 255, auÃŸer wenn c Teil der Mandelbrotmenge ist.
    # Dadurch wird das innere schwarz.
    value = 255 if i < max_i else 0

    # Volle SÃ¤ttigung
    saturation = 255

    return (hue, saturation, value)