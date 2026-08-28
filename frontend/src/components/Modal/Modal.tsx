import React from 'react';

export interface ModalProps {
    className?: string;
    children?: React.ReactNode;
}

export const Modal: React.FC<ModalProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
