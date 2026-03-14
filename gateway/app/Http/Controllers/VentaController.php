<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class VentaController extends Controller
{
    private $inventarioUrl;
    private $ventasUrl;

    public function __construct()
    {
        $this->inventarioUrl = env('MS_INVENTARIO_URL');
        $this->ventasUrl     = env('MS_VENTAS_URL');
    }

    public function registrarVenta(Request $request)
    {
        $request->validate([
            'producto_id' => 'required|string',
            'cantidad'    => 'required|integer|min:1',
        ]);

        $productoId = $request->producto_id;
        $cantidad   = $request->cantidad;
        $usuarioId  = auth('api')->user()->id;

        //Stock Flask
        try {
            $stockResponse = Http::timeout(3)->get(
                "{$this->inventarioUrl}/stock/{$productoId}",
                ['cantidad' => $cantidad]
            );
        } catch (\Exception $e) {
            return response()->json([
                'error' => 'Servicio de inventario no disponible'
            ], 503);
        }

        $stockData = $stockResponse->json();

        if (!$stockData || $stockData['disponible'] !== 1) {
            return response()->json([
                'error' => 'Producto sin stock suficiente'
            ], 400);
        }

        // VENTA EXPRESS
        try {
            $productoResponse = Http::timeout(3)->get(
                "{$this->inventarioUrl}/productos/{$productoId}"
            );
            $producto    = $productoResponse->json();
            $precioTotal = $producto['precio'] * $cantidad;

            $ventaResponse = Http::timeout(3)->post(
                "{$this->ventasUrl}/ventas",
                [
                    'usuario_id'   => (string) $usuarioId,
                    'producto_id'  => $productoId,
                    'cantidad'     => $cantidad,
                    'precio_total' => $precioTotal,
                ]
            );
        } catch (\Exception $e) {
            return response()->json([
                'error' => 'Servicio de ventas no disponible'
            ], 503);
        }

        // Actualizar stock Flask
        try {
            Http::timeout(3)->patch(
                "{$this->inventarioUrl}/stock/{$productoId}?cantidad={$cantidad}"
            );
        } catch (\Exception $e) {
            return response()->json([
                'error' => 'Venta registrada pero error al actualizar stock'
            ], 500);
        }

        return response()->json([
            'mensaje' => 'Venta registrada exitosamente',
            'venta'   => $ventaResponse->json()
        ], 201);
    }

    public function consultarVentas()
    {
        try {
            $response = Http::timeout(3)->get("{$this->ventasUrl}/ventas");
            return response()->json($response->json());
        } catch (\Exception $e) {
            return response()->json([
                'error' => 'Servicio de ventas no disponible'
            ], 503);
        }
    }

    //Preguntar venta id express
    public function consultarVenta($id)
    {
        try {
            $response = Http::timeout(3)->get("{$this->ventasUrl}/ventas/{$id}");
            return response()->json($response->json());
        } catch (\Exception $e) {
            return response()->json([
                'error' => 'Servicio de ventas no disponible'
            ], 503);
        }
    }
}