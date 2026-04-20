"""
Tests para la API de actividades extracurriculares
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


class TestObtenerActividades:
    """Tests para el endpoint GET /activities"""

    def test_obtener_actividades_exitoso(self):
        """Debe retornar todas las actividades disponibles"""
        respuesta = client.get("/activities")
        assert respuesta.status_code == 200
        actividades = respuesta.json()
        assert isinstance(actividades, dict)
        assert "Chess Club" in actividades
        assert "Programming Class" in actividades
        assert "Gym Class" in actividades

    def test_actividad_tiene_estructura_valida(self):
        """Cada actividad debe tener los campos requeridos"""
        respuesta = client.get("/activities")
        actividades = respuesta.json()
        
        for nombre, detalles in actividades.items():
            assert "description" in detalles
            assert "schedule" in detalles
            assert "max_participants" in detalles
            assert "participants" in detalles
            assert isinstance(detalles["participants"], list)


class TestRegistroActividades:
    """Tests para el endpoint POST /activities/{activity_name}/signup"""

    def test_registrar_estudiante_exitosamente(self):
        """Debe registrar un estudiante en una actividad"""
        respuesta = client.post(
            "/activities/Basketball Team/signup?email=test@mergington.edu"
        )
        assert respuesta.status_code == 200
        datos = respuesta.json()
        assert "message" in datos
        assert "test@mergington.edu" in datos["message"]

    def test_error_al_registrarse_dos_veces(self):
        """No debe permitir registrar el mismo estudiante dos veces"""
        email = "doble@mergington.edu"
        
        # Primer registro
        respuesta1 = client.post(
            f"/activities/Tennis Club/signup?email={email}"
        )
        assert respuesta1.status_code == 200
        
        # Segundo registro con el mismo email
        respuesta2 = client.post(
            f"/activities/Tennis Club/signup?email={email}"
        )
        assert respuesta2.status_code == 400
        assert "already signed up" in respuesta2.json()["detail"]

    def test_error_actividad_no_existe(self):
        """Debe retornar error si la actividad no existe"""
        respuesta = client.post(
            "/activities/Actividad Inexistente/signup?email=test@mergington.edu"
        )
        assert respuesta.status_code == 404
        assert "not found" in respuesta.json()["detail"]

    def test_error_actividad_llena(self):
        """Debe retornar error si la actividad alcanzó su capacidad máxima"""
        # Primero, llenar completamente una actividad
        actividad = "Tennis Club"
        
        # Obtener la capacidad máxima
        respuesta_actividades = client.get("/activities")
        max_participants = respuesta_actividades.json()[actividad]["max_participants"]
        
        # Registrar estudiantes hasta llenar la actividad
        for i in range(max_participants):
            client.post(
                f"/activities/{actividad}/signup?email=usuario{i}@mergington.edu"
            )
        
        # Intentar registrar uno más
        respuesta = client.post(
            f"/activities/{actividad}/signup?email=usuario_extra@mergington.edu"
        )
        assert respuesta.status_code == 400
        assert "full" in respuesta.json()["detail"]


class TestDesregistro:
    """Tests para el endpoint DELETE /activities/{activity_name}/unregister"""

    def test_desregistrar_estudiante_exitosamente(self):
        """Debe desregistrar un estudiante de una actividad"""
        email = "desregistro@mergington.edu"
        
        # Primero registrar
        client.post(
            f"/activities/Drama Club/signup?email={email}"
        )
        
        # Luego desregistrar
        respuesta = client.delete(
            f"/activities/Drama Club/unregister?email={email}"
        )
        assert respuesta.status_code == 200
        datos = respuesta.json()
        assert "message" in datos
        assert email in datos["message"]

    def test_error_desregistrar_no_registrado(self):
        """Debe retornar error al desregistrar un estudiante que no está registrado"""
        respuesta = client.delete(
            "/activities/Art Club/unregister?email=no_registrado@mergington.edu"
        )
        assert respuesta.status_code == 400
        assert "not signed up" in respuesta.json()["detail"]

    def test_error_desregistrar_actividad_inexistente(self):
        """Debe retornar error si la actividad no existe"""
        respuesta = client.delete(
            "/activities/Actividad Inexistente/unregister?email=test@mergington.edu"
        )
        assert respuesta.status_code == 404
        assert "not found" in respuesta.json()["detail"]


class TestRutaPrincipal:
    """Tests para el endpoint GET /"""

    def test_ruta_principal_redirige(self):
        """La ruta principal debe redirigir a la página estática"""
        respuesta = client.get("/", follow_redirects=False)
        assert respuesta.status_code == 307
        assert "/static/index.html" in respuesta.headers["location"]
