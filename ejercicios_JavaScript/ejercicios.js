//////////////////////////////////////
//8 FACTORIAL

// let n = Number(prompt("Dime un numero"));

// function factorial(n) {
//   f = 1;
//   for (i = 1; i <= n; i++) {
//     f *= i;
//   }
//   return f;
// }

// if (!(isNaN(n) || n < 0)) {
//   console.log(factorial(n));
// } else {
//   alert("Por favor ingresa un número valido");
// }

//////////////////////////////////////
//9 Contador de letras (como hacerlo sin len dentro del for?)

// let input = prompt("Dime algo");

// function contarLetras(a) {
//   let n = 0;
//   for (i = 0; i < a.length; i++) {
//     if (a[i] !== " ") {
//       n++;
//     }
//   }

//   return n;
// }

// if (typeof input == "string") {
//   console.log(contarLetras(input));
// } else {
//   alert("Por favor ingresa un texto valido");
// }

//////////////////////////////////////
//10. Vocales en una palabra

// Pide una palabra y cuenta cuántas vocales contiene. (investigar como sabes que es una vocal con condiciones)

//////////////////////////////////////
// EJERCICIO EN CLASE funcion potencia sin  usar el operador potencia

// let n = Number(prompt("Dime un numero"));
// base = 2;

// function potencia(b, e) {
//   p = 1;
//   for (i = 1; i <= e; i++) {
//     p *= b;
//   }
//   return p;
// }

// if (!(isNaN(n) || n < 0)) {
//   console.log(potencia(base, n));
// } else {
//   alert("Por favor ingresa un número valido");
// }

//////////////////////////////////////
//11. Potencias sucesivas
// Pide un número y muestra sus potencias desde el exponente 1 hasta 5 (por ejemplo, 2¹, 2², 2³, 2⁴, 2⁵).

// let b = Number(prompt("Dime un numero"));

// if (isNaN(b) || b < 0) {
//   alert("Por favor ingresa un número valido");
// }

// p = 1;
// for (i = 1; i <= 5; i++) {
//   p *= b;
//   console.log(p);
// }

// 14. quiero una funcion que me permita pintar por pantalla un cuadrado o un circulo, del ancho que queramos y el color que queramos.

// let fig = prompt("Que figura quieres: circulo, cuadrado?");
// let ancho = parseInt(
//   Number(
//     prompt("Cuantos pixeles quieres que tenga tu figura de ancho (o diametro)?")
//   )
// );
// let color_inp = prompt("De que color queires la figura?: red, blue, green");

// const pintar = function (figura, ancho, color) {
//   let radio = figura === "circulo" ? "50%" : "0%";
//   document.write(
//     `<div style="width: ${ancho}px; height: ${ancho}px;background-color: ${color}; border-radius: ${radio};"></div>`
//   );
// };

// pintar(fig, ancho, color_inp);

// 17 Quiero hacer una aplicacion que me permita calcular y sacar por patalla PVP de un producto
//     ejemplo: si tengo un producto que a mi me cuesta 1000 y quiero ganarle el 50% y pagar el iva
// 1000 + 500 = 1500 -> 21 % -> 1815

// let costo = Number(prompt("Cuanto te cuesta el producto?"));

// let ganancia = Number(prompt("Cuanto te Que porcentaje quieres ganarle?"));

// function calculoPVP(costo, ganancia) {
//   let PVP = costo * 1.21 * (1 + ganancia / 100); //1.21 ES EL IVA DE 21%
//   document.write(
//     `<div style="padding: 10px; background-color: bisque; border-radius: 5px;border: 5px solid;">El PVP de tu producto deberia ser ${PVP}</div>`
//   );
// }

// calculoPVP(costo, ganancia);

// 18. Quiero un programa que me permita saber si un numero es primo o no es primo.Un numero es primo si y solo si el numero es divisible por 1 o por si mismo, recorriendo todos los numeros desde el numero dado a hasta 1.

// let n = parseInt(Number(prompt("Dime un numero entero")));

// function primo(n) {
//   let esprimo = true;
//   for (i = n - 1; i > 1; i--) {
//     if (n % i === 0) {
//       console.log(n % i);
//       esprimo = false;
//     }
//   }
//   return esprimo;
// }

// resultado = primo(n);

// document.write(
//   `<div style="padding: 10px; width: 50%; background-color: bisque;margin-bottom:15px;5">El número ${n} es primo? </div>
//     <span style="padding: 10px; width: 50%; background-color: bisque; left:30px;7
//      border-radius: 5px;border: 5px solid;font-size: larger;
//         font-weight: bold;"> ${resultado}  </span>`
// );

// 19. Hacer una funcion que me permita saber si una frase es palindromo. Una frase es palindromo si se lee igual de derecha a izquierda que de izquierda a derecha
//     ana = ana
//     "Somos o no somos"
//     "Anita lava la tina"
//     "La ruta natural"
// "Amor a Roma"

let input = prompt("Dime algo");

function palindromo(frase) {
  let len = frase.length - 1;
  console.log(frase[len - 2]);
  espalindromo = true;
  for (i = 0; i < len; i++) {
    //   console.log(frase[i]);
    if (frase[i] !== " ") {
      // console.log("NO es espacio" + i);
      if (frase[i] != frase[len - i]) {
        console.log(`Comparando ${frase[i]} vesrsus ${frase[len - i]}`);
        espalindromo = false;
        break;
      }
    }
  }

  return espalindromo;
}

resultado = palindromo(input);

document.write(
  `<div style="padding: 10px; width: 50%;margin-bottom:15px;5"> La frase " ${input} " es palindromo? </div>
    <span style="padding: 10px; width: 50%; background-color: bisque; margin 15px;
     border-radius: 5px;border: 5px solid;font-size: larger;
        font-weight: bold;"> ${resultado}  </span>`
);

if (typeof input == "string") {
  console.log(palindromo(input));
} else {
  alert("Por favor ingresa un texto valido");
}
