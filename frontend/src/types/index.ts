export interface User {
  id: number;
  username: string;
  is_admin: boolean;
  last_login: string | null;
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  password: string;
}

export interface ChangePasswordData {
  current_password: string;
  new_password: string;
}

export interface Token {
  access_token: string;
  token_type: string;
  expires_in?: string;
}

export interface LastLoginResponse {
  fecha: string;
  hora: string;
  zona_horaria: string;
}

export interface ApiError {
  detail: string;
}
