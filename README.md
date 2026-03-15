# Sistema de Ventas con Microservicios
**Materia:** Ingeniería de Software II  
**Estudiante:** Gabriel Franco  
**Universidad:** Universidad Nacional de Colombia Sede Manizales 
**Fecha:** 15 de Marzo 2026  

## Descripción
Sistema de ventas basado en arquitectura de microservicios. Gestiona autenticación, 
inventario y registro de ventas a través de tres servicios independientes coordinados 
por un API Gateway.

## Arquitectura
| Componente | Tecnología | Puerto | Base de datos |
|---|---|---|---|
| API Gateway | Laravel 11 | 8000 | MySQL |
| MS Inventario | Flask | 5001 | Firebase Realtime DB |
| MS Ventas | Express | 5002 | MongoDB |

## Requisitos previos
- PHP 8.x + Composer + Laragon
- Node.js 18+
- Python 3.10+
- Git
- MongoDB local (puerto 27017)
- Cuenta Firebase con Realtime Database activa

## Instalación

### 1. Clonar el repositorio
git clone https://github.com/GaboFranco09/gftaller1stock_is2.git

### 2. Configurar variables de entorno
Copiar y completar el .env en cada servicio:
cp gateway/.env.example gateway/.env
cp ms-inventario/.env.example ms-inventario/.env
cp ms-ventas/.env.example ms-ventas/.env

### 3. Levantar los servicios

**Gateway:**
cd gateway
composer install
php artisan serve --host=127.0.0.1 --port=8000

**MS Inventario:**
cd ms-inventario
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python run.py

**MS Ventas:**
cd ms-ventas
npm install
npm run dev

## Documentación completa
Ver carpeta `/docs` para el documento Word con arquitectura, 
endpoints y flujo detallado del sistema.

## Repositorio
https://github.com/GaboFranco09/gftaller1stock_is2