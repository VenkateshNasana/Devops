import React from 'react';

export interface ToastProps {
    className?: string;
    children?: React.ReactNode;
}

export const Toast: React.FC<ToastProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
