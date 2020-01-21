def get_message(binary):
    message = ""
    for byte in [binary[step * 8: step * 8 + 8] for step in range(0, int(len(binary)/8))]:
        message += chr(int(byte, 2))
    return message