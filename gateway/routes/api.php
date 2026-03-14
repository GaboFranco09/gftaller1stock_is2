<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\VentaController;

Route::post('/register', [AuthController::class, 'register']);
Route::post('/login',    [AuthController::class, 'login']);

// JWT 
Route::middleware('auth:api')->group(function () {
    Route::post('/logout', [AuthController::class, 'logout']);
    Route::get('/me',      [AuthController::class, 'me']);
});

Route::middleware('auth:api')->group(function () {
    Route::post('/venta',       [VentaController::class, 'registrarVenta']);
    Route::get('/ventas',       [VentaController::class, 'consultarVentas']);
    Route::get('/ventas/{id}',  [VentaController::class, 'consultarVenta']);
});