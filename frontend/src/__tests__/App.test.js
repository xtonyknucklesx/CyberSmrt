import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from '../App';

test('renders learn react link', () => {
  render(<App />);
  const headingElement = screen.getByText(/CyberSmrt is going to win/i);
  expect(headingElement).toBeInTheDocument();
});