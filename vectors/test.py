def extended_range(start: int, stop: int, step: int) -> list:
    return [start + i * step for i in range(int(stop / step) + start)]


print(extended_range(-7, 8, 0.5))
