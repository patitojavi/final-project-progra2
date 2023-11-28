class Ambiente:
    def __init__(self, fact_ambioticos, eve_climaticos):
        self.fac_ambioticos = fact_ambioticos
        self.eve_climaticos = eve_climaticos

        # Ejemplo de factores ambientales iniciales
        self.temperatura = 25  # Temperatura inicial
        self.lluvia = False  # No hay lluvia al inicio

    def evento_climatico(self):

        # Por ejemplo, cambios en la temperatura, lluvia, etc.

        # Actualizar la temperatura
        if self.eve_climaticos == "calor":
            self.temperatura += 5  # Incrementar la temperatura
        elif self.eve_climaticos == "lluvia":
            self.lluvia = True  # Activar la lluvia

        # Otros tipos de eventos climáticos y sus efectos

    def factor_ambiental(self):

        # Por ejemplo, cambio en la vegetación, cambio de estaciones, etc.

        # Cambios estacionales
        if self.fac_ambioticos == "cambio_estacion":
            # Actualizar la vegetación según la estación
            if self.eve_climaticos == "invierno":
                # Cambiar la vegetación para el invierno
                pass
            elif self.eve_climaticos == "verano":
                # Cambiar la vegetación para el verano
                pass
