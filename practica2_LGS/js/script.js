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
  const boton_dest = document.createElement("button");
  const imagen = document.createElement("img");
  const lista = document.createElement("ul");
  const li_cat = document.createElement("li");
  const li_nombre = document.createElement("li");
  const li_ref = document.createElement("li");
  const li_precio = document.createElement("li");

  // <article class="caja_producto">
  //           <div class="destacado"><button class="destacar"><i class="fa-solid fa-star"></button></i></div>
  //           <div class="imagen"></div>
  //           <ul>
  //             <li class="gris">Categoria</li>
  //             <li class="nombre">Nombre</li>
  //             <li class="gris">Referencia</li>
  //             <li class="precio">$ Precio</li>
  //           </ul>
  //         </article>

  //Clases
  article.className = "caja_producto";
  li_cat.className = "gris";
  li_nombre.className = "nombre";
  li_ref.className = "gris";
  li_precio.className = "precio";
  dest.className = producto.destacado ? "destacado fav" : "destacado";
  boton_dest.className = "b_destacar";
  article.classList.add(producto.sku);
  boton_dest.classList.add(producto.sku);

  //Contenido
  boton_dest.innerHTML = `<i class="fa-solid fa-star"></i>`;
  boton_dest.addEventListener("click", () => {
    console.log("Button clicked!");
  });
  imagen.src = producto.imagen_url; // imagen por defecto
  imagen.alt = producto.nombre;
  li_cat.textContent = producto.categoria;
  li_nombre.textContent = producto.nombre;
  li_ref.textContent = `SKU: ${producto.sku}`;
  li_precio.textContent = `$ ${producto.precio.toFixed(2)}`;

  dest.append(boton_dest);
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

// parte 2

const form = document.querySelector("#filtrar_producto");

function obtenerDatosForm(event) {
  event.preventDefault();
  //array con filtros
  const filtros_prod = {
    nombre: event.target.nombre_producto.value,
    precio_min: Number(event.target.r_precio_min.value),
    precio_max: Number(event.target.r_precio_max.value),
  };

  // filtro de productos que cumplen la  busqueda:
  filtrar_producto(filtros_prod);

  event.target.reset();
}

/////////////////////77

function filtrar_producto(filtros_prod) {
  // filtro de productos que cumplen la  busqueda:

  let prod_filtrados = productos.filter(
    (producto) =>
      producto.nombre
        .toLowerCase()
        .includes(filtros_prod.nombre.toLowerCase()) &&
      filtros_prod.precio_min < producto.precio &&
      producto.precio < filtros_prod.precio_max
  );

  //Limpiar html
  seccionDestacados.innerHTML = "";
  seccionAllProd.innerHTML = "";

  pintarTodosProductos(prod_filtrados, seccionAllProd, seccionDestacados);
}

form.addEventListener("submit", obtenerDatosForm);

// parte 3 ?

// function destacar(event) {
//   const ClasePadre = event.target.parentNode.classList[1];
//   producto.destacado != producto.destacado;
// productos.push(producto) //hay que actualizar el arreglo de json -> buscar como sobreescribir objeto en lugar de añadirlo
//   pintarTodosProductos(productos, seccionAllProd, seccionDestacados);
// }
