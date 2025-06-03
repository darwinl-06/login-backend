'use client';

import { useState, useEffect } from 'react';
import { ProtectedRoute } from '@/components/ProtectedRoute';
import { Navbar } from '@/components/Navbar';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { useAuth } from '@/contexts/AuthContext';
import { authService } from '@/lib/services';
import { LastLoginResponse } from '@/types';
import { Calendar, Clock, MapPin, User, Shield } from 'lucide-react';
import Link from 'next/link';

export default function DashboardPage() {
  const { user } = useAuth();
  const [lastLogin, setLastLogin] = useState<LastLoginResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchLastLogin = async () => {
      try {
        const response = await authService.getLastLogin();
        setLastLogin(response);
      } catch (error: any) {
        setError('Error al cargar información del último acceso');
      } finally {
        setLoading(false);
      }
    };

    fetchLastLogin();
  }, []);

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        
        <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          <div className="px-4 py-6 sm:px-0">
            <div className="border-4 border-dashed border-gray-200 rounded-lg p-8">
              {/* Header */}
              <div className="mb-8">
                <h1 className="text-3xl font-bold text-gray-900 mb-2">
                  ¡Bienvenido, {user?.username}!
                </h1>
                <p className="text-gray-600">
                  Este es tu panel de control personal
                </p>
              </div>

              {/* Cards Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
                {/* User Info Card */}
                <Card>
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">
                      Información de Usuario
                    </CardTitle>
                    <User className="h-4 w-4 text-muted-foreground" />
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-2">
                      <div className="flex items-center space-x-2">
                        <span className="text-sm text-gray-600">Usuario:</span>
                        <span className="font-medium">{user?.username}</span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <span className="text-sm text-gray-600">Tipo:</span>
                        {user?.is_admin ? (
                          <Badge variant="default" className="flex items-center">
                            <Shield className="h-3 w-3 mr-1" />
                            Administrador
                          </Badge>
                        ) : (
                          <Badge variant="secondary">Usuario</Badge>
                        )}
                      </div>
                    </div>
                  </CardContent>
                </Card>

                {/* Last Login Card */}
                <Card>
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">
                      Último Acceso
                    </CardTitle>
                    <Clock className="h-4 w-4 text-muted-foreground" />
                  </CardHeader>
                  <CardContent>
                    {loading ? (
                      <div className="animate-pulse">
                        <div className="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
                        <div className="h-4 bg-gray-200 rounded w-1/2"></div>
                      </div>
                    ) : error ? (
                      <Alert variant="destructive">
                        <AlertDescription className="text-xs">{error}</AlertDescription>
                      </Alert>
                    ) : lastLogin ? (
                      <div className="space-y-2">
                        <div className="flex items-center space-x-2">
                          <Calendar className="h-3 w-3 text-gray-500" />
                          <span className="text-sm">{lastLogin.fecha}</span>
                        </div>
                        <div className="flex items-center space-x-2">
                          <Clock className="h-3 w-3 text-gray-500" />
                          <span className="text-sm">{lastLogin.hora}</span>
                        </div>
                        <div className="flex items-center space-x-2">
                          <MapPin className="h-3 w-3 text-gray-500" />
                          <span className="text-xs text-gray-600">{lastLogin.zona_horaria}</span>
                        </div>
                      </div>
                    ) : null}
                  </CardContent>
                </Card>

                {/* Quick Actions Card */}
                <Card>
                  <CardHeader>
                    <CardTitle className="text-sm font-medium">
                      Acciones Rápidas
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="space-y-2">
                    <Link href="/profile">
                      <Button variant="outline" size="sm" className="w-full justify-start">
                        <User className="h-4 w-4 mr-2" />
                        Ver Perfil
                      </Button>
                    </Link>
                    {user?.is_admin && (
                      <Link href="/admin">
                        <Button variant="outline" size="sm" className="w-full justify-start">
                          <Shield className="h-4 w-4 mr-2" />
                          Panel de Admin
                        </Button>
                      </Link>
                    )}
                  </CardContent>
                </Card>
              </div>

              {/* Welcome Message */}
              <Card>
                <CardHeader>
                  <CardTitle>Bienvenido a Login Platform</CardTitle>
                  <CardDescription>
                    Tu plataforma de gestión de usuarios y autenticación
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="prose prose-sm max-w-none">
                    <p className="text-gray-600 mb-4">
                      Desde aquí puedes gestionar tu perfil, cambiar tu contraseña y acceder 
                      a todas las funcionalidades de la plataforma.
                    </p>
                    
                    {user?.is_admin && (
                      <Alert>
                        <Shield className="h-4 w-4" />
                        <AlertDescription>
                          Como administrador, tienes acceso completo al panel de administración 
                          donde puedes gestionar usuarios, resetear contraseñas y más.
                        </AlertDescription>
                      </Alert>
                    )}
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </main>
      </div>
    </ProtectedRoute>
  );
}
