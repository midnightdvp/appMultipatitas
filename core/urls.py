from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import boleta, confirmar_venta, sales, formLogin, modificar_contraseña, enviarComentario, donacion, modificarContrasenia, modificarCuenta, logout, formAgreProd, formSignUp, index, carrito, contactos, productos, producto, eliminar_producto, agregar_producto, restar_producto, limpiar_carrito, cuenta, login, modCuenta, sign_up, add_product, mod_productos, Cod_Correo, mod_Pass, Compra, modificarProducto, EliminarProducto, formAgreDirect, agregarDireccion


urlpatterns = [
    path('', index, name="inicio"),

    #URLs Tienda
    path('boleta/', boleta, name = "boleta"),
    path('carrito', carrito, name= "carrito"),
    path('contactos', contactos, name= "contactos"),
    path('productos/', productos, name='productos'),
    path('productos/<int:category_id>/', productos, name= "productos"),
    path('producto/<int:producto_id>/', producto, name= "producto"),
    path('enviarComentario/<int:id>/', enviarComentario, name="enviarComentario"),
    path('agregar_producto/<int:idProduct>/', agregar_producto, name= "Add" ),
    path('eliminar_producto/<int:idProduct>/', eliminar_producto, name= "Del" ),
    path('restar_producto/<int:idProduct>/', restar_producto, name= "Sub" ),
    path('limpiar_carrito/', limpiar_carrito, name= "Clean" ),
    
    path('Compra', Compra, name="Compra"),

    #URLs Usuario
    path('cuenta/', cuenta, name= "cuenta"),
    path('donacion', donacion, name="donacion"),
    path('login/', formLogin, name= "formLogin"),
    path('mod_cuenta/', modCuenta, name= "mod_cuenta"),
    path('modificarCuenta/<int:idUser>/', modificarCuenta, name= "modificarCuenta"),
    path('modificar_contraseña/', modificar_contraseña, name="modificar_contraseña"),
    path('sign_up/', sign_up, name= "sign_up"),
    path('formSignUp/', formSignUp, name="formSignUp"),
    path('logout/', logout, name='logout'),
    
    path('formAgreDirect/', formAgreDirect, name="formAgreDirect"),
    path('agregarDireccion/', agregarDireccion, name="agregarDireccion"),
    
    #URLs Recuperar
    path('Cod_Correo/', Cod_Correo, name= "Cod_Correo"),
    path('mod_Pass/', mod_Pass, name= "mod_Pass"),
    path('modificarContrasenia/<int:idUser>/', modificarContrasenia, name= "modificarContrasenia"),

    #URLs Admin
    path('add_product/',add_product, name= "add_product"),
    path('formAgreProd/', formAgreProd, name="formAgreProd"),
    path('mod_productos/', mod_productos, name= "mod_productos"),
    path('modificarProducto/<int:id>', modificarProducto, name= "modificarProducto"),
    path('EliminarProducto/<int:id>', EliminarProducto, name= "EliminarProducto"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


