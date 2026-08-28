import React from 'react';

export interface ButtonProps {
    className?: string;
    children?: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
