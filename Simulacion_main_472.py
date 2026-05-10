#==============================================================================
# SIMULACIÓN — 10 OPERACIONES DEL SISTEMA
# Demuestra: manejo de excepciones, polimorfismo y estabilidad del sistema
#==============================================================================

def main():
    print("=" * 65)
    print("   SISTEMA DE GESTIÓN - SOFTWARE FJ")
    print("   Fase 4 - Programación 213023 - UNAD - Grupo 472")
    print("   Simulación de 10 operaciones")
    print("=" * 65)

    sistema = SistemaGestion()

    # ------------------------------------------------------------------
    # OP 1 — Registro INVÁLIDO: email sin formato correcto
    # Demuestra: ClienteError lanzado desde set_correo(), try/except/finally
    # ------------------------------------------------------------------
    print("\n[OP 1] Registro inválido — email sin formato correcto:")
    sistema.registrar_cliente("C001", "Pedro Gomez", "correomal", "3001234567")

    # ------------------------------------------------------------------
    # OP 2 — Registro VÁLIDO de primer cliente
    # Demuestra: try/except/else/finally en registrar_cliente()
    # ------------------------------------------------------------------
    print("\n[OP 2] Registro válido — primer cliente:")
    c1 = sistema.registrar_cliente(
        "C002", "Juan Perez", "juan@email.com", "3001234567"
    )

    # ------------------------------------------------------------------
    # OP 3 — Registro INVÁLIDO: nombre vacío
    # Demuestra: ClienteError lanzado desde set_nombre()
    # ------------------------------------------------------------------
    print("\n[OP 3] Registro inválido — nombre vacío:")
    sistema.registrar_cliente("C003", "", "test@email.com", "3009999999")

    # ------------------------------------------------------------------
    # OP 4 — Registro VÁLIDO de segundo cliente
    # Demuestra: sistema sigue estable tras los errores anteriores
    # ------------------------------------------------------------------
    print("\n[OP 4] Registro válido — segundo cliente:")
    c2 = sistema.registrar_cliente(
        "C004", "Carlos Ruiz", "carlos@email.com", "3007654321"
    )

    # ------------------------------------------------------------------
    # OP 5 — Crear los tres servicios y demostrar polimorfismo en describir()
    # Demuestra: instanciación de las tres subclases de Servicio,
    # polimorfismo: mismo método describir(), tres salidas distintas
    # ------------------------------------------------------------------
    print("\n[OP 5] Crear servicios — polimorfismo en describir():")
    sala = asesoria = equipo = None
    try:
        sala     = ReservaSala("Sala Innovación", 50_000, 15)
        asesoria = AsesoriaEspecializada("Asesoría Python", 80_000, "Dr. García")
        equipo   = AlquilerEquipo("Portátiles HP", 15_000, "Laptop", 50_000)

        sistema.agregar_servicio(sala)
        sistema.agregar_servicio(asesoria)
        sistema.agregar_servicio(equipo)

        print("\n  Polimorfismo — mismo método describir(), tres resultados distintos:")
        for s in [sala, asesoria, equipo]:
            print(f"  → {s.describir()}")

    except ServicioError as e:
        print(f"  ❌ {e}")

    # ------------------------------------------------------------------
    # OP 6 — Reserva INVÁLIDA: asesoría supera límite de horas
    # Demuestra: validar_parametros() en AsesoriaEspecializada,
    # encadenamiento de excepciones ServicioError → ReservaError
    # ------------------------------------------------------------------
    print("\n[OP 6] Reserva inválida — asesoría supera límite de horas (máx 4h):")
    if c1 and asesoria:
        r_invalida = sistema.crear_reserva(c1, asesoria, 6)  # 6h > HORAS_MAX=4
        if r_invalida:
            try:
                r_invalida.procesar()
            except ReservaError as e:
                print(f"  ❌ Reserva bloqueada: {e}")

    # ------------------------------------------------------------------
    # OP 7 — Reserva INVÁLIDA: servicio no disponible
    # Demuestra: validacion de disponibilidad en crear_reserva()
    # ------------------------------------------------------------------
    print("\n[OP 7] Reserva inválida — servicio marcado como no disponible:")
    if c1 and sala:
        sala.set_disponible(False)
        sistema.crear_reserva(c1, sala, 3)
        sala.set_disponible(True)  # restaurar para las siguientes ops

    # ------------------------------------------------------------------
    # OP 8 — Reserva VÁLIDA con IVA y descuento
    # Demuestra: calcular_costo() con parámetros opcionales (método sobrecargado),
    # polimorfismo en confirmar(), try/except/else/finally completo
    # ------------------------------------------------------------------
    print("\n[OP 8] Reserva válida — sala 3h con IVA 19% y descuento 10%:")
    r1 = None
    if c1 and sala:
        r1 = sistema.crear_reserva(c1, sala, 3)
        if r1:
            try:
                costo = r1.confirmar(con_iva=True, descuento=10)
                print(f"  ✅ Reserva confirmada — Costo final: ${costo:,.2f}")
            except ReservaError as e:
                print(f"  ❌ {e}")

    # ------------------------------------------------------------------
    # OP 9 — Operación NO PERMITIDA: confirmar una reserva ya confirmada
    # Demuestra: control de estado en confirmar(), ReservaError
    # ------------------------------------------------------------------
    print("\n[OP 9] Operación no permitida — confirmar reserva ya confirmada:")
    if r1:
        try:
            r1.confirmar()
        except ReservaError as e:
            print(f"  ❌ Operación bloqueada: {e}")

    # ------------------------------------------------------------------
    # OP 10 — Operación NO PERMITIDA: cancelar una reserva dos veces
    # Demuestra: control de estado en cancelar(), try/except/finally,
    # sistema sigue estable tras el segundo intento fallido
    # ------------------------------------------------------------------
    print("\n[OP 10] Operación no permitida — cancelar reserva dos veces:")
    r2 = None
    if c2 and equipo:
        r2 = sistema.crear_reserva(c2, equipo, 2)
        if r2:
            try:
                r2.cancelar()
                print("  ✅ Primera cancelación exitosa")
                r2.cancelar()  # segundo intento — debe fallar controladamente
            except ReservaError as e:
                print(f"  ❌ Segunda cancelación bloqueada: {e}")

    # ------------------------------------------------------------------
    # CIERRE
    # ------------------------------------------------------------------
    print("\n" + "=" * 65)
    print("   Simulación completada — sistema estable en todas las operaciones")
    print("   Registro completo en: logs/sistema.log")
    print("=" * 65)


#==============================================================================
# PUNTO DE ENTRADA
#==============================================================================
if __name__ == "__main__":
    main()