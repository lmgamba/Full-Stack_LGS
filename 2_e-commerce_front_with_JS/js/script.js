//importar logica
import { filtrar_producto, destacar } from "./logic.js";
import { productos } from "./data.js";

// cargo lugar donde quiero pintar los productos
const seccionDestacados = document.querySelector("#prod_destacados .productos");
const seccionAllProd = document.querySelector("#prod_all .productos");

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
  boton_dest.addEventListener("click", actualizar_destacados);
  imagen.src = producto.imagen_url;
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

function pintarTodosProductos(
  productosArray,
  dom_all,
  dom_destacado,
  caso = "sin_destacados",
) {
  switch (caso) {
    case "all_products": // usar en caso que se quiera re-pintar toda la pagina
      //Limpiar html
      dom_all.innerHTML = "";
      dom_destacado.innerHTML = "";
      for (let producto of productosArray) {
        pintarProducto(producto, dom_all);
        if (producto.destacado == true) {
          pintarProducto(producto, dom_destacado);
        }
      }
    case "sin_destacados": // usar si no se quieren sobreescribir los destacados
      //Limpiar html, solo all
      dom_all.innerHTML = "";
      for (let producto of productos) {
        pintarProducto(producto, dom_all);
      }
  }
}

// INICIALIZAR EL ARRAY
let productosCopy = [...productos]; // Copia inicial
pintarTodosProductos(
  productosCopy,
  seccionAllProd,
  seccionDestacados,
  "all_products",
);

// parte 2 : formulario
// select form by id
const form = document.querySelector("#filtrar_producto");

function obtenerDatosForm(event) {
  event.preventDefault();
  //array con filtros
  const filtros_prod = {
    nombre: event.target.nombre_producto.value,
    precio_min: Number(event.target.r_precio_min.value),
    precio_max: Number(event.target.r_precio_max.value),
  };

  // llama a la funcion que filtra los productos que cumplen la  busqueda:
  let prod_filtrados = filtrar_producto(filtros_prod);

  // mensaje para informar al usuario que no hay productos que cumplan con ese filtro
  if (prod_filtrados[0] === undefined) {
    seccionAllProd.innerHTML = `<span style="font-style: italic; color: gray;" > No hay productos que cumplan con la búsqueda, intenta con otro filtro </span>`;
  } else {
    // mostrar solo productos filtrados SIN TOCAR LOS DESTACADOS
    pintarTodosProductos(
      prod_filtrados,
      seccionAllProd,
      seccionDestacados,
      "sin_destacados",
    );
  }

  event.target.reset();
}

form.addEventListener("submit", obtenerDatosForm);

// parte (?) : funcionamiento del boton destacado
// cambiar estado destacado si  clic -> producto.destacado = !producto.destacado
//actualizar el arreglo de json?

function actualizar_destacados(event) {
  // 1. buscar en la clase del boton la referencia del producto

  const ClaseSKU = event.target.parentNode.classList[1];
  // cambiar destacado con ese sku a true
  destacar(ClaseSKU, productosCopy);

  //actualizar los productos que se muestran como destacados
  pintarTodosProductos(
    productosCopy,
    seccionAllProd,
    seccionDestacados,
    "all_products",
  );
}
