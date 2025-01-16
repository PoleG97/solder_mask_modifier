# solder_mask_modifier
Este plugin permite modificar la "solder mask" de todos los PADS de una lista de componentes.

## Problema que soluciona
Está pensado para solucionar el error de DRC **"Solder mask aperture bridges items with different nets"**. 

Una de las formas en la que la gente está resolviendo este problema, es modificando la severidad de las DRC o permitiendo los gridges.

Este plugin permite eliminar el problema, no sólo parchearlo.

![](img/image.png)

## Solución en la que se basa
Para arreglarlo de forma eficaz, habría que
1. Abrir el editor de la huella del componente
2. En el editor, modificar cada uno de los pads
3. Guardar el cambio

El problema, es que esto es muy largo y aburrido de hacer, para ello este plugin

# Instalación
Copiar `solder_mask_modifier.py` a la ruta `scripting/plugins`, en mi caso sería en esta ruta

> `C:\Users\jairo\Documents\KiCad\8.0\scripting\plugins`

# Uso
Con el `.py` en la ruta correcta, abrir el editor de pcb y ejecutar el plugin

`tools > external plugins > Sodler Mask Modifier`

Ahora, ponemos el nombre de los componentes (respetando mayúsculas y minúsculas), y en caso de ser varios componentes, ponerlos seguidos de comas y sin espacios `U3,CLK2,j2`. Luego se establece el tamaño de la solder mask (normalmente 0).

Por último, `Aplicar cambios`