/* <article class="caja_producto">
            <div class="fav">X</div>
            <img src="./css/images/zapatilla.jpg" alt="Zapatilla deportiva" />
            <ul>
              <il class="gris">Calzado</il>
              <il class="nombre">Zapatilla Deportiva X-run</il>
              <il class="gris">SKU: ZR 4583</il>
              <il class="precio">$ 120.00</il>
            </ul>
</article> */

// cargo lugar donde quiero pintar los productos
const seccionDestacados = document.querySelector("#prod_destacados .productos");
const seccionAllProd = document.querySelector("#prod_all .productos");

//Limpiar html
seccionDestacados.innerHTML = "";
seccionAllProd.innerHTML = "";

function pintarProducto(producto, dom) {
  const article = document.createElement("article");
  const dest = document.createElement("div");
  const imagen = document.createElement("img");
  const lista = document.createElement("ul");
  const li_cat = document.createElement("li");
  const li_nombre = document.createElement("li");
  const li_ref = document.createElement("li");
  const li_precio = document.createElement("li");
  //Clases
  article.className = "caja_producto";
  li_cat.className = "gris";
  li_nombre.className = "nombre";
  li_ref.className = "gris";
  li_precio.className = "precio";
  dest.className = producto.destacado ? "destacado fav" : "destacado";

  //Contenido
  dest.innerHTML = `<i class="fa-solid fa-star"></i>`;
  imagen.src = producto.imagen_url; // imagen por defecto
  imagen.alt = producto.nombre;
  li_cat.textContent = producto.categoria;
  li_nombre.textContent = producto.nombre;
  li_ref.textContent = `REF: ${producto.referencia}`;
  li_precio.textContent = `$ ${producto.precio.toFixed(2)}`;

  article.append(dest, imagen, lista);
  lista.append(li_cat, li_nombre, li_ref, li_precio);
  dom.appendChild(article);
}

function pintarTodosProductos(ArrayProductos, dom_all, dom_destacado) {
  for (let producto of ArrayProductos) {
    pintarProducto(producto, dom_all);
    if (producto.destacado == true) {
      pintarProducto(producto, dom_destacado);
    }
  }
}

pintarTodosProductos(productos, seccionAllProd, seccionDestacados);
