import { apiClient } from './apiService';

export const login = async (username, password) => {
    try {
        const response = await apiClient.post('/auth/login', { username, password });
        return response.data;
    } catch (error) {
        console.error('Login failed:', error);
        throw error;
    }
};