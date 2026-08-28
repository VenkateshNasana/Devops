import React from 'react';

export interface FooterProps {
    className?: string;
    children?: React.ReactNode;
}

export const Footer: React.FC<FooterProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
