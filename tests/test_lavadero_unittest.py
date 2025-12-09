# tests/test_lavadero_unittest.py

import unittest
from lavadero import Lavadero


class TestLavadero(unittest.TestCase):
    """
    Pruebas de la lógica del lavadero:
    - Reglas de negocio (caja negra).
    - Transiciones de fases e ingresos (caja blanca/caminos).
    """

    def setUp(self):
        """Crear un lavadero nuevo antes de cada prueba."""
        self.lavadero = Lavadero()

    # ============================================================
    # CAJA NEGRA: Reglas de negocio y validaciones
    # ============================================================

    def test_inicializacion_correcta(self):
        """El lavadero empieza inactivo, sin ingresos y no ocupado."""
        self.assertFalse(self.lavadero.ocupado)
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)

    def test_no_permitir_lavado_mientras_esta_ocupado(self):
        """Requisito 3: No se puede iniciar un lavado si ya está ocupado."""
        self.lavadero.hacerLavado(prelavado_a_mano=False,
                                  secado_a_mano=False,
                                  encerado=False)
        with self.assertRaises(RuntimeError):
            self.lavadero.hacerLavado(prelavado_a_mano=False,
                                      secado_a_mano=False,
                                      encerado=False)

    def test_no_permitir_encerado_sin_secado_mano(self):
        """Requisito 2: Encerado sin secado a mano debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(prelavado_a_mano=False,
                                      secado_a_mano=False,
                                      encerado=True)

    def test_precio_base_sin_extras(self):
        """
        Requisito 9: Lavado sin extras.
        Precio esperado: 5.00 €
        """
        self.lavadero.hacerLavado(prelavado_a_mano=False,
                                  secado_a_mano=False,
                                  encerado=False)
        # Primera llamada a avanzarFase cobra el lavado
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 5.00, places=2)

    def test_precio_con_todos_los_extras(self):
        """
        Requisitos 4, 7, 8, 14:
        Prelavado + secado a mano + encerado.
        Precio esperado según comentario: 5.00 + 1.50 + 1.20 + 1.00 = 8.70 €
        """
        self.lavadero.hacerLavado(prelavado_a_mano=True,
                                  secado_a_mano=True,
                                  encerado=True)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 8.70, places=2)

    def test_precio_solo_prelavado(self):
        """
        Requisito 4 y 10:
        Solo prelavado a mano.
        Precio esperado: 5.00 + 1.50 = 6.50 €
        """
        self.lavadero.hacerLavado(prelavado_a_mano=True,
                                  secado_a_mano=False,
                                  encerado=False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 6.50, places=2)

    # ============================================================
    # CAJA BLANCA: Cobertura de caminos de fases
    # ============================================================

    def test_ciclo_completo_sin_extras(self):
        """
        Camino: sin prelavado, sin secado a mano, sin encerado.
        Debe pasar por COBRANDO -> ECHANDO_AGUA -> ENJABONANDO ->
        RODILLOS -> SECADO_MANO o SECADO_AUTOMATICO según la lógica
        y terminar inactivo.
        """
        self.lavadero.hacerLavado(False, False, False)
        fases_visitadas = [self.lavadero.fase]

        # Avanzamos hasta que termine o límite de pasos
        pasos = 0
        while self.lavadero.ocupado and pasos < 15:
            self.lavadero.avanzarFase()
            fases_visitadas.append(self.lavadero.fase)
            pasos += 1

        # Debe terminar inactivo y no ocupado
        self.assertFalse(self.lavadero.ocupado)
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        # Comprobamos que en algún momento estuvo en fase de cobro
        self.assertIn(Lavadero.FASE_COBRANDO, fases_visitadas)

    def test_ciclo_completo_con_todos_los_extras(self):
        """
        Camino: prelavado a mano, secado a mano y encerado.
        Verificamos que se recorre el flujo completo y termina inactivo.
        """
        self.lavadero.hacerLavado(True, True, True)
        fases_visitadas = [self.lavadero.fase]

        pasos = 0
        while self.lavadero.ocupado and pasos < 15:
            self.lavadero.avanzarFase()
            fases_visitadas.append(self.lavadero.fase)
            pasos += 1

        self.assertFalse(self.lavadero.ocupado)
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertIn(Lavadero.FASE_COBRANDO, fases_visitadas)
        # Debería haber pasado por PRELAVADO_MANO y RODILLOS
        self.assertIn(Lavadero.FASE_PRELAVADO_MANO, fases_visitadas)
        self.assertIn(Lavadero.FASE_RODILLOS, fases_visitadas)

    def test_avanzar_fase_sin_lavado_no_cambia_estado(self):
        """
        Si se llama a avanzarFase cuando no está ocupado,
        no debe cambiar nada.
        """
        fase_inicial = self.lavadero.fase
        ingresos_iniciales = self.lavadero.ingresos
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.fase, fase_inicial)
        self.assertEqual(self.lavadero.ingresos, ingresos_iniciales)

    def test_terminar_resetea_estado(self):
        """
        Comprobar que terminar() resetea ocupación, extras y fase.
        """
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero.terminar()
        self.assertFalse(self.lavadero.ocupado)
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)


if __name__ == "__main__":
    unittest.main()
