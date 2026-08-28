import React from 'react';

export interface InputProps {
    className?: string;
    children?: React.ReactNode;
}

export const Input: React.FC<InputProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
