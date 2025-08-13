import pyttsx3 as pyt

class TextoAVoz:
    """
    Clase para convertir texto a voz utilizando pyttsx3.
    Permite ajustar velocidad, volumen, voz y guardar el audio en un archivo.
    """

    def __init__(self, velocidad=-25, volumen=0.5, voz_index=0):
        self.engine = pyt.init()

        # Ajuste de velocidad
        rate = self.engine.getProperty("rate")
        self.engine.setProperty("rate", rate + velocidad)

        # Ajuste de volumen
        volume = self.engine.getProperty("volume")
        self.engine.setProperty("volume", min(max(volumen, 0.0), 1.0))

        # Selección de voz
        voices = self.engine.getProperty("voices")
        if voices:
            self.engine.setProperty("voice", voices[voz_index].id)

    def reproducir(self, texto):
        """Reproduce el texto como audio."""
        if not texto.strip():
            print("No se ingresó texto para convertir.")
            return
        self.engine.say(texto)
        self.engine.runAndWait()

    def guardar_a_archivo(self, texto, archivo_salida="salida.mp3"):
        """Convierte el texto a voz y lo guarda como archivo."""
        if not texto.strip():
            print("No se ingresó texto para convertir.")
            return

        self.engine.save_to_file(texto, archivo_salida)
        print(f"Audio guardado como {archivo_salida}")
        self.engine.runAndWait()


if __name__ == "__main__":
    texto = input("Introduce el texto que quieres convertir: ")
    tav = TextoAVoz()

    # Reproducir
    tav.reproducir(texto)

    # Guardar como archivo (opcional)
    guardar = input("¿Quieres guardar el audio como archivo? (s/n): ").lower()
    if guardar == "s":
        tav.guardar_a_archivo(texto, "voz_generada.mp3")
