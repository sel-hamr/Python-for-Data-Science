import shutil

def get_percentage(part, whole):
    """Return the percentage of part in whole."""
    if whole == 0:
        return 0  # To avoid division by zero
    return int((part / whole) * 100)

def ft_tqdm(list:range):
    """Print a progress bar for the given list."""
    i = 0
    listLength = len(list)
    terminal_width = shutil.get_terminal_size().columns - 13
    while i <= listLength:
        percentage = get_percentage(i,listLength)
        progress = int(i / listLength * terminal_width)
        progress_bar = f"|{'█' * progress:<{terminal_width}}|"
        print(f"\r{percentage}%{progress_bar}{i}/{listLength}", end="")
        yield i
        i+=1