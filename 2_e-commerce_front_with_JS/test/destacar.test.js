import { destacar } from "../js/logic.js";
import { productos } from "../js/data.js";

let productosTest = [...productos];

beforeEach(async () => {
  productosTest = [...productos];
});

describe("destacar", () => {
  describe("casos exitosos", () => {
    test("debería cambiar destacado de false a true", () => {
      const sku = "CC02-02"; // Stilletto (destacado: false)
      const productosOriginal = [...productosTest];

      const productoACambiar = productosOriginal.find((p) => p.sku === sku);

      const resultado = destacar(sku, productosOriginal);

      // Verificar que el producto específico cambió
      const productoCambiado = resultado.find((p) => p.sku === sku);
      expect(productoCambiado.destacado).toBe(true);

      // Verificar que otros productos NO cambiaron
      const otroProducto = resultado.find((p) => p.sku === "CC01-01");
      expect(otroProducto.destacado).toBe(true); // Sigue igual

      expect(productoACambiar.destacado).toBe(false); // Original debe seguir false// Verificar que NO se mutó el array original => parece que si lo muta #TODO
    });

    test("debería cambiar destacado de true a false", () => {
      const sku = "CC01-01"; // Zapatilla (destacado: true)

      const resultado = destacar(sku, productosTest);

      const productoCambiado = resultado.find((p) => p.sku === sku);
      expect(productoCambiado.destacado).toBe(false);
    });

    test("debería mantener las otras propiedades del producto", () => {
      const sku = "BB01-03";

      const resultado = destacar(sku, productosTest);

      const productoCambiado = resultado.find((p) => p.sku === sku);

      // Todas las demás propiedades deben mantenerse
      expect(productoCambiado.nombre).toBe("Bolso City 25");
      expect(productoCambiado.categoria).toBe("Bolsos");
      expect(productoCambiado.precio).toBe(293.0);
      expect(productoCambiado.sku).toBe("BB01-03");
    });

    test("debería devolver un NUEVO array (no mutar el original)", () => {
      const sku = "HH02-17";
      const productosOriginal = [...productosTest];
      const copiaOriginal = [...productosOriginal]; // Para comparar después

      const resultado = destacar(sku, productosOriginal);

      // El resultado debe ser un array diferente
      expect(resultado).not.toBe(productosOriginal);

      // El original debe permanecer igual
      expect(productosOriginal).toEqual(copiaOriginal);

      // El resultado debe tener la misma longitud
      expect(resultado.length).toBe(productosOriginal.length);
    });
  });

  describe("manejo de errores", () => {
    test("debería lanzar error si SKU no existe", () => {
      const skuInexistente = "SKU-INEXISTENTE-999";

      expect(() => {
        destacar(skuInexistente, productosTest);
      }).toThrow(`Producto con SKU ${skuInexistente} no encontrado`);
    });

    test("debería lanzar error si SKU es undefined", () => {
      expect(() => {
        destacar(undefined, productosTest);
      }).toThrow("Parámetros inválidos");
    });

    test("debería lanzar error si array de productos es undefined", () => {
      expect(() => {
        destacar("CC01-01", undefined);
      }).toThrow("Parámetros inválidos");
    });

    test("debería lanzar error si array de productos está vacío", () => {
      expect(() => {
        destacar("CC01-01", []);
      }).toThrow("Producto con SKU CC01-01 no encontrado");
    });
  });

  describe("casos especiales", () => {
    test("debería funcionar con múltiples cambios secuenciales", () => {
      let productosActualizados = [...productosTest];

      // Primer cambio
      productosActualizados = destacar("CC01-01", productosActualizados);
      expect(
        productosActualizados.find((p) => p.sku === "CC01-01").destacado,
      ).toBe(false);

      // Segundo cambio (mismo producto)
      productosActualizados = destacar("CC01-01", productosActualizados);
      expect(
        productosActualizados.find((p) => p.sku === "CC01-01").destacado,
      ).toBe(true);

      // Tercer cambio (otro producto)
      productosActualizados = destacar("BB01-03", productosActualizados);
      expect(
        productosActualizados.find((p) => p.sku === "BB01-03").destacado,
      ).toBe(true);
    });

    test("debería manejar SKU con caracteres especiales", () => {
      const productosConSKUComplejo = [
        { sku: "PROD-001-A", destacado: false, nombre: "Producto A" },
        { sku: "PROD_002_B", destacado: true, nombre: "Producto B" },
      ];

      const resultado = destacar("PROD-001-A", productosConSKUComplejo);

      expect(resultado.find((p) => p.sku === "PROD-001-A").destacado).toBe(
        true,
      );
    });

    test("debería buscar coincidencia exacta de SKU (no parcial)", () => {
      // Si buscas "CC01" no debería encontrar "CC01-01"
      expect(() => {
        destacar("CC01", productosTest); // Busca "CC01", existe "CC01-01"
      }).toThrow("Producto con SKU CC01 no encontrado");
    });
  });

  describe("integración con el sistema", () => {
    test("el estado destacado afecta al filtrado visual (lógica de negocio)", () => {
      // Este test verifica la lógica de negocio:
      // Los productos destacados deberían mostrarse en sección especial

      const productosConDestacados = [...productosTest];
      const destacadosAntes = productosTest.filter((p) => p.destacado).length; // 2

      // Destacar un producto
      const conDestacado = destacar("BB01-03", productosConDestacados);

      // Verificar que ahora hay 3 productos destacados en lugar de 2
      const destacadosDespues = conDestacado.filter((p) => p.destacado).length; // 3
      expect(destacadosDespues).toBe(destacadosAntes + 1);

      // El producto específico ahora está destacado
      const bolsoDestacado = conDestacado.find((p) => p.sku === "BB01-03");
      expect(bolsoDestacado.destacado).toBe(true);
    });
  });
});
