//impoerts
import { filtrar_producto } from "../js/logic.js";
import { productos } from "../js/data.js";
// o require('../js/data.js')

// TODOS los test para filtrar_producto
describe("filtrar_producto", () => {
  // TEST FILTRADO POR NOMBRE
  describe("filtrado por nombre", () => {
    test("debería encontrar producto por nombre exacto", () => {
      const filtros = {
        nombre: "Zapatilla Deportiva X-Run",
        precio_min: 0,
        precio_max: 0,
      };

      const resultado = filtrar_producto(filtros, productos);

      expect(resultado[0].nombre).toBe("Zapatilla Deportiva X-Run");
      expect(resultado[0].sku).toBe("CC01-01");
    });

    test("debería encontrar productos por nombre parcial", () => {
      const filtros = {
        nombre: "Mochila",
        precio_min: 0,
        precio_max: 0,
      };

      const resultado = filtrar_producto(filtros, productos);

      expect(resultado.map((p) => p.nombre)).toEqual(
        expect.arrayContaining([
          "Mochila Cuero Sintético",
          "Mochila Laptop Legacy",
        ]),
      );
    });

    test("debería ser case insensitive", () => {
      const filtros = {
        nombre: "zapatilla deportiva", // todo en minúsculas
        precio_min: 0,
        precio_max: 0,
      };

      const resultado = filtrar_producto(filtros, productos);

      expect(resultado[0].nombre).toBe("Zapatilla Deportiva X-Run");
    });

    test('filtro por categoria, debería encontrar productos de "Electrónica"', () => {
      const filtros = {
        nombre: "Electrónica",
        precio_min: 0,
        precio_max: 0,
      };

      const resultado = filtrar_producto(filtros, productos);

      expect(resultado.map((p) => p.nombre)).toEqual(
        expect.arrayContaining([
          "Smartwatch Active Pro",
          "Audifonos Bluetooth Xtreme",
        ]),
      );
    });
  });

  // TESTS DE FILTRADO POR PRECIO
  describe("filtrado por precio", () => {
    test("debería filtrar productos entre $100 y $200", () => {
      const filtros = {
        nombre: "",
        precio_min: 100,
        precio_max: 200,
      };

      const resultado = filtrar_producto(filtros, productos);

      // Productos entre 100 y 200:
      // Zapatilla Deportiva X-Run ($128), Mochila Laptop Legacy ($145), Collar Plata Esterlina ($150)
      expect(resultado.map((p) => p.nombre)).toEqual(
        expect.arrayContaining([
          "Zapatilla Deportiva X-Run",
          "Mochila Laptop Legacy",
          "Collar Plata Esterlina",
        ]),
      );
    });

    test('debería manejar precio máximo = 0 como "infinito" (999999)', () => {
      const filtros = {
        nombre: "",
        precio_min: 300,
        precio_max: 0, // Debería tratarse como 999999
      };

      const resultado = filtrar_producto(filtros, productos);

      // Productos > 300: Stilletto Legend Black ($305), Bolso City 25 ($293 NO, es menor),
      // Bolso New Gen ($757), Smartwatch Active Pro ($299 NO, es menor)
      expect(resultado.map((p) => p.nombre)).toEqual(
        expect.arrayContaining(["Stilletto Legend Black", "Bolso New Gen"]),
      );
    });

    test("debería filtrar productos económicos (menos de $50)", () => {
      const filtros = {
        nombre: "",
        precio_min: 0,
        precio_max: 50,
      };

      const resultado = filtrar_producto(filtros, productos);

      // Productos < 50: Balón de Fútbol Pro ($40), Cinturón Cuero Negro ($45)
      expect(resultado.map((p) => p.precio)).toEqual(
        expect.arrayContaining([40.0, 45.0]),
      );
    });

    test("debería devolver array vacío si precio mínimo > precio máximo", () => {
      const filtros = {
        nombre: "",
        precio_min: 500,
        precio_max: 100,
      };

      const resultado = filtrar_producto(filtros, productos);

      expect(resultado).toEqual([]);
    });
  });

  // TESTS DE COMBINACIÓN DE FILTROS
  describe("combinación de filtros", () => {
    test("debería combinar filtros de nombre y precio", () => {
      const filtros = {
        nombre: "Bolso",
        precio_min: 200,
        precio_max: 800,
      };

      const resultado = filtrar_producto(filtros, productos);

      // "Bolso" con precio entre 200-800: Bolso City 25 ($293), Bolso New Gen ($757)
      expect(resultado.map((p) => p.nombre)).toEqual(
        expect.arrayContaining(["Bolso City 25", "Bolso New Gen"]),
      );
    });

    test("debería encontrar productos con entre 250 y 350 que ocntengan la palabra pro", () => {
      const filtros = {
        nombre: "Pro", // Aparece en "Smartwatch Active Pro"
        precio_min: 250,
        precio_max: 350,
      };

      const resultado = filtrar_producto(filtros, productos);

      // "Pro" con precio 250-350: Smartwatch Active Pro ($299)
      expect(resultado[0].nombre).toBe("Smartwatch Active Pro");
      expect(resultado[0].precio).toBe(299.0);
    });
  });

  // TESTS DE CASOS ESPECIALES
  describe("casos especiales y manejo de errores", () => {
    test("debería devolver array vacio si no hay coincidencias", () => {
      const filtros = {
        nombre: "Producto Inexistente XYZ",
        precio_min: 0,
        precio_max: 0,
      };

      const resultado = filtrar_producto(filtros, productos);

      expect(resultado).toHaveLength(0);
      expect(resultado).toEqual([]);
    });

    test("debería mostrar todos los productos con filtros vacíos", () => {
      const filtros = {
        nombre: "",
        precio_min: 0,
        precio_max: 0,
      };

      const resultado = filtrar_producto(filtros, productos);

      expect(resultado).toHaveLength(15); // Todos los productos del array
    });
  });
});
