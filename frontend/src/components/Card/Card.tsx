import React from 'react';

export interface CardProps {
    className?: string;
    children?: React.ReactNode;
}

export const Card: React.FC<CardProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
