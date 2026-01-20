function filtrar_producto(filtros_prod, productosArray) {
  if (filtros_prod.precio_max === 0) {
    filtros_prod.precio_max = 999999; //max default, en caso que no se llene el input del precio max
  }

  //productos resultantes de la busqueda con los filtros recibidos
  //filter: (producto) =>  (nombre filtro y producto en lowercase es igual) && (pmin < precio <pmax)

  const busqueda = filtros_prod.nombre.toLowerCase(); // input string del usuario

  let prod_filtrados = productosArray.filter(
    (producto) =>
      (producto.nombre.toLowerCase().includes(busqueda) ||
        producto.categoria.toLowerCase().includes(busqueda)) &&
      filtros_prod.precio_min < producto.precio &&
      producto.precio < filtros_prod.precio_max,
  );

  return prod_filtrados;
}

function destacar(ClaseSKU, productosArray) {
  //Validación basica
  if (!ClaseSKU || !productosArray) {
    throw new Error("Parámetros inválidos");
  }

  // Crea una COPIA del array para no mutar el original
  const productosCopy = [...productosArray];

  // usando find buscar el encontrar indice del producto de con la misma referencia
  const index_producto = productosCopy.findIndex(
    (producto) => producto.sku === ClaseSKU,
  );

  if (index_producto === -1) {
    throw new Error(`Producto con SKU ${ClaseSKU} no encontrado`);
  }

  // Invertir el estado de destacado
  productosCopy[index_producto].destacado =
    !productosCopy[index_producto].destacado;

  return productosCopy;
}
// Exporta
export { filtrar_producto, destacar };
